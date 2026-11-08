"""Output naming shared by voice generators and recording plans; no service imports."""
from pathlib import Path

from settings import VOICE_BACKEND


def output_path(destination):
    path = Path(destination)
    return path.with_suffix('.wav') if VOICE_BACKEND == 'voicestudio' else path
