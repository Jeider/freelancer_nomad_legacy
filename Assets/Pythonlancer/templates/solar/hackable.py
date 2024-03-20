from templates.solar.hacker_panel import REL_FRONT, REL_TOP


class HackableSolar(object):
    OFFSET = (0, 0, 0)
    ARCHETYPE = None
    ROTATE = (0, 0, 0)
    PANEL_RELATION = None


class HackableOutpost(HackableSolar):
    OFFSET = (40, 47.5,  0)
    ARCHETYPE = 'space_police01'
    ROTATE = (0, 0, 18.5)
    PANEL_RELATION = REL_TOP


class HackableOutpostRot90(HackableSolar):
    OFFSET = (0, 47.5,  40)
    ARCHETYPE = 'space_police01'
    ROTATE = (90, 108.5, 90)
    PANEL_RELATION = REL_TOP


class HackableRheinlandBattleship(HackableSolar):
    OFFSET = (-3, -20, -93.5)
    ARCHETYPE = 'suprise_rh_battleship'
    ROTATE = (0, -90, 0)
    PANEL_RELATION = REL_FRONT


class HackableKusariBattleship(HackableSolar):
    OFFSET = (0, 52, 110)
    ARCHETYPE = 'suprise_ku_battleship'
    ROTATE = (0, 0, 0)
    PANEL_RELATION = REL_TOP
