"""Rules for parsing old-format Thorn cutscenes.

Facial clip names are dumped from DATA/CHARACTERS/ANIMATIONS/facial*.anm
into story/cutscenes/db/facial_anims.json. Body motions stay active.
When a scene switches to auto facial, old Facial events are still parsed
but emitted commented, so they do not fight Character.facial(auto_lip=True).

Phrases that must not use auto lipsync keep a hand-authored track in
story/cutscenes/db/audio_meta.json. Record or replace that track with:

    python single.py meta

Existing Facial events can be cached into the same JSON through
cache_lipsync().
"""
import json
import pathlib
import re

FACIAL_FILES = {
    "trent": "facialtrent.anm",
    "male": "facialmale.anm",
    "female": "facialfemale.anm",
    "juni": "facialjuni.anm",
}

_DB = pathlib.Path(__file__).resolve().parent / "db" / "facial_anims.json"
_NAMES = None


def facial_names():
    global _NAMES
    if _NAMES is None:
        dumped = json.loads(_DB.read_text(encoding="utf-8"))
        _NAMES = {name for clips in dumped.values() for name in clips}
    return _NAMES


def is_facial(animation):
    name = animation.strip().strip("'\"")
    if name in facial_names():
        return True
    low = name.lower()
    return low.startswith("sc_dx_") or "head_" in low or low.startswith("sc_fmhead") or low.startswith("sc_mlhead") or low.startswith("sc_adhead")


def motion_line(actor, animation, start, duration, auto_facial=True, **kwargs):
    """Python scene line. Facial is parsed, then commented when auto facial is on."""
    extra = ""
    if kwargs:
        extra = ", " + ", ".join(f"{key}={value}" for key, value in kwargs.items())
    line = f"self._m({actor}, {animation!r}, {start}, {duration}{extra})"
    if auto_facial and is_facial(animation):
        return f"# {line}  # old Facial; auto facial owns the face"
    return line


def facial_props(animation, duration=10, start_time=0, time_scale=1, trans_time=0.25, weight=1, heading=-1):
    parts = [f'animation="{animation}"']
    if start_time:
        parts.append(f"start_time={start_time}")
    parts.append(f"duration={duration}")
    parts.append(f"time_scale={time_scale}")
    parts.append(f"trans_time={trans_time}")
    parts.append(f"weight={weight}")
    parts.append(f"heading={heading}")
    return "{%s}" % ", ".join(parts)


def cache_lipsync(nickname, events):
    """Store parsed Facial events in the lipsync database used without auto lipsync."""
    from story.cutscenes.meta import MetaDatabase
    meta = []
    for event in events:
        meta.append({
            "delay": float(event.get("delay", 0)),
            "props": event.get("props") or facial_props(
                event["animation"],
                duration=event.get("duration", 10),
                start_time=event.get("start_time", 0),
                time_scale=event.get("time_scale", 1),
            ),
        })
    MetaDatabase().set_meta(nickname, meta)
    return meta


_EVENT = re.compile(
    r"\{\s*([0-9.]+)\s*,\s*START_MOTION\s*,\s*\{[^}]*\}\s*,\s*\{([^}]+)\}\s*\}",
    re.S,
)


def parse_old_motions(text):
    events = []
    for delay, props in _EVENT.findall(text):
        anim = re.search(r'animation\s*=\s*"([^"]+)"', props)
        if not anim:
            continue
        events.append({
            "delay": float(delay),
            "animation": anim.group(1),
            "props": "{" + " ".join(props.split()) + "}",
            "facial": is_facial(anim.group(1)),
        })
    return events
