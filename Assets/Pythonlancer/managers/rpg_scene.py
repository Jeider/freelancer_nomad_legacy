"""Build localized THNs from installed, verified PCM audio; publish via DataFolder."""
import datetime
import hashlib
import io
import json
from pathlib import Path
import wave
from xml.sax.saxutils import escape

from jinja2 import FileSystemLoader
from files.rpg_recordings import non_data_path
from managers.jinja_manager import JinjaTemplateManager
from story.rpg.scene import FragmentScene, GestureScene, CAMERAS, GESTURE_COUNT, GESTURE_SEQUENCE
from tools.data_folder import DataFolder


class RpgSceneManager:
    def __init__(self, project_root, script, game_root=None):
        self.project = Path(project_root).resolve()
        self.script = script
        self.folder = DataFolder(root=game_root or self.project.parent.parent)
        self.templates = JinjaTemplateManager()
        self.templates.environment.loader = FileSystemLoader(self.project / 'templates')

    def plan(self, languages):
        script = self.script
        manifest = json.loads(self.folder.data_path(f'AUDIO/RPG/{script.name}.json').read_text(encoding='utf-8'))
        if manifest.get('schema') != 1 or manifest.get('group') != script.name:
            raise ValueError('Unexpected installed audio manifest')
        bank = self.folder.data_path(f'AUDIO/RPG/{script.name}_sounds.ini').read_text(encoding='utf-8')
        sounds = script.recording_group().get_sounds()
        inputs = []
        # Validate the whole requested batch before rendering or writing any THN.
        for language in languages:
            if language not in ('ru', 'en') or language not in manifest['languages']:
                raise ValueError(f'Install audio for language {language} first')
            rows = manifest['languages'][language]
            by_id = {row['fragment']: row for row in rows}
            if len(by_id) != len(rows) or set(by_id) != {row['id'] for row in script.fragments}:
                raise ValueError('Audio manifest does not match the scenario fragments')
            audio_root = 'MOD' if language == 'ru' else 'MOD_ENG'
            for fragment, sound in zip(script.fragments, sounds):
                row = by_id[fragment['id']]
                expected_file = f'AUDIO/{audio_root}/RPG/{script.name}/{script.line_name(fragment)}.wav'
                nickname = f'DX_{script.line_name(fragment)}_{language}'
                if row['file'] != expected_file or row['nickname'] != nickname:
                    raise ValueError('Audio manifest identity mismatch')
                if f'nickname = {nickname}\n' not in bank or f'file = {expected_file.replace(chr(47), chr(92))}\n' not in bank:
                    raise ValueError('Audio bank is missing the installed recording')
                content = self.folder.data_path(expected_file).read_bytes()
                if hashlib.sha256(content).hexdigest() != row['sha256']:
                    raise ValueError('Installed WAV changed; reinstall audio first: ' + expected_file)
                with wave.open(io.BytesIO(content), 'rb') as wav:
                    frames, rate = wav.getnframes(), wav.getframerate()
                    if (wav.getsampwidth() != 2 or wav.getcomptype() != 'NONE' or frames <= 0 or
                            len(wav.readframes(frames)) != frames * 2 * wav.getnchannels()):
                        raise ValueError('Expected complete PCM16 recording: ' + expected_file)
                    seconds = frames / rate
                inputs.append((language, fragment, sound, row, seconds))
        files, catalogs = {}, {}
        for language, fragment, sound, audio, seconds in inputs:
            prefix = f'SCRIPTS/RPG/{script.name}/{language}'
            scene = FragmentScene(self.templates, script, fragment, sound, language, seconds, audio['nickname'])
            path = f'{prefix}/{fragment["id"]}.thn'
            content = scene.get_content().encode('utf-8')
            files[path] = content
            catalog = catalogs.setdefault(language, {
                'schema': 1, 'group': script.name, 'language': language,
                'runtime_connected': False,
                'contract': {'actor_binding': script.data['binding'], 'bind_mode': 2,
                             'require_existing_actors': True, 'session_cameras': CAMERAS,
                             'position_actors_once': True, 'skip': 'current_fragment_only'},
                'dialogue': script.data, 'fragments': []})
            catalog['fragments'].append({
                'id': fragment['id'], 'role': fragment['role'], 'pool': fragment['pool'],
                'path': path, 'sha256': hashlib.sha256(content).hexdigest(),
                'audio': audio['file'], 'audio_sha256': audio['sha256'], 'sound': audio['nickname'],
                'speech_seconds': seconds, 'scene_seconds': scene.duration,
                'facial_timing': 'Character.facial(auto_lip=True)',
                'text': fragment[language]})
        gestures = []
        role_inputs = {row[1]['role']: row for row in inputs}
        for role, (language, fragment, sound, audio, seconds) in role_inputs.items():
            for step in range(GESTURE_COUNT):
                scene = GestureScene(self.templates, script, fragment, sound, language, seconds,
                                     audio['nickname'], step)
                path = f'SCRIPTS/RPG/{script.name}/gestures/{role}_{step + 1:02d}.thn'
                content = scene.get_content().encode('utf-8')
                files[path] = content
                gestures.append({'role': role, 'step': step, 'path': path, 'duration': scene.duration,
                                 'sha256': hashlib.sha256(content).hexdigest()})
        for language, catalog in catalogs.items():
            catalog['gestures'] = gestures
            catalog['gesture_sequence'] = GESTURE_SEQUENCE
            prefix = f'SCRIPTS/RPG/{script.name}/{language}'
            files[f'{prefix}/manifest.json'] = (json.dumps(catalog, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
            subtitles = ['<?xml version="1.0" encoding="utf-8"?>', '<Subtitles>']
            for row in catalog['fragments']:
                audio_file = row['audio'].removeprefix('AUDIO/').replace('/', '\\')
                subtitles.append(f'<Static AudioFile="{audio_file}" TextArea="Cinematic">{escape(row["text"])}</Static>')
            subtitles.append('</Subtitles>')
            files[f'{prefix}/subtitles.xml'] = ('\n'.join(subtitles) + '\n').encode('utf-8')
        return files, catalogs

    def build(self, languages, output, dry_run=False):
        output = non_data_path(output)
        files, catalogs = self.plan(languages)
        if not dry_run:
            backup = output / 'backups' / datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
            self.folder.sync_rpg_scenes(self.script.name, files, backup)
        report = {'group': self.script.name, 'dry_run': dry_run, 'runtime_connected': False,
                  'files': sorted(files), 'fragments': sum(len(c['fragments']) for c in catalogs.values())}
        output.mkdir(parents=True, exist_ok=True)
        (output / 'scene_build.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
        return report
