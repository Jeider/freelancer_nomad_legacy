import io
import wave

from pydub import AudioSegment


def _as_s16(samples, width):
    if width == 2:
        return samples
    if width == 1:
        return b''.join(int((b - 128) << 8).to_bytes(2, 'little', signed=True) for b in samples)
    if width == 3:
        return b''.join(samples[i + 1:i + 3] for i in range(0, len(samples) - 2, 3))
    if width == 4:
        return b''.join(samples[i + 2:i + 4] for i in range(0, len(samples) - 3, 4))
    raise ValueError('unsupported sample width %s' % width)


def _pack_s24(samples16):
    # pydub's sample_width 3 is stored as 4 bytes. Write real 3-byte samples.
    return b''.join(b'\x00' + samples16[i:i + 2] for i in range(0, len(samples16) - 1, 2))


def goldwave_wav(path):
    # Plain 48 kHz resample, then a classic 24-bit header. Not part of VoiceStudio.
    path = str(path)
    with wave.open(path, 'rb') as src:
        channels, width, rate, frames, compression, _ = src.getparams()
        samples = src.readframes(frames)
    if compression != 'NONE' or not frames:
        raise ValueError('post-process expects an uncompressed WAV')
    samples = _as_s16(samples, width)
    segment = AudioSegment(data=samples, sample_width=2, frame_rate=rate, channels=channels)
    segment = segment.set_channels(1).set_frame_rate(48000)
    packed = _pack_s24(segment.raw_data)
    result = io.BytesIO()
    with wave.open(result, 'wb') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(3)
        wav.setframerate(48000)
        wav.writeframes(packed)
    with open(path, 'wb') as handle:
        handle.write(result.getvalue())
    return path


def repair_mislabeled(path):
    # Files written from pydub's 4-byte "24-bit" buffer with a 3-byte header.
    path = str(path)
    with wave.open(path, 'rb') as src:
        channels, width, rate, frames, compression, _ = src.getparams()
        samples = src.readframes(frames)
    if compression != 'NONE' or width != 3 or channels != 1 or rate != 48000:
        return False
    usable = len(samples) - (len(samples) % 4)
    zeros = sum(1 for i in range(0, min(usable, 4000), 4) if samples[i:i + 2] == b'\x00\x00')
    if zeros < 800:
        return False
    packed = b''.join(b'\x00' + samples[i + 2:i + 4] for i in range(0, usable, 4))
    result = io.BytesIO()
    with wave.open(result, 'wb') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(3)
        wav.setframerate(48000)
        wav.writeframes(packed)
    with open(path, 'wb') as handle:
        handle.write(result.getvalue())
    return True
