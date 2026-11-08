"""Generate local parking managers from installed base rooms, without changing the game.

Standalone: can also run from Pythonlancer/tools/ship_parking.py.
"""
from pathlib import Path
import argparse
import json
import re
import sys

NAME_ID = 238390


def data_folder_type(game):
    """Use Pythonlancer's single DATA writer, including when run from this repo."""
    pythonlancer = game / 'Assets/Pythonlancer'
    if str(pythonlancer) not in sys.path:
        sys.path.insert(0, str(pythonlancer))
    from tools.data_folder import DataFolder
    return DataFolder


def sections(path):
    data = path.read_bytes()
    try:
        text = data.decode('utf-8-sig')
    except UnicodeDecodeError:
        text = data.decode('cp1251')
    result = []
    for line in text.splitlines():
        line = line.split(';', 1)[0].strip()
        if line.startswith('[') and line.endswith(']'):
            result.append((line[1:-1].lower(), {}))
        elif '=' in line and result:
            key, value = line.split('=', 1)
            result[-1][1].setdefault(key.strip().lower(), []).append(value.strip())
    return result


def one(section, key, default=''):
    return section.get(key, [default])[-1]


def datafile(game, relative):
    root = (game / 'DATA').resolve()
    path = (root / relative.replace('\\', '/')).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Path outside DATA: ' + relative)
    return path


def dialogue(base, seller):
    from files.rpg_reputation import parking_denial_ini
    text = f'[Dialog]\nnickname = {seller}_dialog\nstart = parking_start\nparking_base = {base}\nparking_seller = {seller}\n'
    nodes = {
        'parking_start': ('Стоянка: {base}. Куплено мест: {owned} из {maximum}. Занято: {used}. Цена места: {price} кредитов.',
                          'Parking: {base}. Owned: {owned} of {maximum}. Occupied: {used}. A slot costs {price} credits.'),
        'parking_confirm': ('Купить одно постоянное место на базе «{base}» за {price} кредитов?',
                            'Buy one permanent parking slot at {base} for {price} credits?'),
        'parking_success': ('Место оплачено. Теперь у вас {owned} из {maximum} мест на этой базе.',
                            'Slot purchased. You now own {owned} of {maximum} slots at this base.'),
        'parking_no_money': ('Недостаточно кредитов. Покупка не состоялась.', 'Not enough credits. No purchase was made.'),
        'parking_maximum': ('Вы уже приобрели максимальное число мест на этой базе.', 'You already own the maximum number of slots at this base.'),
        'parking_error': ('Покупка не состоялась. Уточните условия ещё раз.', 'No purchase was made. Please request a new quote.'),
        'parking_help': ('Место действует только на этой базе и остаётся вашим после вывоза корабля. Активный корабль места не занимает. На полной стоянке можно обменять корабли.',
                         'Slots belong to this base and remain yours after collecting a ship. Your active ship uses no slot. You can switch ships even when parking is full.'),
    }
    for name, (ru, en) in nodes.items():
        text += f'\n[DialogNode]\nnickname = {name}\ntext_ru = {ru}\ntext_en = {en}\n'

    def choice(node, ru, en, target='', action=''):
        return (f'\n[DialogChoice]\nnode = {node}\ntext_ru = {ru}\ntext_en = {en}\n' +
                (f'goto = {target}\n' if target else '') + (f'action = {action}\n' if action else ''))
    text += choice('parking_start', 'Купить место', 'Buy a slot', 'parking_confirm', 'quote_parking')
    text += choice('parking_start', 'Как работает стоянка?', 'How does parking work?', 'parking_help')
    text += choice('parking_start', 'До встречи', 'Goodbye', action='close')
    text += choice('parking_confirm', 'Подтверждаю покупку', 'Confirm purchase', action='buy_parking')
    text += choice('parking_confirm', 'Отмена', 'Cancel', 'parking_start')
    for name in nodes:
        if name in ('parking_start', 'parking_confirm'):
            continue
        text += choice(name, 'Назад', 'Back', 'parking_start')
        text += choice(name, 'До встречи', 'Goodbye', action='close')
    return parking_denial_ini(text)


def generate(game, output, *, folder=None):
    game, output = game.resolve(), output.resolve()
    if output.is_relative_to((game / 'DATA').resolve()):
        raise ValueError('Output must be a game/staging root, not a directory inside game DATA')
    if folder is None:
        folder = data_folder_type(game)(root=output)
    if folder.get_root().resolve() != output:
        raise ValueError('DataFolder destination must match the output root')
    reserved, factions = {}, {}
    base = room = ''
    for kind, row in sections(game / 'DATA/MISSIONS/mbases.ini'):
        if kind == 'mbase':
            base, room = one(row, 'nickname').lower(), ''
            factions[base] = one(row, 'local_faction', 'fc_uk_grp')
        elif kind == 'mroom':
            room = one(row, 'nickname').lower()
            for fixture in row.get('fixture', []):
                reserved.setdefault((base, room), set()).add(fixture.split(',')[1].strip().lower())
    catalog = game / 'DATA/RPG/contacts.ini'
    if catalog.exists():
        for kind, row in sections(catalog):
            if kind != 'rpgcontact' or one(row, 'enabled').lower() not in ('true', '1'):
                continue
            rtc = sections(datafile(game, one(row, 'rtc')))
            encounter = next(r for k, r in rtc if k == 'characterencounter')
            base, room = [s.strip().lower() for s in one(encounter, 'location').split(',')]
            for k, r in rtc:
                if k == 'reserve':
                    reserved.setdefault((base, room), set()).update(s.lower() for s in r.get('spot', []))

    files = {}
    config_path = game / 'DATA/RPG/ship_parking.ini'
    config = config_path.read_text(encoding='utf-8-sig') if config_path.exists() else (
        '; Permanent parking rights per character and base. Restart after editing.\n'
        '[ParkingDefaults]\nmax_slots = 3\ninitial_slots = 0\nslot_price = 20000\n')
    overrides = {one(r, 'base').lower(): r for k, r in sections(config_path) if k == 'parkingbase'} if config_path.exists() else {}
    entries, skipped = [], []
    seen = {}
    catalog_text = '; Generated parking managers; independent of story contacts.\n'
    for kind, row in sections(game / 'DATA/UNIVERSE/universe.ini'):
        if kind != 'base':
            continue
        base = one(row, 'nickname').lower()
        definition_path = one(row, 'file').lower()
        if base in seen:
            # Universe::GBases.insert keeps the first record for a duplicate nickname.
            continue
        seen[base] = definition_path
        base_file = datafile(game, one(row, 'file'))
        if not base_file.is_file():
            skipped.append(dict(base=base, reason='Missing base definition: ' + one(row, 'file')))
            continue
        rooms = [r for k, r in sections(base_file) if k == 'room' and one(r, 'nickname').lower() == 'bar']
        if not rooms:
            skipped.append(dict(base=base, reason='No bar'))
            continue
        room = one(rooms[0], 'nickname')
        definition = sections(datafile(game, one(rooms[0], 'file')))
        layouts = [datafile(game, p) for k, r in definition if k == 'room_info' for p in r.get('set_script', [])]
        layout = b'\n'.join(p.read_bytes() for p in layouts)
        candidates = sorted(set(re.findall(rb'Zg/NPC/m[A-Za-z0-9_/]+/A/(?:Stand|SitLow)', layout)),
                            key=lambda p: (not p.endswith(b'/Stand'), p))
        spot = None
        for candidate in candidates:
            prefix = candidate.decode().rsplit('/A/', 1)[0].replace('Zg/', 'Zs/', 1)
            if (candidate.decode().lower() not in reserved.get((base, room.lower()), set()) and
                (prefix + '/P/Stand').encode() in layout and (prefix + '/PCU/Camera').encode() in layout):
                spot = candidate.decode()
                break
        if spot is None:
            skipped.append(dict(base=base, reason='No free NPC marker with player/camera markers'))
            continue
        seller = 'park_' + base.removesuffix('_base')
        assert len(seller) < 32
        if base in overrides and one(overrides[base], 'seller') != seller:
            skipped.append(dict(base=base, reason='Custom seller configured; preserve authored contact'))
            continue
        path = f'RPG/parking/{base}.ini'
        fidget = 'fidget_stand_male_01.thn' if spot.endswith('/Stand') else 'fidget_sit_male_01.thn'
        catalog_text += f'\n[RpgContact]\nnickname = {seller}\nenabled = true\nbase = {base}\nrtc = {path.replace("/", chr(92))}\n'
        if base not in overrides:
            config += f'\n[ParkingBase]\nbase = {base}\nseller = {seller}\n'
        files['DATA/' + path] = f'''[CharacterEncounter]
Location = {base}, {room}
choices = true

[Reserve]
spot = {spot}

[Char]
npc = {seller}
actor = {seller}
spot = {spot}
fidget = scripts\\extras\\{fidget}

[NPC]
nickname = {seller}
body = pl_male1_journeyman_body
head = br_brighton_head
lefthand = benchmark_male_hand_left
righthand = benchmark_male_hand_right
affiliation = {factions.get(base, 'fc_uk_grp')}
voice = rvp101
individual_name = {NAME_ID}

''' + dialogue(base, seller)
        # Authored voiced parking contacts own their costume and external graph.
        # A world/parking regeneration must retain them and their reserved marker.
        existing = datafile(game, path)
        if existing.is_file() and any(k == 'characterencounter' and one(r, 'dialog')
                                      for k, r in sections(existing)):
            authored = sections(existing)
            actor = next((r for k, r in authored if k == 'char' and one(r, 'npc') == seller), None)
            if actor is None:
                raise ValueError('Authored parking contact has no matching seller: ' + path)
            spot = one(actor, 'spot')
            files['DATA/' + path] = existing.read_bytes()
        entries.append(dict(base=base, seller=seller, room=room, spot=spot))
    from files.rpg_reputation import parking_rules
    files['DATA/RPG/ship_parking.ini'] = parking_rules(config, factions)
    files['DATA/RPG/parking_contacts.ini'] = catalog_text
    assert (game / 'DATA/RPG/dialogue_choice.thn').is_file(), 'Install RPG dialog scene first'
    folder.sync_ship_parking({relative.removeprefix('DATA/'): text for relative, text in files.items()})
    report = dict(managers=entries, skipped=skipped)
    (output / 'parking_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Generated {len(entries)} parking managers; {len(skipped)} bases skipped. Report: {output / "parking_report.json"}')
    return files, report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game-root', type=Path, default=Path('D:/Games/FL_MOD'))
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    generate(args.game_root.resolve(), args.output.resolve())
