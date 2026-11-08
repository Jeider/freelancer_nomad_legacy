"""Pythonlancer parking commandants: source coverage, per-base scripts and DATA plan.

Installed as managers.parking_commandants. All game/staging writes use DataFolder.
"""
import copy
import datetime
import hashlib
import json
from pathlib import Path
import re

from files.rpg_runtime import dialog_ini, SESSION_THN
from story.rpg.script import RpgScript
from files.rpg_reputation import parking_scenario, parking_rules

MISSING_INTERIORS = {'co_mad_04_base', 'arch_01_base', 'heavy_barrel2_01_base'}
DONOR = 'co_och_01_base'
AVALON = 'br_avl_01_base'
GENERIC_HEADS = ['ge_male1_head', 'ge_male2_head', 'ge_male3_head', 'ge_male4_head',
                 'ge_male6_head', 'ge_male7_head', 'pl_male1_head', 'pl_male2_head',
                 'pl_male3_head', 'pl_male4_head', 'pl_male5_head', 'pl_male6_head']
SURNAMES = {
    'rh': ['Adler','Vogel','Keller','Brandt','Fischer','Weber','Wolf','Braun','Kraus','Stein'],
    'li': ['Carter','Hayes','Morgan','Reed','Grant','Brooks','Cole','Ward','Turner','Miller','Bennett','Shaw','Parker','Wells','Davis','Stone','Harris','Blake'],
    'br': ['Whitmore','Bennett','Hawthorne','Ashford','Sinclair','Clarke','Hughes','Lancaster','Pembroke','Sutton','Barrett'],
    'ku': ['Sato','Mori','Tanaka','Kato','Abe','Hayashi','Kondo','Shimizu','Ishida','Watanabe','Okada','Nakamura'],
    'free': ['Vega','Ramos','Silva','Cruz','Navarro','Ortega','Serrano','Duarte','Rojas','Costa']}


def parse(content):
    if isinstance(content, bytes):
        try: content = content.decode('utf-8-sig')
        except UnicodeDecodeError: content = content.decode('cp1251')
    rows = []
    for line in content.splitlines():
        line = line.split(';', 1)[0].strip()
        if line.startswith('[') and line.endswith(']'):
            rows.append((line[1:-1].lower(), {}))
        elif '=' in line and rows:
            k, v = line.split('=', 1)
            rows[-1][1].setdefault(k.strip().lower(), []).append(v.strip())
    return rows


def one(row, key, default=''):
    return row.get(key, [default])[-1]


def source_bases(universe):
    result = []
    for system in universe.universe_root.get_all_systems():
        if not system.have_dynamic_content(): continue
        for base in system.get_dockable_objects():
            if not base.IS_BASE or not base.have_shipdealer(): continue
            name = base.get_ru_name()
            result.append(dict(base=base.get_base_nickname().lower(), system=system.NAME,
                               faction=base.get_faction().CODE, name_ru=name.get_ru().replace('+',''),
                               name_en=name.get_en().replace('+',''), locked=bool(base.LOCKED_DOCK)))
    if len({r['base'] for r in result}) != len(result):
        raise ValueError('Duplicate Pythonlancer shipdealer base')
    return result


def assign_registry(project, bases):
    path = project / 'story/rpg/parking_commandants.json'
    old = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'bases': []}
    previous = {r['base']: r for r in old['bases']}
    groups = {r['group'] for r in old['bases']}
    owners_registry = project/'story/rpg/courier_owners.json'
    if owners_registry.exists():
        groups.update(r['group'] for r in json.loads(owners_registry.read_text(encoding='utf-8'))['bases'])
    groups.update(p.stem for p in (project/'story/rpg').glob('rm*.json'))
    result, counts = [], {}
    costumes = {tuple(r['appearance'].values()) for r in old['bases'] if 'appearance' in r}
    costumes.add(('br_captain_head','br_male_elite_body'))
    used_costumes = {('br_captain_head','br_male_elite_body')}
    for row in sorted(bases, key=lambda r:r['base']):
        base = row['base']
        if base == AVALON:
            result.append(dict(row, group='rm0002', authored=True))
            continue
        region = row['faction'][:2] if row['faction'] in ('rh_grp','li_grp','br_grp','ku_grp') else 'free'
        index = counts.get(region, 0); counts[region] = index + 1
        if base in previous:
            entry = dict(previous[base], **row)
            costume = (entry['appearance']['head'], entry['appearance']['body'])
            if costume in used_costumes:
                head = next(h for h in GENERIC_HEADS if (h,costume[1]) not in costumes)
                entry['appearance'] = {'head':head,'body':costume[1]}
                costumes.add((head,costume[1]))
        else:
            number = next(n for n in range(100,10000) if f'rm{n:04d}' not in groups)
            group = f'rm{number:04d}'; groups.add(group)
            heads = ([region+'_captain_head'] if region != 'free' else ['pi_pirate1_head','pi_pirate2_head']) + GENERIC_HEADS
            bodies = [region+'_male_elite_body',region+'_male_guard_body'] if region != 'free' else ['pi_pirate1_body','pi_pirate2_body','pi_pirate6_body','pl_male2_journeyman_body']
            combos = [(h,b) for h in heads for b in bodies]
            h,b = next(c for c in combos if c not in costumes)
            costumes.add((h,b))
            entry = dict(row, group=group, region=region, surname=SURNAMES[region][index % len(SURNAMES[region])],
                         style=index % 4, appearance={'head':h,'body':b})
        used_costumes.add((entry['appearance']['head'],entry['appearance']['body']))
        result.append(entry)
    return {'schema':1, 'bases':result}


def scenario(template, entry):
    data = parking_scenario(template)
    group, base = entry['group'], entry['base']
    data.update(id=group, status='generated', scenario='parking_commandant', local_scene=True,
                appearance=entry['appearance'], vendor_posture=entry['posture'])
    seller = 'park_' + base.removesuffix('_base')
    data['binding']['vendor'] = seller
    data['parking'] = {'base':base,'seller':seller}
    data['rules']['first_greeting'] = group+'_frag0001'
    name, ru, officer = entry['name_en'], entry['name_ru'], entry['surname']
    style = entry['style']
    greetings = [
        f'Welcome to {name}. I am Commandant {officer}. I handle parking berths here.',
        f'Commandant {officer}, at your service. If you need to store a ship at {name}, talk to me.',
        f'You have reached the parking office for {name}. Commandant {officer}. What can I do for you?',
        f'Hello, pilot. I am {officer}, the parking commandant at {name}. Looking for a berth?']
    replacements = {
        '0001': (f'Добро пожаловать. {ru}. Я комендант стоянки {officer}. Нужно место для корабля?',greetings[style]),
        '0005': (f'Оплата принята. {ru}: место закреплено за тобой. Можешь оставить корабль.', f'Payment received. Your berth at {name} is registered. You can store a ship here now.'),
        '0011': (f'Место действует только здесь: {ru}. На другой базе его нужно покупать отдельно.', f'This berth is only valid at {name}. You will need a separate berth at any other base.'),
        '0015': ('Ты уже приобрёл все доступные тебе места на этой базе. Ещё одно оформить не могу.', 'You already own the maximum number of berths at this base. I cannot register another one.'),
        '0018': ('На этом всё. До встречи, комендант.', 'That is all for now. Goodbye, Commandant.'),
        '0020': (f'С возвращением. Комендант {officer} слушает. По поводу стоянки?', f'Welcome back. Commandant {officer} speaking. Here about ship storage?'),
        '0021': (f'Привет, Трент. Стоянка базы «{ru}» к твоим услугам.', f'Hello, Trent. Need another berth at {name}?')}
    for row in data['fragments']:
        suffix = row['id'][-4:]
        row['id'] = group+'_frag'+suffix
        if suffix in replacements: row['ru'], row['en'] = replacements[suffix]
    for node in data['nodes'].values():
        for key in ('text_en','text_ru'):
            if key in node:
                node[key] = node[key].replace('Avalon','{base}').replace('Авалона','{base}').replace('Авалоне','{base}')
    data['choices']['leave'].update(ru='До встречи, комендант',en='Goodbye, Commandant')
    RpgScript(data)
    return data


def session(script):
    text = SESSION_THN.replace('Actor="rpg_biz_contact"', 'Actor="'+script.data['binding']['vendor']+'"')
    if script.data.get('vendor_posture') == 'sit':
        text = text.replace('{"RpgVendor"},{animation="Sc_MLBODY_STND_IDLE_000LV_XB_04"',
                            '{"RpgVendor"},{animation="Sc_MLBODY_CHRB_IDLE_000LV_XA_05"')
    return text.encode('utf-8')


def plan(project, folder, registry, assets_root=None):
    """Validate every room/costume/marker before publishing any contact."""
    from tools.data_folder import DataFolder
    assets = DataFolder(root=assets_root or project.parent.parent)
    files = {}
    def read(path):
        path = path.replace('\\','/')
        if path in files: return files[path]
        target = folder.data_path(path)
        return target.read_bytes() if target.exists() else assets.data_path(path).read_bytes()
    definitions = {}
    for kind,row in parse(read('UNIVERSE/universe.ini')):
        if kind=='base': definitions.setdefault(one(row,'nickname').lower(), one(row,'file'))
    reserved = {}; base = room = ''
    for kind,row in parse(read('MISSIONS/mbases.ini')):
        if kind=='mbase': base = one(row,'nickname').lower()
        elif kind=='mroom':
            room=one(row,'nickname').lower()
            for f in row.get('fixture',[]):
                reserved.setdefault((base,room),set()).add(f.split(',')[1].strip().lower())
    contact_catalog = read('RPG/contacts.ini')
    owner_catalog = folder.data_path('RPG/courier_contacts.ini')
    if not owner_catalog.exists(): owner_catalog = assets.data_path('RPG/courier_contacts.ini')
    if owner_catalog.exists(): contact_catalog += b'\n' + owner_catalog.read_bytes()
    for kind,row in parse(contact_catalog):
        if kind!='rpgcontact' or one(row,'enabled').lower() not in ('1','true'): continue
        contact=parse(read(one(row,'rtc')))
        loc=one(next(r for k,r in contact if k=='characterencounter'),'location')
        base,room=[p.strip().lower() for p in loc.split(',')]
        for k,r in contact:
            if k=='reserve': reserved.setdefault((base,room),set()).update(s.lower() for s in r.get('spot',[]))
    parts={one(r,'nickname').lower() for k,r in parse(read('CHARACTERS/bodyparts.ini'))}
    config = read('RPG/ship_parking.ini').decode('utf-8-sig')
    prices={one(r,'base').lower():r for k,r in parse(config) if k=='parkingbase'}
    catalog = read('RPG/parking_contacts.ini').decode('utf-8-sig')
    known={one(r,'base').lower():r for k,r in parse(catalog) if k=='rpgcontact'}
    template=json.loads((project/'story/rpg/rm0002.json').read_text(encoding='utf-8'))
    scripts={}; report=[]
    for entry in registry['bases']:
        base=entry['base']; path=definitions[base].replace('\\','/')
        try: definition=read(path)
        except FileNotFoundError:
            if base not in MISSING_INTERIORS: raise
            donor=read(definitions[DONOR]).decode('utf-8-sig')
            definition=re.sub(r'(?im)^(nickname\s*=\s*)co_och_01_base\s*$',lambda m:m[1]+base,donor).encode('utf-8')
            files[path]=definition
        rooms=parse(definition)
        bar=next((r for k,r in rooms if k=='room' and one(r,'nickname').lower()=='bar'),None)
        if bar is None: raise ValueError('Shipdealer has no bar: '+base)
        barfile=one(bar,'file'); roomdata=parse(read(barfile))
        layout=b'\n'.join(read(p) for k,r in roomdata if k=='room_info' for p in r.get('set_script',[]))
        candidates=sorted(set(re.findall(rb'Zg/NPC/m[A-Za-z0-9_/]+/A/(?:Stand|SitLow)',layout)),key=lambda p:(not p.endswith(b'/Stand'),p))
        viable=[]
        for candidate in candidates:
            spot=candidate.decode(); prefix=spot.rsplit('/A/',1)[0].replace('Zg/','Zs/',1)
            if spot.lower() in reserved.get((base,'bar'),set()): continue
            if all((prefix+s).encode() in layout for s in ('/P/Stand','/PCU/Camera','/ACU/Camera')): viable.append(spot)
        if not viable: raise ValueError('No safe bar marker with both cameras: '+base)
        target='RPG/parking/'+base+'.ini'; seller='park_'+base.removesuffix('_base')
        if base in prices and one(prices[base],'seller')!=seller: raise ValueError('Custom seller needs explicit mapping: '+base)
        if entry.get('authored'):
            content=read(target)
            original=next(r for k,r in parse(content) if k=='char')
            spot=one(original,'spot')
            if spot not in viable: raise ValueError('Authored Avalon marker became unavailable')
            report.append(dict(entry,spot=spot,posture='stand',contact=target))
            continue
        # A stable base hash distributes new commandants among free placements.
        seed=int(hashlib.sha256(base.encode()).hexdigest()[:8],16)
        standing=[s for s in viable if s.endswith('/Stand')]
        choices=standing or viable; spot=choices[seed%len(choices)]
        entry['spot']=spot; entry['posture']='stand' if spot.endswith('/Stand') else 'sit'
        for part in entry['appearance'].values():
            if part.lower() not in parts: raise ValueError('Missing costume: '+part)
        data=scenario(template,entry); script=RpgScript(data); scripts[script.name]=data
        fidget='stand' if entry['posture']=='stand' else 'sit'
        files[target]=(f'[CharacterEncounter]\nLocation = {base}, Bar\nchoices = true\nicon = rumor\ndialog = RPG\\{script.name}_dialog.ini\n\n'
                       f'[Reserve]\nspot = {spot}\n\n[Char]\nnpc = {seller}\nactor = {seller}\nspot = {spot}\nfidget = scripts\\extras\\fidget_{fidget}_male_01.thn\n\n'
                       f'[NPC]\nnickname = {seller}\nbody = {entry["appearance"]["body"]}\nhead = {entry["appearance"]["head"]}\n'
                       f'lefthand = benchmark_male_hand_left\nrighthand = benchmark_male_hand_right\naffiliation = {entry["faction"]}\nvoice = rvp101\nindividual_name = 238390\n').encode()
        # Never replay stale words if a source scenario was edited after recording.
        available=set()
        manifest=folder.data_path(f'SCRIPTS/RPG/{script.name}/en/manifest.json')
        if manifest.exists():
            recorded={r['id']:r for r in json.loads(manifest.read_text(encoding='utf-8'))['fragments']}
            for row in script.fragments:
                saved=recorded.get(row['id'])
                if saved and saved['text']==row['en'] and all(folder.data_path(saved[k]).is_file() for k in ('path','audio')):
                    available.add(row['id'])
        ini=dialog_ini(script,available).replace('scene_group = '+script.name+'\n','scene_group = '+script.name+'\nlocal_scene = 1\n',1)
        files[f'RPG/{script.name}_dialog.ini']=ini.encode('utf-8')
        files[f'SCRIPTS/RPG/{script.name}/conversation.thn']=session(script)
        if base not in prices: config+=f'\n[ParkingBase]\nbase = {base}\nseller = {seller}\n'
        if base not in known: catalog+=f'\n[RpgContact]\nnickname = {seller}\nenabled = true\nbase = {base}\nrtc = RPG\\parking\\{base}.ini\n'
        report.append(dict(entry,contact=target,voiced=len(available)))
    config=parking_rules(config,{r['base']:r['faction'] for r in registry['bases']})
    files['RPG/ship_parking.ini']=config.encode('utf-8')
    files['RPG/parking_contacts.ini']=catalog.encode('utf-8')
    from managers.parking_rooms import plan_room_hotspots
    room_files, room_coverage = plan_room_hotspots([r['base'] for r in registry['bases']], definitions, read)
    files.update(room_files)
    from managers.parking_ui import plan as plan_ui
    files.update(plan_ui(project, read))
    by_base = {row['base']: row['rooms'] for row in room_coverage}
    for row in report:
        row['parking_rooms'] = by_base[row['base']]
    return files,scripts,report


def sync_from_universe(universe, folder):
    """Called after Pythonlancer has exported its room definitions, including builds."""
    project=Path(__file__).resolve().parents[1]
    registry=assign_registry(project,source_bases(universe))
    files,scripts,report=plan(project,folder,registry)
    output=project/'results/parking_commandants'
    output.mkdir(parents=True,exist_ok=True)
    for group,data in scripts.items():
        (project/'story/rpg'/f'{group}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (project/'story/rpg/parking_commandants.json').write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    folder.sync_parking_commandants(files,output/'backups'/datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f'))
    (output/'coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return report
