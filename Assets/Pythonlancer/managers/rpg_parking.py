"""Bind rm0002 to the existing Avalon parking seller, retaining local rights."""
import datetime
import hashlib
import json
import re

from files.rpg_recordings import non_data_path
from files.rpg_runtime import dialog_ini
from managers.rpg_scene import RpgSceneManager
from tools.ship_parking import sections, one, datafile


def bind_parking_contact(content, script):
    if script.name != 'rm0002' or script.data['parking'] != {
            'base': 'br_avl_01_base', 'seller': 'park_br_avl_01'}:
        raise ValueError('Expected the Avalon parking scenario')
    text = content.decode('utf-8-sig')
    if not re.search(r'(?im)^Location\s*=\s*br_avl_01_base,\s*Bar\s*$', text):
        raise ValueError('Wrong parking contact location')
    result, found = [], set()
    for chunk in re.split(r'(?m)(?=^\[)', text):
        header = chunk.splitlines()[0].strip().lower() if chunk else ''
        if header in ('[dialog]', '[dialognode]', '[dialogchoice]'):
            continue
        if header == '[characterencounter]':
            chunk = re.sub(r'(?im)^\s*(click_script|dialog)\s*=[^\r\n]*\r?\n', '', chunk)
            pos = chunk.index('\n') + 1
            chunk = chunk[:pos] + 'dialog = RPG\\rm0002_dialog.ini\n' + chunk[pos:]
            found.add('encounter')
        if header == '[npc]' and re.search(r'(?im)^nickname\s*=\s*park_br_avl_01\s*$', chunk):
            for key in ('head', 'body'):
                chunk, count = re.subn(r'(?im)^' + key + r'\s*=[^\r\n]*',
                                      key + ' = ' + script.data['appearance'][key], chunk)
                if count != 1:
                    raise ValueError('Missing/duplicate NPC ' + key)
            found.add('npc')
        result.append(chunk)
    if found != {'encounter', 'npc'}:
        raise ValueError('Missing Avalon contact or appearance')
    return ''.join(result).encode('utf-8')


def install_parking_runtime(project, script, game_root, output, dry_run=False):
    scenes = RpgSceneManager(project, script, game_root)
    folder, game = scenes.folder, scenes.folder.get_root()
    # Recompute using the same production compiler: both audio and THNs must be current.
    scene_files, catalogs = scenes.plan(('en',))
    for name, content in scene_files.items():
        if folder.data_path(name).read_bytes() != content:
            raise ValueError('Rebuild scenes before connecting rm0002: ' + name)
    if not folder.data_path('SCRIPTS/RPG/conversation.thn').is_file():
        raise ValueError('Install the shared RPG conversation session first')
    source = 'RPG/parking/br_avl_01_base.ini'
    rows = sections(folder.data_path(source))
    spot = next(one(row, 'spot') for kind, row in rows if kind == 'char')
    if not spot.endswith('/A/Stand'):
        raise ValueError('Parking officer needs a standing marker')
    room = folder.data_path('UNIVERSE/SYSTEMS_MOD/BR_AVALON/ROOM/br_avl_01_bar.ini')
    layout = b'\n'.join(datafile(game, path).read_bytes() for kind, row in sections(room)
                        if kind == 'room_info' for path in row.get('set_script', []))
    prefix = spot.rsplit('/A/', 1)[0].replace('Zg/', 'Zs/', 1)
    for marker in (spot, prefix + '/P/Stand', prefix + '/PCU/Camera', prefix + '/ACU/Camera'):
        if marker.encode() not in layout:
            raise ValueError('Missing Avalon placement/camera: ' + marker)
    if not any(kind == 'parkingbase' and one(row, 'base') == 'br_avl_01_base' and
               one(row, 'seller') == 'park_br_avl_01'
               for kind, row in sections(folder.data_path('RPG/ship_parking.ini'))):
        raise ValueError('Avalon parking seller is not registered')
    files = {source: bind_parking_contact(folder.data_path(source).read_bytes(), script),
             'RPG/rm0002_dialog.ini': dialog_ini(script).encode('utf-8')}
    output = non_data_path(output)
    report = {'group': script.name, 'language': 'en', 'dry_run': dry_run, 'spot': spot,
              'fragments': len(catalogs['en']['fragments']),
              'files': {name: hashlib.sha256(content).hexdigest() for name, content in files.items()}}
    if not dry_run:
        backup = output / 'backups' / datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        folder.sync_rpg_parking_runtime(files, backup)
        for name, content in files.items():
            assert folder.data_path(name).read_bytes() == content
    output.mkdir(parents=True, exist_ok=True)
    (output / 'runtime_install.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    return report
