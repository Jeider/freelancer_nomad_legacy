from world.equipment import Equipment as eq

class NPC(object):
    D1 = 1
    D2 = 2
    D3 = 3
    D4 = 4
    D5 = 5
    D6 = 6
    D7 = 7
    D8 = 8
    D9 = 9
    D10 = 10
    D11 = 11
    D12 = 12
    D13 = 13
    D14 = 14
    D15 = 15
    D16 = 16
    D17 = 17
    D18 = 18
    D19 = 19

    LEVELS = [
        D1, D2, D3, D4,
        D5, D6, D7, D8,
        D9, D10, D11, D12,
        D13, D14, D15, D16,
        D17, D18, D19
    ]

    SHIP1_LEVELS = [
        D1, D2, D3, D4,
        D5, D6, D7, D8,
        D9, D10, D11, D12,
        # D13, D14, D15, D16,
        # D17, D18, D19
    ]

    SHIP2_LEVELS = [
        # D1, D2, D3, D4,
        D5, D6, D7, D8,
        D9, D10, D11, D12,
        D13, D14, D15, D16,
        D17, D18, D19
    ]

    SHIP3_LEVELS = [
        # D1, D2, D3, D4,
        # D5, D6, D7, D8,
        D9, D10, D11, D12,
        D13, D14, D15, D16,
        D17, D18, D19
    ]

    WEAPON_1 = 'weapon1'
    WEAPON_2 = 'weapon2'
    WEAPON_3 = 'weapon3'
    WEAPON_4 = 'weapon4'
    WEAPON_5 = 'weapon5'
    WEAPON_6 = 'weapon6'
    AFTERBURN_1 = 'afterburn1'
    AFTERBURN_2 = 'afterburn2'
    TORPEDO = 'torpedo'
    TORPEDO_AMMO = 'torpedo_ammo'
    CM = 'cm'
    CM_AMMO = 'cm_ammo'
    MINE = 'mine'
    MINE_AMMO = 'mine_ammo'
    ENGINE = 'engine'
    POWER = 'power'
    SHIELD = 'shield'

    EQUIP_COLUMNS = [
        ENGINE,
        POWER,
        SHIELD,
        WEAPON_1,
        WEAPON_2,
        WEAPON_3,
        WEAPON_4,
        WEAPON_5,
        WEAPON_6,
        AFTERBURN_1,
        AFTERBURN_2,
        TORPEDO,
        CM,
        MINE,
        TORPEDO_AMMO,
        CM_AMMO,
        MINE_AMMO,
    ]

    EQUIPMENT_MAP = [
        D1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        D2: [2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0],
        D3: [2, 2, 2, 3, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1],
        D4: [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2],
        D5: [3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 2, 1, 1, 3, 1, 1, 2],
        D6: [3, 3, 3, 4, 3, 3, 3, 3, 2, 3, 3, 1, 1, 3, 2, 1, 2],
        D7: [4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 3, 1, 1, 3, 2, 1, 3],
        D8: [4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 4, 1, 1, 3, 3, 2, 5],
        D9: [4, 4, 4, 5, 5, 4, 4, 4, 4, 5, 4, 1, 1, 3, 3, 2, 5],
        D10: [5, 5, 5, 5, 5, 5, 4, 4, 4, 5, 5, 1, 1, 3, 4, 2, 6],
        D11: [5, 5, 5, 6, 6, 5, 5, 4, 4, 6, 5, 1, 1, 5, 4, 2, 6],
        D12: [6, 6, 6, 6, 6, 6, 5, 5, 5, 6, 6, 1, 1, 5, 5, 3, 6],
        D13: [6, 6, 6, 7, 6, 6, 5, 5, 5, 7, 6, 1, 1, 5, 5, 3, 8],
        D14: [7, 7, 7, 7, 7, 6, 6, 5, 5, 7, 7, 1, 1, 5, 6, 3, 8],
        D15: [7, 7, 7, 7, 7, 7, 6, 6, 6, 7, 7, 1, 1, 7, 6, 3, 10],
        D16: [7, 7, 7, 8, 8, 7, 7, 7, 7, 8, 7, 1, 1, 7, 8, 5, 10],
        D17: [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 7, 10, 5, 10],
        D18: [8, 8, 8, 9, 9, 8, 8, 8, 8, 9, 8, 1, 1, 7, 10, 20, 20],
        D19: [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 2, 9, 15, 25, 25],
	]

    PILOT = 'mod_fighter_level_basic'
    CLASS_FIGHTER = 'class_figher'

    NPC_SHIPARCH_TEMPLATE = '''[NPCShipArch]
nickname = {npc_shiparch_nickname}
loadout = {loadout_nickname}
level = {level}
ship_archetype = {shiparch}
pilot = {pilot}
state_graph = FIGHTER
npc_class = {classes_list}'''

    def __init__(self, faction, ship, level):
        self.faction = faction
        self.ship = ship
        self.level = level

    def get_npc_level_code(self):
        return 'd{}'.format(self.level)

    def get_npc_shiparch_nickname(self):
        return 'gen_{faction_code}_{shipclass_name}_{level_code}'.format(
            faction_code=faction.CODE,
            shipclass_name=ship.SHIPCLASS_NAME,
            level_code=self.get_npc_level_code()
        )

    def get_loadout_nickname(self):
        return self.get_npc_shiparch_nickname()

    def get_required_equipment(self):
        return zip(self.EQUIP_COLUMNS, self.EQUIPMENT_MAP[self.level])

    def get_classes_list(self):
        classes = [
            self.faction.LEGALITY,
            CLASS_FIGHTER,
            get_npc_level_code(),
        ]
        classes += self.ship.EXTRA_CLASSES
        return ', '.join(classes)

    def get_npc_shiparch_template_params(self):
        return {
            'npc_shiparch_nickname': self.get_npc_shiparch_nickname(),
            'loadout_nickname': self.get_loadout_nickname(),
            'shiparch': self.ship.ARCHETYPE,
            'pilot': self.PILOT,
            'classes_list': self.get_classes_list(),
        }

    def get_npc_shiparch(self):
        self.NPC_SHIPARCH_TEMPLATE.format(**self.get_npc_shiparch_template_params())
