"""Locomotive owners: source selection, placement and a pure DATA publication plan.

Voice groups are shared explicitly; session groups own the room pose and gestures.
No recordings are synthesized or modified by this generator.
"""
import copy
import datetime
import hashlib
import json
from pathlib import Path
import re

from managers.parking_commandants import parse, one, session, GENERIC_HEADS
from files.rpg_runtime import dialog_ini
from story.rpg.script import RpgScript


def asset_path(project, folder, name):
    """Builds use newly generated rooms first and installed shared assets second."""
    path=folder.data_path(name)
    if path.exists():return path
    from tools.data_folder import DataFolder
    return DataFolder(root=project.parent.parent).data_path(name)


def source_bases(universe):
    from universe.content import meta
    rows = []
    for system in universe.universe_root.get_all_systems():
        if not system.have_dynamic_content():
            continue
        for obj in system.get_dockable_objects():
            if not obj.IS_BASE or obj.LOCKED_DOCK or not isinstance(obj.BASE_PROPS, (meta.LargePlanet, meta.Megabase)):
                continue
            name = obj.get_ru_name()
            rows.append(dict(base=obj.get_base_nickname().lower(), system=system.NAME,
                             faction=obj.get_faction().CODE, economic_type=type(obj.BASE_PROPS).__name__,
                             name_ru=name.get_ru().replace('+', ''), name_en=name.get_en().replace('+', '')))
    return sorted(rows, key=lambda r:r['base'])


def assign_registry(project, rows):
    path = project / 'story/rpg/courier_owners.json'
    old = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'bases': []}
    previous = {r['base']: r for r in old['bases']}
    used = {r['group'] for r in old['bases']}
    used.update(p.stem for p in (project/'story/rpg').glob('rm*.json'))
    parking = project/'story/rpg/parking_commandants.json'
    if parking.exists():
        used.update(r['group'] for r in json.loads(parking.read_text(encoding='utf-8'))['bases'])
    result = []
    for row in rows:
        base = row['base']
        if base in previous:
            entry = dict(previous[base], **row)
        else:
            group = next(f'rm{n:04d}' for n in range(200, 10000) if f'rm{n:04d}' not in used)
            used.add(group)
            region = row['faction'][:2]
            if region not in ('rh','li','br','ku'):
                raise ValueError('Define a civilian costume for '+base)
            entry = dict(row, group=group, voice_group='rm0001',
                         actor='loco_'+base.removesuffix('_base'),
                         appearance={'head':GENERIC_HEADS[len(result) % len(GENERIC_HEADS)],
                                     'body':region+'_commtrader_body'})
        if base == 'rh_biz_01_base':
            entry['actor'] = 'rpg_biz_contact'
            entry['appearance'] = {'head':'br_brighton_head','body':'rh_commtrader_body'}
        result.append(entry)
    if len({r['base'] for r in result}) != len(result) or len({r['group'] for r in result}) != len(result):
        raise ValueError('Duplicate courier owner base/session group')
    return {'schema':1, 'bases':result}


def transfer_plan(project, folder, registry):
    """Recreate transfer registrations after universe/mbases export, including builds."""
    read = lambda p: asset_path(project, folder, p).read_bytes()
    catalog = parse(read('MISSIONS/TrainCourier/catalog.ini'))
    universe = read('UNIVERSE/universe.ini')
    mbases = read('MISSIONS/mbases.ini')
    definitions = {one(r, 'nickname'): r for k, r in parse(universe) if k == 'base'}
    systems = {one(r, 'nickname') for k, r in parse(universe) if k == 'system'}
    mission = {one(r, 'nickname') for k, r in parse(mbases) if k == 'mbase'}
    factions = {}
    for kind, row in catalog:
        if kind in ('courierpoint', 'courierparking'):
            system = one(row, 'system')
            expected = 'tc_' + system + '_base'
            if one(row, 'transfer_base') != expected:
                raise ValueError('Unexpected locomotive transfer base for ' + system)
            factions.setdefault(system, one(row, 'faction'))
    for row in registry['bases']:
        factions.setdefault(row['system'], row['faction'])
    files = {}
    for system, faction in sorted(factions.items()):
        if system not in systems or not re.fullmatch(r'[a-z0-9_]+', system) or not faction:
            raise ValueError('Missing transfer system or faction: ' + system)
        base = 'tc_' + system + '_base'
        path = f'UNIVERSE/TrainCourier/{base}.ini'
        definition = definitions.get(base)
        if definition is None:
            universe += (f'\n[Base]\nnickname = {base}\nsystem = {system}\nstrid_name = 1\n'
                         f'file = Universe\\TrainCourier\\{base}.ini\nautosave_forbidden = true\n').encode()
        elif (one(definition, 'system') != system or
              one(definition, 'file').replace('\\', '/').lower() != path.lower()):
            raise ValueError('Conflicting locomotive transfer definition: ' + base)
        if base not in mission:
            mbases += (f'\n[MBase]\nnickname = {base}\nlocal_faction = {faction}\ndiff = 1\n'
                       '\n[MRoom]\nnickname = Deck\ncharacter_density = 0\n').encode()
        defaults = {
            path: (f'[BaseInfo]\nnickname = {base}\nstart_room = Deck\n\n[Room]\n'
                   'nickname = Deck\nfile = Universe\\ROOM\\KU\\battleship_deck.ini\n'),
            f'MISSIONS/TrainCourier/launch_{system}.ini': (
                f'[CharacterEncounter]\nLocation = {base}, Deck\nautoplay = true\nrelocate_player = spaceflight\n'
                '\n[Char]\nnpc = test_npc_01\nactor = tc_transfer\nspot = Zs/NPC/Shipdealer/01/A/Stand\n'
                'fidget = scripts\\extras\\fidget_stand_male_NULL.thn\n'),
        }
        for name, default in defaults.items():
            source = asset_path(project, folder, name)
            files[name] = source.read_bytes() if source.exists() else default.encode()
    files['UNIVERSE/universe.ini'] = universe
    files['MISSIONS/mbases.ini'] = mbases
    return files


def extend_catalog(universe, folder, registry, project=None, universe_data=None):
    """Retain installed routes/economy, add missing owner depots and local berths."""
    from managers.courier_graph import paths_from
    from universe.content.main_objects import Jumpgate, DockableObject
    project=project or Path(__file__).resolve().parents[1]
    read = lambda p: asset_path(project,folder,p).read_bytes()
    content = read('MISSIONS/TrainCourier/catalog.ini').decode('utf-8-sig')
    rows = parse(content)
    points = {one(r,'base'):r for k,r in rows if k=='courierpoint'}
    parking = {one(r,'base'):r for k,r in rows if k=='courierparking'}
    goods = {one(r,'nickname') for k,r in rows if k=='couriercommodity'}
    routes = {(one(r,'source'),one(r,'destination')) for k,r in rows if k=='courierroute'}
    bases = {b.system_object.get_base_nickname().lower():b for b in universe.get_bases()}
    universe_data = read('UNIVERSE/universe.ini') if universe_data is None else universe_data
    definitions = {one(r,'nickname'):r for k,r in parse(universe_data) if k=='base'}
    systems = {one(r,'nickname'):one(r,'file') for k,r in parse(universe_data) if k=='system'}
    solars = {one(r,'nickname'):r for k,r in parse(read('SOLAR/solararch.ini')) if k=='solar'}
    extra = []
    new = set()
    for entry in registry['bases']:
        name, system = entry['base'], entry['system']
        if name not in definitions or name not in bases:
            raise ValueError('Missing owner base in universe export or source: '+name)
        if 'tc_'+system+'_base' not in definitions:
            raise ValueError('Missing locomotive transfer registration: tc_'+system+'_base (owner '+name+')')
        if name in points and name in parking:
            continue
        objects = [r for k,r in parse(read('UNIVERSE/'+systems[system])) if k=='object']
        anchors = [r for r in objects if one(r,'dock_with')==name]
        # Planet fixtures already have measured mount poses in CourierParking.
        anchor = next((r for r in anchors if one(solars.get(one(r,'archetype'),{}),'type').upper() not in ('DOCKING_RING','JUMP_HOLE','JUMP_GATE') and one(r,'archetype')!='docking_fixture'), None)
        if anchor is None:
            raise ValueError('Export the planet docking fixture before adding its owner: '+name)
        nick = one(anchor,'nickname')
        xyz = lambda r: [float(v) for v in one(r,'pos','0,0,0').split(',')]
        pos = xyz(anchor)
        assembly = [r for r in objects if one(r,'nickname')==nick or one(r,'nickname').startswith(nick+'_')]
        top = max(xyz(r)[1] + max(1500.,float(one(solars.get(one(r,'archetype'),{}),'solar_radius','1500'))) for r in assembly)
        pos[1] = max(pos[1]+4000, top+2000)
        yaw = float(one(anchor,'rotate','0,0,0').split(',')[1])
        common = (f'base = {name}\nsystem = {system}\nfaction = {entry["faction"]}\n'
                  f'name_ids = {one(definitions[name],"strid_name","0")}\n'
                  f'voice_name = {bases[name].get_base_msg_relative()}\ntransfer_base = tc_{system}_base\n')
        if name not in points:
            economy = []
            for c in bases[name].get_commodities_values():
                commodity = c.get_nickname()
                if commodity not in goods:
                    continue
                if c.in_stock():
                    economy += ['commodity = '+commodity, f'supply_price = {commodity}, {max(1,round(c.get_commodity_price()))}']
                if c.consume:
                    economy.append('demand = '+commodity)
            if not economy:
                raise ValueError('No supported economy for '+name)
            text = (f'\n[CourierPoint]\nnickname = {nick}_courier_point\n'+common+
                    'freight_hub = true\nlarge_planet = '+str(entry['economic_type'] in ('LargePlanet','ManhattanSuperPlanet')).lower()+
                    '\nposition = '+', '.join(map(str,pos))+f'\nrotation = 0, {yaw}, 0\n'+'\n'.join(economy)+'\n')
            extra.append(text);points[name] = parse(text)[0][1];new.add(name)
        if name not in parking:
            # Separate from freight tracks and their +350 m runtime offset.
            pos[1] += 1500
            text = (f'\n[CourierParking]\nnickname = {nick}_courier_berth\n'+common+
                    'position = '+', '.join(map(str,pos))+f'\nrotation = 0, {yaw}, 0\n')
            extra.append(text);parking[name] = parse(text)[0][1]
    excluded = set()
    for name in sorted(points):
        if name not in bases:
            continue
        root = bases[name].system_object
        graph = paths_from(root, Jumpgate, excluded)
        jumps = paths_from(root, Jumpgate, excluded, minimize_jumps=True)
        for obj, path in graph.items():
            if not isinstance(obj,DockableObject):
                continue
            target = obj.get_base_nickname().lower()
            key = name,target
            if target==name or target not in points or key in routes or not ({name,target}&new):
                continue
            extra.append(f'\n[CourierRoute]\nsource = {name}\ndestination = {target}\ndistance = {len(path)}\njumps = {sum(s["kind"]=="jumpgate" for s in jumps[obj])}\n')
            routes.add(key)
    for entry in registry['bases']:
        name = entry['base']
        if name not in parking or not any(a==name for a,b in routes):
            raise ValueError('Owner has no berth or outgoing routes: '+name)
    return (content+''.join(extra)).encode('utf-8')


def plan(project, folder, registry, catalog):
    from managers.rpg_scene import RpgSceneManager
    from story.rpg.scene import GestureScene, GESTURE_COUNT
    read = lambda p: asset_path(project,folder,p).read_bytes()
    definitions = {one(r,'nickname').lower():one(r,'file') for k,r in parse(read('UNIVERSE/universe.ini')) if k=='base'}
    reserved = {}
    base=room=''
    for k,r in parse(read('MISSIONS/mbases.ini')):
        if k=='mbase':base=one(r,'nickname').lower()
        if k=='mroom':
            room=one(r,'nickname').lower()
            reserved.setdefault((base,room),set()).update(f.split(',')[1].strip().lower() for f in r.get('fixture',[]))
    for catalog_name in ('RPG/contacts.ini','RPG/parking_contacts.ini'):
        for k,r in parse(read(catalog_name)):
            if k!='rpgcontact' or one(r,'enabled').lower() not in ('true','1') or one(r,'nickname')=='rpg_biz_contact':
                continue
            contact = parse(read(one(r,'rtc')))
            loc = next(one(c,'location') for kind,c in contact if kind=='characterencounter')
            base,room = [s.strip().lower() for s in loc.split(',')]
            for kind,c in contact:
                if kind=='reserve':reserved.setdefault((base,room),set()).update(s.lower() for s in c.get('spot',[]))
    parts={one(r,'nickname').lower() for k,r in parse(read('CHARACTERS/bodyparts.ini'))}
    files={'MISSIONS/TrainCourier/catalog.ini':catalog}
    entries=[]; report=[]
    for entry in registry['bases']:
        base,group=entry['base'],entry['group']
        source=RpgScript.load(project/'story/rpg'/f'{entry["voice_group"]}.json')
        bar=next((r for k,r in parse(read(definitions[base])) if k=='room' and one(r,'nickname').lower()=='bar'),None)
        if bar is None:raise ValueError('No bar for '+base)
        layout=b'\n'.join(read(p) for k,r in parse(read(one(bar,'file'))) if k=='room_info' for p in r.get('set_script',[]))
        spots=[]
        for candidate in sorted(set(re.findall(rb'Zg/NPC/m[A-Za-z0-9_/]+/A/(?:Stand|SitLow)',layout))):
            spot=candidate.decode();prefix=spot.rsplit('/A/',1)[0].replace('Zg/','Zs/',1)
            if spot.lower() not in reserved.get((base,'bar'),set()) and all((prefix+s).encode() in layout for s in ('/P/Stand','/PCU/Camera','/ACU/Camera')):
                spots.append(spot)
        if not spots:raise ValueError('No free conversation placement: '+base)
        preferred=entry.get('spot','Zg/NPC/mFloor2/01/A/Stand' if base=='rh_biz_01_base' else '')
        spot=preferred if preferred in spots else next((s for s in spots if s.endswith('/Stand')),spots[0])
        entry.update(spot=spot,posture='stand' if spot.endswith('/Stand') else 'sit')
        if not all(p.lower() in parts for p in entry['appearance'].values()):raise ValueError('Missing civilian costume: '+base)
        data=copy.deepcopy(source.data)
        data['binding']['vendor']=entry['actor'];data['vendor_posture']=entry['posture']
        script=RpgScript(data)
        voiced=set()
        for lang in ('ru','en'):
            manifest=asset_path(project,folder,f'SCRIPTS/RPG/{source.name}/{lang}/manifest.json')
            if not manifest.exists():continue
            current={r['id']:r for r in source.fragments}
            for row in json.loads(manifest.read_text(encoding='utf-8'))['fragments']:
                if row['id'] not in current or row['text']!=current[row['id']][lang]:continue
                if not asset_path(project,folder,row['audio']).exists():continue
                if any(hashlib.sha256(read(row[k])).hexdigest()!=row[h] for k,h in (('audio','audio_sha256'),('path','sha256'))):
                    raise ValueError('Rebuild voice scenes before owners: '+row['id'])
                voiced.add(row['id'])
        ini=dialog_ini(script,voiced).replace('nickname = '+source.name+'\n','nickname = '+entry['actor']+'_dialog\n',1)
        ini=ini.replace('[Dialog]\n',f'[Dialog]\ncourier_base = {base}\nsession_group = {group}\n',1)
        ini=ini.replace('reputation_faction = rh_grp','reputation_faction = '+entry['faction'])
        files[f'RPG/courier/{base}_dialog.ini']=ini.encode('utf-8')
        files[f'SCRIPTS/RPG/{group}/conversation.thn']=session(script)
        sounds=script.recording_group().get_sounds()
        templates=RpgSceneManager(project,script,folder.get_root()).templates
        for role in ('vendor','player'):
            index=next(i for i,r in enumerate(script.fragments) if r['role']==role)
            for step in range(GESTURE_COUNT):
                scene=GestureScene(templates,script,script.fragments[index],sounds[index],'en',20,'unused',step)
                files[f'SCRIPTS/RPG/{group}/gestures/{role}_{step+1:02d}.thn']=scene.get_content().encode('utf-8')
        actor=entry['actor'];appearance=entry['appearance']
        target='RPG/rh_biz_contact.ini' if base=='rh_biz_01_base' else f'RPG/courier/{base}.ini'
        files[target]=(f'[CharacterEncounter]\nLocation = {base}, Bar\nchoices = true\nicon = mission\ndialog = RPG\\courier\\{base}_dialog.ini\n\n'
                       f'[Reserve]\nspot = {spot}\n\n[Char]\nnpc = {actor}\nactor = {actor}\nspot = {spot}\n'
                       f'fidget = scripts\\extras\\fidget_{entry["posture"]}_male_01.thn\n\n'
                       f'[NPC]\nnickname = {actor}\nbody = {appearance["body"]}\nhead = {appearance["head"]}\n'
                       f'lefthand = benchmark_male_hand_left\nrighthand = benchmark_male_hand_right\naffiliation = {entry["faction"]}\nvoice = rvp101\nindividual_name = 238270\n').encode('utf-8')
        if base!='rh_biz_01_base':entries.append(f'[RpgContact]\nnickname = {actor}\nenabled = true\nbase = {base}\nrtc = {target.replace(chr(47),chr(92))}\n')
        report.append(dict(entry,voiced=len(voiced),pending=len(source.fragments)-len(voiced)))
    files['RPG/courier_contacts.ini']='\n'.join(entries).encode('utf-8')
    return files,report


def generate(universe, folder, project, output, dry_run=False):
    registry=assign_registry(project,source_bases(universe))
    transfers=transfer_plan(project,folder,registry)
    catalog=extend_catalog(universe,folder,registry,project,transfers['UNIVERSE/universe.ini'])
    files,report=plan(project,folder,registry,catalog)
    files.update(transfers)
    output.mkdir(parents=True,exist_ok=True)
    (output/'coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    if not dry_run:
        folder.sync_courier_owners(files,output/'backups'/datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f'))
        (project/'story/rpg/courier_owners.json').write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return files,registry,report


def sync_from_universe(universe, folder):
    project=Path(__file__).resolve().parents[1]
    # Installation is explicit. Once enabled, universe builds retain these owners.
    if (project/'story/rpg/courier_owners.json').exists():
        generate(universe,folder,project,project/'results/courier_owners')


def refresh(project, folder, output, dry_run=False):
    """Reconnect freshly recorded shared speech without rebuilding the universe."""
    registry=json.loads((project/'story/rpg/courier_owners.json').read_text(encoding='utf-8'))
    files,report=plan(project,folder,registry,folder.data_path('MISSIONS/TrainCourier/catalog.ini').read_bytes())
    if not dry_run:
        folder.sync_courier_owners(files,output/'backups'/datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f'))
    output.mkdir(parents=True,exist_ok=True)
    (output/'coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return {'owners':len(report),'dry_run':dry_run}
