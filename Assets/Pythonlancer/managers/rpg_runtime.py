"""Connect the authored rm0001 graph to its existing Bismarck contact."""
import datetime
import hashlib
import json

from files.rpg_runtime import dialog_ini, bind_contact, SESSION_THN
from files.rpg_recordings import non_data_path
from managers.rpg_scene import RpgSceneManager


def install_runtime(project, script, game_root, output, dry_run=False):
    if script.name == 'rm0002':
        from managers.rpg_parking import install_parking_runtime
        return install_parking_runtime(project, script, game_root, output, dry_run)
    if script.name != 'rm0001':
        raise ValueError('This contact binding is specific to rm0001')
    if (project/'story/rpg/courier_owners.json').exists():
        from managers.courier_owners import refresh
        from tools.data_folder import DataFolder
        return refresh(project, DataFolder(root=game_root or project.parent.parent), output, dry_run)
    scenes = RpgSceneManager(project, script, game_root)
    folder = scenes.folder
    # The user may temporarily remove voices while rerecording. Do not restore them.
    # Existing WAVs must still match the scene; missing ones use the client's text fallback.
    manifest = json.loads(folder.data_path('SCRIPTS/RPG/rm0001/en/manifest.json').read_text(encoding='utf-8'))
    rows = manifest['fragments']
    current = {r['id']: r for r in script.fragments}
    if (manifest.get('group') != script.name or len({r['id'] for r in rows}) != len(rows)
            or not {r['id'] for r in rows} <= current.keys()):
        raise ValueError('Scene catalog does not match rm0001')
    missing, voiced = [], set()
    for row in manifest.get('gestures', []):
        path = row['path']
        if hashlib.sha256(folder.data_path(path).read_bytes()).hexdigest() != row['sha256']:
            raise ValueError('Modified gesture THN: ' + path)
    for row in rows:
        path = f'SCRIPTS/RPG/rm0001/en/{row["id"]}.thn'
        if row['path'] != path or hashlib.sha256(folder.data_path(path).read_bytes()).hexdigest() != row['sha256']:
            raise ValueError('Modified THN: ' + path)
        audio = folder.data_path(row['audio'])
        if not audio.is_file():
            missing.append(row['audio'])
        elif hashlib.sha256(audio.read_bytes()).hexdigest() != row['audio_sha256']:
            raise ValueError('Regenerate THN for changed audio: ' + row['audio'])
        elif row.get('text') == current[row['id']]['en'] and row['role'] == current[row['id']]['role']:
            voiced.add(row['id'])
    layout = folder.data_path('SCRIPTS/BASES/Rh_01_Bar_hardpoint_01.thn').read_bytes()
    for marker in (b'Zs/NPC/mFloor2/01/PCU/Camera', b'Zs/NPC/mFloor2/01/ACU/Camera',
                   b'Zs/NPC/mFloor2/01/P/Stand'):
        if marker not in layout:
            raise ValueError('Missing Bismarck camera/placement: ' + marker.decode())
    files = {'RPG/rm0001_dialog.ini': dialog_ini(script, voiced).encode('utf-8'),
             'RPG/rh_biz_contact.ini': bind_contact(folder.data_path('RPG/rh_biz_contact.ini').read_bytes()),
             'SCRIPTS/RPG/conversation.thn': SESSION_THN.encode('utf-8')}
    output = non_data_path(output)
    report = {'group': script.name, 'dry_run': dry_run, 'missing_audio': missing,
              'pending_voice_fragments': sorted(current.keys() - voiced),
              'files': {path: hashlib.sha256(content).hexdigest() for path, content in files.items()}}
    if not dry_run:
        backup = output / 'backups' / datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        folder.sync_rpg_runtime(files, backup)
    output.mkdir(parents=True, exist_ok=True)
    (output / 'runtime_install.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    return report
