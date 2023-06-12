from world.equipment import Equipment
from world.npc import NPC

DIVIDER = "\n"
CLASS_INTERCEPTOR = 'class_interceptor'
CLASS_ELITE = 'class_elite_fighter'

CLASS_RHEINLAND_INTERCEPTOR = 'class_rheinland_interceptor'
CLASS_RHEINLAND_ELITE = 'class_rheinland_elite'
CLASS_RHEINLAND_FIGHTER_ONLY = 'class_rheinland_fighter_only'

class Ship(object):
    ARCHETYPE = None
    MISSILE_MOUNT_POINT = None
    EQUIP_TEMPLATE= '''
equip = {nickname}, {hardpoint}'''
    CARGO_TEMPLATE = '''
cargo = {nickname}, {amount}'''
    EXTRA_CLASSES = []
    HP_TORPEDO = 'HpTorpedo01'
    HP_CM = 'HpCM01'
    HP_MINE = 'HpMine01'
    DEFAULTS = {
        'scanner': 'scanner_npc',
        'tractor': 'tractor01',
        'armor': 'armor_scale_fighter_level1',
    }

    @staticmethod
    def get_extra_content(torpedo, cm, mine, torpedo_ammo, cm_ammo, mine_ammo):
        extra = []
        if torpedo:
            extra.append(Ship.EQUIP_TEMPLATE, format(torpedo, Ship.HP_TORPEDO))
            if torpedo_ammo:
                extra.append(Ship.CARGO_TEMPLATE, format(torpedo, torpedo_ammo))

        if cm:
            extra.append(Ship.EQUIP_TEMPLATE, format(cm, Ship.HP_CM))
            if cm_ammo:
                extra.append(Ship.CARGO_TEMPLATE, format(torpedo, cm_ammo))

        if mine:
            extra.append(Ship.EQUIP_TEMPLATE, format(mine, Ship.HP_MINE))
            if mine_ammo:
                extra.append(Ship.CARGO_TEMPLATE, format(torpedo, mine_ammo))

        return DIVIDER.join(extra)


class Ship1(object):
    NPC_LEVELS = NPC.SHIP1_LEVELS


class Ship2(object):
    NPC_LEVELS = NPC.SHIP2_LEVELS


class Ship3(object):
    NPC_LEVELS = NPC.SHIP3_LEVELS


class ShipInterceptor(Ship):
    SHIPCLASS_NAME = 'interceptor'
    EQUIPMENT_SHIPCLASS = Equipment.SHIPCLASS_FIGHTER
    EXTRA_CLASSES = [CLASS_INTERCEPTOR]


class ShipFighter(Ship):
    SHIPCLASS_NAME = 'fighter'
    EQUIPMENT_SHIPCLASS = Equipment.SHIPCLASS_ELITE
    EXTRA_CLASSES = [CLASS_ELITE]


class ShipElite(Ship):
    SHIPCLASS_NAME = 'elite'
    EQUIPMENT_SHIPCLASS = Equipment.SHIPCLASS_ELITE
    EXTRA_CLASSES = [CLASS_ELITE]


class ShipFreighter(Ship):
    EQUIPMENT_SHIPCLASS = Equipment.SHIPCLASS_FREIGHTER
    SHIPCLASS_NAME = 'freighter'
    EXTRA_CLASSES = []


class Dagger(ShipInterceptor, Ship1):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_RHEINLAND_INTERCEPTOR]

    ARCHETYPE = 'bw_fighter'
    HP_TORPEDO = 'HpTorpedo01'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
cargo = {power}, 1
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield_npc}, HpShield01
cargo = {shield}, 1
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {afterburn1}, HpThruster01
equip = {afterburn2}, HpThruster02
equip = LargeWhiteSpecial, HpHeadlight
equip = {small_light}, HpRunningLight01
equip = {small_light}, HpRunningLight02
equip = {small_light}, HpRunningLight03
equip = {small_light}, HpRunningLight04
equip = {small_light}, HpRunningLight05
equip = {small_light}, HpRunningLight08
equip = DockingLightRedSmall, HpDockLight01
equip = DockingLightRedSmall, HpDockLight02
equip = {contrail}, HpContrail01
equip = {contrail}, HpContrail02
equip = {contrail}, HpContrail03
equip = {contrail}, HpContrail04
equip = single_eng_force, HpEngine01
equip = single_eng_weight, HpCockpit
{extra}'''


class Banshee(ShipInterceptor, Ship2):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_RHEINLAND_INTERCEPTOR]

    ARCHETYPE = 'rh_fighter'
    TORPEDO_HP = 'HpTorpedo01'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
cargo = {power}, 1
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield_npc}, HpShield01
cargo = {shield}, 1
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {afterburn1}, HpThruster01
equip = {afterburn2}, HpThruster02
equip = LargeWhiteSpecial, HpHeadlight
equip = {small_light}, HpRunningLight01
equip = {small_light}, HpRunningLight02
equip = {small_light}, HpRunningLight03
equip = {small_light}, HpRunningLight04
equip = {small_light}, HpRunningLight05
equip = {small_light}, HpRunningLight06
equip = DockingLightRedSmall, HpDockLight01
equip = DockingLightRedSmall, HpDockLight02
equip = {contrail}, HpContrail01
equip = {contrail}, HpContrail02
equip = {contrail}, HpContrail03
equip = {contrail}, HpContrail04
equip = single_eng_force, HpEngine01
equip = single_eng_weight, HpCockpit
{extra}'''


class Stiletto(ShipFighter, Ship1):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE, CLASS_RHEINLAND_FIGHTER_ONLY]

    ARCHETYPE = 'bw_elite'
    TORPEDO_HP = 'HpTorpedo01'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
cargo = {power}, 1
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield_npc}, HpTurret01
cargo = {shield}, 1
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {weapon5}, HpWeapon05
equip = {weapon6}, HpWeapon06
equip = {afterburn1}, HpThruster01
equip = {afterburn2}, HpShield01
equip = LargeWhiteSpecial, HpHeadlight
equip = {small_light}, HpRunningLight01
equip = {small_light}, HpRunningLight02
equip = {small_light}, HpRunningLight03
equip = {small_light}, HpRunningLight04
equip = {small_light}, HpRunningLight05
equip = {small_light}, HpRunningLight06
equip = {small_light}, HpRunningLight07
equip = {small_light}, HpRunningLight08
equip = DockingLightRedSmall, HpDockLight01
equip = DockingLightRedSmall, HpDockLight02
equip = {contrail}, HpContrail01
equip = {contrail}, HpContrail02
equip = {contrail}, HpContrail03
equip = {contrail}, HpContrail04
equip = double_same_eng_force, HpEngine01
equip = double_same_eng_force, HpEngine02
equip = double_eng_weight, HpCockpit
{extra}'''


class Sabre(ShipFighter, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE, CLASS_RHEINLAND_FIGHTER_ONLY]

    ARCHETYPE = 'bw_elite2'
    TORPEDO_HP = 'HpTorpedo01'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
cargo = {power}, 1
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield_npc}, HpTurret01
cargo = {shield}, 1
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {weapon5}, HpWeapon05
equip = {weapon6}, HpWeapon06
equip = {afterburn1}, HpThruster01
equip = {afterburn2}, HpShield01
equip = LargeWhiteSpecial, HpHeadlight
equip = {small_light}, HpRunningLight01
equip = {small_light}, HpRunningLight02
equip = {small_light}, HpRunningLight03
equip = {small_light}, HpRunningLight04
equip = {small_light}, HpRunningLight05
equip = {small_light}, HpRunningLight06
equip = {small_light}, HpRunningLight07
equip = {small_light}, HpRunningLight08
equip = DockingLightRedSmall, HpDockLight01
equip = DockingLightRedSmall, HpDockLight02
equip = {contrail}, HpContrail01
equip = {contrail}, HpContrail02
equip = {contrail}, HpContrail03
equip = {contrail}, HpContrail04
equip = double_same_eng_force, HpEngine01
equip = double_same_eng_force, HpEngine02
equip = double_eng_weight, HpCockpit
{extra}'''


class Valkyrie(ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE]

    ARCHETYPE = 'rh_elite'
    TORPEDO_HP = 'HpTorpedo01'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
cargo = {power}, 1
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield_npc}, HpShield01
cargo = {shield}, 1
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {weapon5}, HpWeapon05
equip = {weapon6}, HpWeapon06
equip = {afterburn1}, HpThruster01
equip = {afterburn2}, HpThruster02
equip = LargeWhiteSpecial, HpHeadlight
equip = {small_light}, HpRunningLight01
equip = {small_light}, HpRunningLight02
equip = {small_light}, HpRunningLight03
equip = {small_light}, HpRunningLight04
equip = {small_light}, HpRunningLight05
equip = {small_light}, HpRunningLight06
equip = DockingLightRedSmall, HpDockLight01
equip = DockingLightRedSmall, HpDockLight02
equip = {contrail}, HpContrail01
equip = {contrail}, HpContrail02
equip = {contrail}, HpContrail03
equip = {contrail}, HpContrail04
equip = double_same_eng_force, HpEngine01
equip = double_same_eng_force, HpEngine02
equip = double_eng_weight, HpCockpit
{extra}'''
