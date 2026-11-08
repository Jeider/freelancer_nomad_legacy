"""RPG recording model: stable fragment IDs and native Pythonlancer sounds.

No StoryMission registration, scene construction, or filesystem writes.
"""
import json
from pathlib import Path
import re


class RpgScript:
    def __init__(self, data):
        self.data = data
        self.name = data["id"]
        self.fragments = data["fragments"]
        if not re.fullmatch(r"rm[0-9]{4}", self.name):
            raise ValueError("Expected rmNNNN group ID")
        seen, pools = set(), {}
        for row in self.fragments:
            name = row["id"]
            if not re.fullmatch(self.name + r"_frag[0-9]{4}", name) or name in seen:
                raise ValueError(f"Invalid or duplicate fragment: {name}")
            seen.add(name)
            if row["role"] not in ("player", "vendor"):
                raise ValueError(f"Unknown actor role in {name}")
            if not all(isinstance(row.get(lang), str) and row[lang].strip() for lang in ("ru", "en")):
                raise ValueError(f"Missing RU/EN text in {name}")
            pools.setdefault(row["pool"], set()).add(row["role"])
        if data["start"] not in data["nodes"] or data["rules"]["first_greeting"] not in seen:
            raise ValueError("Invalid start/greeting")
        for name, node in data["nodes"].items():
            if pools.get(node["pool"]) != {"vendor"}:
                raise ValueError(f"Invalid vendor pool in {name}")
            if not node.get("terminal") and node.get("choices") not in data["choice_sets"]:
                raise ValueError(f"Missing choices in {name}")
        for name, choices in data["choice_sets"].items():
            if not 1 <= len(choices) <= 4 or len(set(choices)) != len(choices):
                raise ValueError(f"Invalid choice count in {name}")
            if any(key not in data["choices"] for key in choices):
                raise ValueError(f"Unknown choice in {name}")
        for name, choice in data["choices"].items():
            if pools.get(choice["pool"]) != {"player"}:
                raise ValueError(f"Choice {name} requires a spoken player fragment")
            targets = list(choice.get("outcomes", {}).values())
            if "goto" in choice:
                targets.append(choice["goto"])
            if not targets or any(target not in data["nodes"] for target in targets):
                raise ValueError(f"Invalid transitions in {name}")

    @classmethod
    def load(cls, path):
        return cls(json.loads(Path(path).read_text(encoding="utf-8")))

    @staticmethod
    def line_name(fragment):
        return f'{fragment["id"]}_l001_{fragment["role"]}'

    def vendor_actor_name(self, override=None):
        return override or self.data.get('casting', {}).get('vendor', 'RpgTradeDirector')

    def recording_group(self, vendor_actor=None):
        # Use the same VoiceLine/CutsceneSound contract as mission cutscenes.
        from audio.sound import VoiceLine, CutsceneSound
        from story import actors
        from story.rpg import actors as rpg_actors
        vendor_actor = self.vendor_actor_name(vendor_actor)
        vendor = getattr(rpg_actors, vendor_actor, None) or getattr(actors, vendor_actor, None)
        if not isinstance(vendor, type) or not issubclass(vendor, actors.Actor) or not vendor.is_male():
            raise ValueError(f"Expected a male actor class from story/actors.py: {vendor_actor}")
        return RecordingGroup(self.name, [CutsceneSound(
            line=VoiceLine(1, actors.Trent if row["role"] == "player" else vendor,
                           ru=row["ru"], en=row["en"]),
            name=self.line_name(row), mission_segment=self)
            for row in self.fragments])

    def get_destination(self, suffix=""):
        return f"audio\\MOD{suffix}\\RPG\\{self.name}"

    def get_short_destination(self, suffix=""):
        return f"MOD{suffix}\\RPG\\{self.name}"

    def get_subfolder(self):
        return self.name


class RecordingGroup:
    """AudioFolder-compatible group; all fragments share one folder per language."""
    def __init__(self, name, sounds):
        self.name, self.sounds = name, sounds

    def get_cutscene_folder(self):
        return self.name

    def get_sounds(self):
        return self.sounds
