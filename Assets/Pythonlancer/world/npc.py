from text.dividers import SINGLE_DIVIDER

EXTRA_REPAIR = [
    'cargo = ge_s_repair_01, 2',
    'cargo = ge_s_battery_01, 2',
]


class EqMap(object):

    def __init__(
        self,
        engine=None,
        power=None,
        shield=None,
        weapon1=None,
        weapon2=None,
        weapon3=None,
        weapon4=None,
        weapon5=None,
        weapon6=None,
        afterburn1=None,
        afterburn2=None,
        torpedo=None,
        cm=None,
        mine=None,
        torpedo_ammo=None,
        cm_ammo=None,
        mine_ammo=None,
        base_level=None,
    ):
        self.engine = engine or base_level
        self.power = power or base_level
        self.shield = shield or base_level
        self.weapon1 = weapon1 or base_level
        self.weapon2 = weapon2 or base_level
        self.weapon3 = weapon3 or base_level
        self.weapon4 = weapon4 or base_level
        self.weapon5 = weapon5 or base_level
        self.weapon6 = weapon6 or base_level
        self.afterburn1 = afterburn1 or base_level
        self.afterburn2 = afterburn2 or base_level
        self.torpedo = torpedo
        self.cm = cm
        self.mine = mine
        self.torpedo_ammo = torpedo_ammo
        self.cm_ammo = cm_ammo
        self.mine_ammo = mine_ammo


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

    SHIP_CLASS_PER_LEVEL = {
        D1: 1,
        D2: 2,
        D3: 3,
        D4: 4,
        D5: 4,
        D6: 4,
        D7: 4,
        D8: 5,
        D9: 5,
        D10: 5,
        D11: 5,
        D12: 6,
        D13: 6,
        D14: 6,
        D15: 6,
        D16: 7,
        D17: 7,
        D18: 7,
        D19: 8,
    }

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
        D13, D14, D15, D16,
        D17, D18, D19
    ]

    SHIP2_LEVELS = [
        D1, D2, D3, D4,
        D5, D6, D7, D8,
        D9, D10, D11, D12,
        D13, D14, D15, D16,
        D17, D18, D19
    ]

    SHIP3_LEVELS = [
        D1, D2, D3, D4,
        D5, D6, D7, D8,
        D9, D10, D11, D12,
        D13, D14, D15, D16,
        D17, D18, D19
    ]

    ENGINE = 'engine'
    POWER = 'power'
    SHIELD = 'shield'
    ARMOR = 'armor'
    WEAPON_1 = 'weapon1'
    WEAPON_2 = 'weapon2'
    WEAPON_3 = 'weapon3'
    WEAPON_4 = 'weapon4'
    WEAPON_5 = 'weapon5'
    WEAPON_6 = 'weapon6'
    AFTERBURN_1 = 'afterburn1'
    AFTERBURN_2 = 'afterburn2'
    TORPEDO = 'torpedo'
    CM = 'cm'
    MINE = 'mine'
    TORPEDO_AMMO = 'torpedo_ammo'
    CM_AMMO = 'cm_ammo'
    MINE_AMMO = 'mine_ammo'

    SHIELD_NPC = 'shield_npc'
    SMALL_LIGHT = 'small_light'
    LOADOUT_NICKNAME = 'loadout_nickname'
    SHIP_ARCHETYPE = 'ship_archetype'
    EXTRA = 'extra'
    CONTRAIL = 'contrail'

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

    # PILOT = 'mod_fighter_level_basic'
    PILOT = 'mod_fighter_universe'
    # PILOT = 'pilot_pirate_easy'
    CLASS_FIGHTER = 'class_fighter'

    NPC_SHIPARCH_TEMPLATE = '''[NPCShipArch]
nickname = {npc_shiparch_nickname}
loadout = {loadout_nickname}
level = {level}
ship_archetype = {shiparch}
pilot = {pilot}
state_graph = FIGHTER
npc_class = {classes_list}'''

    def __init__(self, faction, ship, equip_map=None, level=None, name=None,
                 extra_equip=None, have_afterburn1=True, have_afterburn2=True, gen_armor=True,
                 animated_wings=True):
        self.faction = faction
        self.ship = ship
        self.equip_map = equip_map
        self.level = level
        self.name = name
        self.package = None
        self.extra_equip = extra_equip or []
        self.have_afterburn1 = have_afterburn1
        self.have_afterburn2 = have_afterburn2
        self.gen_armor = gen_armor
        self.animated_wings = animated_wings

    def set_name(self, name):
        self.name = name

    def get_npc_level_code(self):
        return 'd{}'.format(self.level)

    def get_npc_shiparch_nickname(self):
        if self.name:
            return self.name
        return 'gen_{faction_code}_{shipclass_name}_{ship_archetype}_{level_code}'.format(
            faction_code=self.faction.CODE,
            shipclass_name=self.ship.SHIPCLASS_NAME,
            ship_archetype=self.ship.ARCHETYPE,
            level_code=self.get_npc_level_code()
        )

    def get_loadout_nickname(self):
        return self.get_npc_shiparch_nickname()

    def get_classes_list(self):
        classes = [
            self.faction.LEGALITY,
            self.CLASS_FIGHTER,
            self.get_npc_level_code(),
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
            'level': self.get_npc_level_code(),
        }

    def get_npc_shiparch(self):
        return self.NPC_SHIPARCH_TEMPLATE.format(**self.get_npc_shiparch_template_params())

    def get_engine_class(self):
        return self.equip_map.engine

    def get_powerplant_class(self):
        return self.equip_map.power

    def get_shield_class(self):
        return self.equip_map.shield

    def get_weapon1_class(self):
        return self.equip_map.weapon1

    def get_weapon2_class(self):
        return self.equip_map.weapon2

    def get_weapon3_class(self):
        return self.equip_map.weapon3

    def get_weapon4_class(self):
        return self.equip_map.weapon4

    def get_weapon5_class(self):
        return self.equip_map.weapon5

    def get_weapon6_class(self):
        return self.equip_map.weapon6

    def have_gen_armor(self):
        return self.gen_armor

    def get_afterburn1_class(self):
        return self.equip_map.afterburn1

    def get_afterburn2_class(self):
        return self.equip_map.afterburn2

    def get_torpedo_class(self):
        return self.equip_map.torpedo

    def get_cm_class(self):
        return self.equip_map.cm

    def get_mine_class(self):
        return self.equip_map.mine

    def get_torpedo_ammo(self):
        return self.equip_map.torpedo_ammo

    def get_cm_ammo(self):
        return self.equip_map.cm_ammo

    def get_mine_ammo(self):
        return self.equip_map.mine_ammo

    def get_armor_index(self):
        return self.SHIP_CLASS_PER_LEVEL[self.level]

    def set_equipment_package(self, package):
        self.package = package

    def get_loadout_template_params(self):
        extra = self.ship.get_extra_items(
            self.package[self.TORPEDO],
            self.package[self.CM],
            self.package[self.MINE],
            self.package[self.TORPEDO_AMMO],
            self.package[self.CM_AMMO],
            self.package[self.MINE_AMMO],
        )
        params = {
            self.LOADOUT_NICKNAME: self.get_loadout_nickname(),
            self.SHIP_ARCHETYPE: self.ship.ARCHETYPE,
            self.ENGINE: self.package[self.ENGINE].get_nickname(),
            self.POWER: self.package[self.POWER].get_nickname(),
            self.SHIELD: self.package[self.SHIELD].get_nickname(),
            self.SHIELD_NPC: self.package[self.SHIELD_NPC].get_nickname(),
            self.ARMOR: self.package[self.ARMOR].get_nickname(),
            self.WEAPON_1: self.package[self.WEAPON_1].get_nickname(),
            self.WEAPON_2: self.package[self.WEAPON_2].get_nickname(),
            self.WEAPON_3: self.package[self.WEAPON_3].get_nickname(),
            self.WEAPON_4: self.package[self.WEAPON_4].get_nickname(),
            self.WEAPON_5: self.package[self.WEAPON_5].get_nickname(),
            self.WEAPON_6: self.package[self.WEAPON_6].get_nickname(),
            self.AFTERBURN_1: self.package[self.AFTERBURN_1].get_nickname() if self.package[self.AFTERBURN_1] else None,
            self.AFTERBURN_2: self.package[self.AFTERBURN_2].get_nickname() if self.package[self.AFTERBURN_1] else None,
            self.SMALL_LIGHT: self.faction.LIGHT,
            self.EXTRA: SINGLE_DIVIDER.join(extra),
            self.CONTRAIL: self.faction.CONTRAIL,
        }
        params.update(self.ship.DEFAULTS)
        return params

    def get_loadout(self, shiparch):
        if not self.package:
            raise Exception('Package is not initialized')
        ship_instance = shiparch.get_ship_by_class(self.ship)

        loadout_template = ship_instance.get_loadout_template(
            have_afterburn1=self.have_afterburn1,
            have_afterburn2=self.have_afterburn2,
            have_gen_armor=self.have_gen_armor(),
            animated_wings=self.animated_wings,
        )
        loadout = loadout_template.format(**self.get_loadout_template_params())

        if len(self.extra_equip) > 0:
            loadout += SINGLE_DIVIDER + SINGLE_DIVIDER.join(self.extra_equip)

        loadout += SINGLE_DIVIDER + SINGLE_DIVIDER.join(EXTRA_REPAIR)

        return loadout
