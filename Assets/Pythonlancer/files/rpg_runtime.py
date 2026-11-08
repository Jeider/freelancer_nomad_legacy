"""Render the INI graph consumed by Content.dll and the persistent room setup."""
import re


def dialog_ini(script, voiced_fragments=None):
    data = script.data
    pools = {}
    for fragment in script.fragments:
        pools.setdefault(fragment['pool'], []).append(fragment)
    lines = ['[Dialog]', 'nickname = ' + script.name, 'scene_group = ' + script.name, 'start = ' + data['start']]
    if 'parking' in data:
        lines += ['parking_base = ' + data['parking']['base'],
                  'parking_seller = ' + data['parking']['seller']]
    rep = data['rules']['reputation']
    if 'parking' not in data and rep.get('enabled') and rep.get('minimum') is not None:
        lines += ['reputation_faction = rh_grp', 'minimum_reputation = ' + str(rep['minimum'])]
        if rep.get('strict'):
            lines.append('reputation_strict = 1')
    for name, node in data['nodes'].items():
        rows = pools[node['pool']]
        lines += ['', '[DialogNode]', 'nickname = ' + name,
                  'text_ru = ' + node.get('text_ru', rows[0]['ru']),
                  'text_en = ' + node.get('text_en', rows[0]['en'])]
        lines += ['fragment = ' + row['id'] for row in rows
                  if voiced_fragments is None or row['id'] in voiced_fragments]
        if node.get('choices') == 'wagons':
            lines.append('escape = resume')
        for key in data['choice_sets'].get(node.get('choices'), []):
            choice = data['choices'][key]
            lines += ['', '[DialogChoice]', 'node = ' + name,
                      'text_ru = ' + choice['ru'], 'text_en = ' + choice['en']]
            lines += ['fragment = ' + row['id'] for row in pools[choice['pool']]
                      if voiced_fragments is None or row['id'] in voiced_fragments]
            if 'action' in choice:
                lines.append('action = ' + choice['action'])
            if 'first_wagons' in choice:
                lines.append('first_wagons = ' + str(choice['first_wagons']))
            outcomes = choice.get('outcomes', {})
            target = choice.get('goto') or outcomes.get('eligible') or outcomes.get('started')
            if target:
                lines.append('goto = ' + target)
            lines += [outcome + ' = ' + target for outcome, target in outcomes.items()
                      if outcome in ('bad_reputation', 'busy', 'failed')]
    return '\n'.join(lines) + '\n'


def bind_contact(content):
    chunks = re.split(rb'(?m)(?=^\[)', content)
    result = []
    found = False
    for chunk in chunks:
        header = chunk.splitlines()[0].strip().lower() if chunk else b''
        if header in (b'[dialog]', b'[dialognode]', b'[dialogchoice]'):
            continue
        if header == b'[npc]' and re.search(rb'(?im)^nickname\s*=\s*rpg_biz_contact\s*$', chunk):
            chunk = re.sub(rb'(?im)^body\s*=[^\r\n]*', b'body = rh_commtrader_body', chunk)
            chunk = re.sub(rb'(?im)^accessory\s*=\s*prop_hat_male_rh_elite\s*\r?\n', b'', chunk)
        if header == b'[characterencounter]':
            found = True
            chunk = re.sub(rb'(?im)^\s*(click_script|dialog|icon)\s*=.*\r?\n', b'', chunk)
            pos = chunk.index(b'\n') + 1
            chunk = chunk[:pos] + b'dialog = RPG\\rm0001_dialog.ini\r\nicon = mission\r\n' + chunk[pos:]
        result.append(chunk)
    if not found or b'rpg_biz_contact' not in content:
        raise ValueError('Unexpected Bismarck contact configuration')
    return b''.join(result)


SESSION_THN = '''-- Persistent setup: placement and cameras once; speech uses separate entries.
duration=86400
entities={
 {entity_name="RpgMonitor",type=MONITOR,template_name=""},
 {entity_name="special/p",type=MARKER,template_name="",spatialprops={pos={0,0,0},orient={{1,0,0},{0,1,0},{0,0,1}}}},
 {entity_name="RpgCamera_player",type=CAMERA,template_name="",cameraprops={fovh=30,hvaspect=1.333333,nearplane=.1,farplane=10000}},
 {entity_name="RpgCamera_vendor",type=CAMERA,template_name="",cameraprops={fovh=30,hvaspect=1.333333,nearplane=.1,farplane=10000}},
 {entity_name="RpgPlayer",type=DEFORMABLE,template_name="",flags=LIT_DYNAMIC,userprops={Actor="Player",category="Character"}},
 {entity_name="RpgVendor",type=DEFORMABLE,template_name="",flags=LIT_DYNAMIC,userprops={Actor="rpg_biz_contact",category="Character"}}
}
events={
 {0,ATTACH_ENTITY,{"RpgPlayer","special/p"},{duration=.01,offset={0,0,0},target_type=ROOT,flags=POSITION+ORIENTATION}},
 {0,START_MOTION,{"RpgPlayer"},{animation="Sc_MLBODY_STND_IDLE_000LV_XB_04",duration=86400,time_scale=1,start_time=0,weight=1,heading=-1,event_flags=2}},
 {0,START_MOTION,{"RpgVendor"},{animation="Sc_MLBODY_STND_IDLE_000LV_XB_04",duration=86400,time_scale=1,start_time=0,weight=1,heading=-1,event_flags=2}},
 {0,SET_CAMERA,{"RpgMonitor","RpgCamera_vendor"}},
 {0.02,START_IK,{"RpgPlayer","RpgVendor"},{duration=86399,end_effector="Body_Head",transition_duration=.3,target_part="Body_Head",target_type=PART,count_to_root=1,damping=1,up=NEG_Y_AXIS,front=Z_AXIS,point_at=1,move_to=0,event_flags=128}},
 {0.02,START_IK,{"RpgVendor","RpgPlayer"},{duration=86399,end_effector="Body_Head",transition_duration=.3,target_part="Body_Head",target_type=PART,count_to_root=1,damping=1,up=NEG_Y_AXIS,front=Z_AXIS,point_at=1,move_to=0,event_flags=128}},
 {0.02,START_IK,{"RpgPlayer","RpgVendor"},{duration=86399,end_effector="Eye IK Left",transition_duration=.2,target_part="Body_Head",target_type=PART,count_to_root=1,damping=1,up=NEG_Y_AXIS,front=Z_AXIS,point_at=1,move_to=0,event_flags=128}},
 {0.02,START_IK,{"RpgVendor","RpgPlayer"},{duration=86399,end_effector="Eye IK Left",transition_duration=.2,target_part="Body_Head",target_type=PART,count_to_root=1,damping=1,up=NEG_Y_AXIS,front=Z_AXIS,point_at=1,move_to=0,event_flags=128}}
}
'''

