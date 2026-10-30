import re

def blocks(text):
    return re.split(r'(?m)(?=^\[[^\r\n]+\])', text)


def value(block, key):
    m = re.search(r'(?im)^\s*' + re.escape(key) + r'\s*=\s*([^;\r\n]+)', block)
    return m[1].strip() if m else ''


def insert(block, line):
    newline = '\r\n' if '\r\n' in block else '\n'
    key = line.split('=')[0].strip()
    if key == 'hp_type' and value(block, key):
        raise ValueError('Equipment already has hp_type: ' + value(block, 'nickname'))
    at = re.search(r'(?im)^nickname\s*=[^\r\n]*\r?\n', block)
    if not at: raise ValueError('Missing nickname')
    return block[:at.end()] + line + newline + block[at.end():]


def ships(text, report):
    result = []
    for b in blocks(text):
        if not b.lower().startswith('[ship]'):
            result.append(b); continue
        nick = value(b, 'nickname')
        levels = re.findall(r'(?im)^hp_type\s*=\s*hp_\w+_engine_special_(\d+)', b)
        if not levels:
            levels = re.findall(r'(?im)^hp_type\s*=\s*hp_(?:gun|\w+_shield)_special_(\d+)', b)
        tier = max(map(int, levels), default=10)
        newline = '\r\n' if '\r\n' in b else '\n'
        def thruster(m):
            hps = m[1].split(';')[0].strip()
            report['hulls'][nick] = dict(max_class=tier, hardpoints=[h.strip() for h in hps.split(',')])
            return newline.join(f'hp_type = hp_thruster_special_{i}, {hps}' for i in range(1, tier+1))
        b = re.sub(r'(?im)^hp_type\s*=\s*hp_thruster\s*,\s*([^\r\n]*)', thruster, b)
        if not re.search(r'(?im)^equipment_slot\s*=\s*HpHardware01\s*,', b):
            b = insert(b, 'equipment_slot = HpHardware01, hardware, 1')
        result.append(b)
    return ''.join(result)


def upgrade_ships(text):
    return ships(text, {'hulls': {}})
