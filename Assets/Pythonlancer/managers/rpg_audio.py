"""Install one explicitly selected base-dialogue group's PCM WAVs through DataFolder."""
import datetime
import hashlib
import io
import json
import re
from pathlib import Path
import wave

from files.rpg_audio import sound_bank, register_bank, audio_manifest
from files.rpg_recordings import non_data_path
from tools.data_folder import DataFolder


class RpgAudioManager:
    def __init__(self, project_root, script, game_root=None):
        self.project = Path(project_root).resolve()
        self.script = script
        self.game = Path(game_root).resolve() if game_root else self.project.parent.parent
        self.folder = DataFolder(root=self.game)

    def source(self, language, fragment):
        folder = 'AUDIO_CUTSCENE_RU' if language == 'ru' else 'AUDIO_CUTSCENE_EN'
        return self.project.parent / folder / self.script.name / (self.script.line_name(fragment) + '.wav')

    def plan(self, languages):
        group = self.script.name
        manifest_path = f'AUDIO/RPG/{group}.json'
        previous = self.folder.data_path(manifest_path)
        records = {}
        if previous.exists():
            old = json.loads(previous.read_text(encoding='utf-8'))
            if old.get('schema') != 1 or old.get('group') != group:
                raise ValueError('Unexpected existing RPG audio manifest')
            records = old['languages']
        files, missing = {}, []
        for language in languages:
            if language not in ('ru', 'en'):
                raise ValueError('Unknown recording language')
            records[language] = []
            for row in self.script.fragments:
                path = self.source(language, row)
                if not path.is_file():
                    missing.append(str(path))
                    continue
                content = path.read_bytes()
                try:
                    with wave.open(io.BytesIO(content), 'rb') as wav:
                        channels, width, rate, frames, codec, _ = wav.getparams()
                        raw = wav.readframes(frames)
                except (wave.Error, EOFError) as error:
                    raise ValueError(f'Expected PCM16 WAV: {path}') from error
                if width != 2 or codec != 'NONE' or not frames or len(raw) != frames * channels * width:
                    raise ValueError(f'Empty, truncated or non-PCM16 WAV: {path}')
                bank = 'MOD' if language == 'ru' else 'MOD_ENG'
                relative = f'AUDIO/{bank}/RPG/{group}/{path.name}'
                files[relative] = content
                records[language].append({'fragment': row['id'], 'file': relative,
                    'nickname': f'DX_{self.script.line_name(row)}_{language}',
                    'sha256': hashlib.sha256(content).hexdigest(), 'duration_seconds': frames / rate,
                    'sample_rate': rate, 'channels': channels})
        if missing:
            raise FileNotFoundError('Record all selected fragments before installation:\n' + '\n'.join(missing))
        # Only emit records for this group, even when retaining the other language.
        for language, rows in records.items():
            if language not in ('ru', 'en'):
                raise ValueError('Unexpected language in installed manifest')
            bank = 'MOD' if language == 'ru' else 'MOD_ENG'
            for row in rows:
                prefix = f'AUDIO/{bank}/RPG/{group}/'
                if not row['file'].startswith(prefix) or Path(row['file']).name != row['file'][len(prefix):]:
                    raise ValueError('Installed manifest escaped the selected group')
                name = Path(row['file']).stem
                if not re.fullmatch(group + r'_frag[0-9]{4}_l001_(vendor|player)', name) or row['nickname'] != f'DX_{name}_{language}':
                    raise ValueError('Invalid recording identity in installed manifest')
                if language not in languages:
                    installed = self.folder.data_path(row['file'])
                    if not installed.is_file() or hashlib.sha256(installed.read_bytes()).hexdigest() != row['sha256']:
                        raise ValueError(f'Previously installed audio changed: {installed}')
        files[f'AUDIO/RPG/{group}_sounds.ini'] = sound_bank(records).encode('utf-8')
        files[manifest_path] = audio_manifest(group, records).encode('utf-8')
        configs = {}
        for name in ('freelancer.ini', 'freelan_en_port.ini'):
            path = self.folder.rpg_bin_path(name)
            configs[name] = register_bank(path.read_bytes(), group)
        return files, configs, records

    def install(self, languages, output, dry_run=False):
        output = non_data_path(output)
        files, configs, records = self.plan(languages)
        report = {'group': self.script.name, 'languages': list(languages), 'game': str(self.game),
                  'dry_run': dry_run, 'files': sorted(files), 'configurations': sorted(configs),
                  'recordings': sum(len(records[lang]) for lang in languages)}
        if not dry_run:
            backup = output / 'backups' / datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
            self.folder.sync_rpg_audio(self.script.name, files, configs, backup)
            report['backup'] = str(backup)
        output.mkdir(parents=True, exist_ok=True)
        (output / 'audio_install.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
        return report
