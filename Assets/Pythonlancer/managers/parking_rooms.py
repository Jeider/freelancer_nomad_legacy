"""Ensure parking access in actual ship-selling rooms, including static interiors."""
from managers.parking_commandants import parse, one

# Authored interiors with a source ship market but no ship-sales room.
LANDING_ROOMS = {
    'om11_01_base': ('deck', 'universe/room/ku/outpost_pirate_deck.ini'),
    'sig42_01_base': ('planetscape', 'universe/systems_mod/sigma42/room/sig42_01_planetscape.ini'),
}
LANDING_PATHS = {path for _, path in LANDING_ROOMS.values()}


def ensure_parking_hotspot(content, declared_dealer=False):
    """Add only the missing service; retain original bytes, comments and newlines."""
    rows = parse(content)
    hotspots = [row for kind, row in rows if kind == 'hotspot']
    if not declared_dealer and not any(one(row, 'behavior').lower() == 'startshipdealer' for row in hotspots):
        return content
    parking = [row for row in hotspots if one(row, 'behavior').lower() == 'startshippark']
    if len(parking) > 1:
        raise ValueError('Duplicate parking services in a ship-selling room')
    if parking:
        return content
    if any(one(row, 'name').lower() == 'ids_hotspot_shippark' for row in hotspots):
        raise ValueError('Parking hotspot name is occupied by a different behavior')
    newline = b'\r\n' if b'\r\n' in content else b'\n'
    block = newline.join((b'[Hotspot]', b'name = IDS_HOTSPOT_SHIPPARK', b'behavior = StartShipPark', b''))
    separator = newline if content.endswith((b'\n', b'\r')) else newline + newline
    return content + separator + block


def plan_room_hotspots(bases, definitions, read):
    files, coverage = {}, []
    for base in bases:
        rooms = parse(read(definitions[base]))
        services = []
        for kind, room in rooms:
            if kind != 'room':
                continue
            path = one(room, 'file').replace('\\', '/')
            # Paths come from the base definition, not from assumptions about filenames.
            content = read(path)
            if not any(k == 'hotspot' and one(r, 'behavior').lower() == 'startshipdealer'
                       for k, r in parse(content)):
                continue
            patched = ensure_parking_hotspot(content)
            files[path] = patched
            services.append({'room': one(room, 'nickname'), 'file': path,
                             'added': patched != content})
        if not services:
            # Use the existing landing room for these two authored interiors.
            if base not in LANDING_ROOMS:
                raise ValueError('Source ShipDealer has no actual StartShipDealer service: ' + base)
            nickname, expected_path = LANDING_ROOMS[base]
            deck = next(r for k, r in rooms if k == 'room' and one(r, 'nickname').lower() == nickname)
            path = one(deck, 'file').replace('\\', '/')
            if path.lower() != expected_path:
                raise ValueError('Review changed landing room: ' + base)
            content = read(path)
            patched = ensure_parking_hotspot(content, declared_dealer=True)
            files[path] = patched
            services.append({'room': one(deck, 'nickname'), 'file': path, 'added': content != patched,
                             'source_declares_shipdealer': True, 'static_shipdealer_missing': True})
        coverage.append({'base': base, 'rooms': services})
    return files, coverage
