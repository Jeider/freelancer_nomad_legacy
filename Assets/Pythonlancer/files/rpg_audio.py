"""Pure renderers for one RPG group's sound registration and launch configuration."""
import json


def sound_bank(records):
    sections = []
    for language in sorted(records):
        for row in records[language]:
            path = row['file'].replace('/', '\\')
            sections.append(f'[Sound]\nnickname = {row["nickname"]}\ntype = voice\n'
                            f'attenuation = 0\nfile = {path}\nis_2d = true\n')
    return '\n'.join(sections)


def register_bank(content, group):
    """Insert only this bank into [Data], preserving encoding and other bytes."""
    bank = f'audio\\RPG\\{group}_sounds.ini'.encode('ascii')
    newline = b'\r\n' if b'\r\n' in content else b'\n'
    lines = content.splitlines(keepends=True)
    section = None
    start = None
    found = 0
    for index, line in enumerate(lines):
        stripped = line.split(b';', 1)[0].strip().lower()
        if stripped.startswith(b'[') and stripped.endswith(b']'):
            section = stripped
            if section == b'[data]':
                if start is not None:
                    raise ValueError('Duplicate [Data] section')
                start = index
        elif section == b'[data]' and b'=' in stripped:
            key, value = stripped.split(b'=', 1)
            if key.strip() == b'sounds' and value.strip().replace(b'/', b'\\') == bank.lower():
                found += 1
    if start is None or found > 1:
        raise ValueError('Missing [Data] section or duplicate RPG bank registration')
    if found:
        return content
    if not lines[start].endswith((b'\r', b'\n')):
        lines[start] += newline
    lines.insert(start + 1, b'      sounds = ' + bank + newline)
    return b''.join(lines)


def audio_manifest(group, records):
    return json.dumps({'schema': 1, 'group': group, 'languages': records}, ensure_ascii=False, indent=2) + '\n'
