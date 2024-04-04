from templates.solar.hacker_panel import REL_FRONT, REL_TOP, REL_BOTTOM


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


class HackableBretoniaBattleship(HackableSolar):
    OFFSET = (-22, -23, -46.5)
    ARCHETYPE = 'suprise_br_battleship'
    ROTATE = (0, 94.5, 0)
    PANEL_RELATION = REL_TOP


class HackableLibertyDreadnought(HackableSolar):
    OFFSET = (0, 14, -120)
    ARCHETYPE = 'suprise_li_dreadnought'
    ROTATE = (0, 0, 0)
    PANEL_RELATION = REL_TOP


class HackableOsiris(HackableSolar):
    OFFSET = (-135, -10, -55)
    ARCHETYPE = 'suprise_or_osiris'
    ROTATE = (0, 75.5, 0)
    PANEL_RELATION = REL_TOP


class HackableLuxuryLiner(HackableSolar):
    OFFSET = (0, -35.7,  -130)
    ARCHETYPE = 'suprise_luxury_liner'
    ROTATE = (0, 0, 0)
    PANEL_RELATION = REL_BOTTOM


class HackablePrisonLiner(HackableSolar):
    OFFSET = (0, -24,  -122)
    ARCHETYPE = 'suprise_prison_liner'
    ROTATE = (0, 0, 0)
    PANEL_RELATION = REL_BOTTOM


class HackableFreeport7Dock(HackableSolar):
    OFFSET = (-20, 38, -20)
    ARCHETYPE = 'freeport7_dock'
    ROTATE = (0, 0, -10)
    PANEL_RELATION = REL_BOTTOM


class HackableFreeport7DockRot180(HackableSolar):
    OFFSET = (20, 38, 20)
    ARCHETYPE = 'freeport7_dock'
    ROTATE = (0, 180, 10)
    PANEL_RELATION = REL_BOTTOM
