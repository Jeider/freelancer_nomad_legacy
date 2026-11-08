"""Parking UI assets exported after room generation; all DATA writes belong to DataFolder."""
import re

ICON = 'Interface/Baseside/parking_p.3db'
NAVBAR = 'Interface/Baseside/navbar.ini'


def plan(project, read):
    original = read(NAVBAR)
    pattern = rb'(?im)^IDS_HOTSPOT_SHIPPARK\s*=[^\r\n]*'
    replacement = b'IDS_HOTSPOT_SHIPPARK = Interface\\Baseside\\parking_p.3db'
    if len(re.findall(pattern, original)) != 1:
        raise ValueError('Expected exactly one parking NavBar mapping')
    navbar = re.sub(pattern, lambda _: replacement, original)
    return {NAVBAR: navbar, ICON: (project/'assets/parking/parking_p.3db').read_bytes()}
