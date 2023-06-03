from world.equipment import Equipment
from world.npc import NPC


class Ship(object):
    ARCHETYPE = None
    MISSILE_MOUNT_POINT = None
    CARGO_TEMPLATE = '''
cargo = {nickname}, {amount}'''
    EXTRA_CLASSES = []


class Ship1(object):
    NPC_LEVELS = NPC.SHIP1_LEVELS


class Ship2(object):
    NPC_LEVELS = NPC.SHIP2_LEVELS


class Ship3(object):
    NPC_LEVELS = NPC.SHIP3_LEVELS


class ShipInterceptor(Ship):
    SHIPCLASS_NAME = 'interceptor'
    EQUIPMENT_SHIPCLASS = Equipment.SHIPCLASS_FIGHTER
    EXTRA_CLASSES = ['class_interceptor']



class ShipElite(Ship):
    SHIPCLASS_NAME = 'elite'
    EQUIPMENT_SHIPCLASS = Equipment.SHIPCLASS_ELITE
    EXTRA_CLASSES = ['class_elite_fighter']


class ShipFreighter(Ship):
    EQUIPMENT_SHIPCLASS = Equipment.SHIPCLASS_FREIGHTER
    SHIPCLASS_NAME = 'freighter'
    EXTRA_CLASSES = []


class Dagger(ShipInterceptor, Ship1):
    ARCHETYPE = 'bw_fighter'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield}, HpShield01
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {torpedo}, HpTorpedo01
equip = {cm}, HpCM01
equip = {mine}, HpMine01
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
    ARCHETYPE = 'rh_fighter'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield}, HpShield01
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {torpedo}, HpTorpedo01
equip = {cm}, HpCM01
equip = {mine}, HpMine01
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


class Stiletto(ShipElite, Ship1):
    ARCHETYPE = 'bw_elite'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield}, HpTurret01
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {weapon5}, HpWeapon05
equip = {weapon6}, HpWeapon06
equip = {torpedo}, HpTorpedo01
equip = {cm}, HpCM01
equip = {mine}, HpMine01
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


class Sabre(ShipElite, Ship2):
    ARCHETYPE = 'bw_elite2'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield}, HpTurret01
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {weapon5}, HpWeapon05
equip = {weapon6}, HpWeapon06
equip = {torpedo}, HpTorpedo01
equip = {cm}, HpCM01
equip = {mine}, HpMine01
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
    ARCHETYPE = 'rh_elite'

    SHIP_TEMPLATE = '''[Loadout]
nickname = {loadout_nickname}
archetype = {ship_archetype}
equip = launch_extend
equip = {engine}
equip = infinite_power
equip = {scanner}
equip = {tractor}
equip = {armor}
equip = {shield}, HpShield01
equip = {weapon1}, HpWeapon01
equip = {weapon2}, HpWeapon02
equip = {weapon3}, HpWeapon03
equip = {weapon4}, HpWeapon04
equip = {weapon5}, HpWeapon05
equip = {weapon6}, HpWeapon06
equip = {torpedo}, HpTorpedo01
equip = {cm}, HpCM01
equip = {mine}, HpMine01
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
