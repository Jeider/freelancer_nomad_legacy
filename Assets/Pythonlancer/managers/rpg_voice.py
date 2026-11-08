"""Coordinate RPG recording preparation and the existing voice backend."""
import os
from pathlib import Path

from files.rpg_recordings import non_data_path, write_recordings
from story.rpg.script import RpgScript
from tools.voice_output import output_path


class RpgVoiceManager:
    def __init__(self, project_root, spec):
        self.root = Path(project_root).resolve()
        self.script = RpgScript.load(spec)

    def prepare(self, output):
        write_recordings(self.script, output)

    def voices(self, output, languages, vendor_actor=None, dry_run=False):
        vendor_actor = self.script.vendor_actor_name(vendor_actor)
        group = self.script.recording_group(vendor_actor)
        plan = {"group": self.script.name, "vendor_actor": vendor_actor,
                "player_actor": "Trent", "dry_run": dry_run, "languages": {}}
        for language in languages:
            folder = "AUDIO_CUTSCENE_RU" if language == "ru" else "AUDIO_CUTSCENE_EN"
            destination = non_data_path(self.root.parent / folder / self.script.name)
            plan["languages"][language] = [{
                "filename": str(output_path(destination / (sound.name + ".mp3"))),
                "actor": sound.line.actor.__name__,
                "text": sound.line.ru if language == "ru" else sound.line.en,
            } for sound in group.get_sounds()]
        write_recordings(self.script, output, plan)
        if not dry_run:
            # Check every required reference before generating any fragment.
            from settings import VOICE_BACKEND
            if VOICE_BACKEND == 'voicestudio':
                from tools.voicestudio import VoiceStudioClone
                missing = []
                for language in languages:
                    for actor in {sound.line.actor for sound in group.get_sounds()}:
                        try:
                            VoiceStudioClone.source_file(actor.__name__, language)
                        except Exception as error:
                            missing.append(str(error))
                if missing:
                    raise ValueError('Missing voice references; nothing generated:\n' + '\n'.join(missing))
            # Lazy import: prepare/dry-run never load or call voice services.
            from tools.audio_folder import AudioFolder
            previous = Path.cwd()
            try:
                os.chdir(self.root)  # AudioFolder/voice services use the project cwd.
                for language in languages:
                    AudioFolder.generate_cutscene_sounds(group, russian=language == "ru")
            finally:
                os.chdir(previous)
        return plan
