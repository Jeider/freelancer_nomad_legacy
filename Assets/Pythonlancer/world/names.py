FACTION_RH = 1
FACTION_LI = 2
FACTION_BR = 3
FACTION_KU = 4
FACTION_CO = 5

ALL_FACTIONS = [
    FACTION_RH,
    FACTION_LI,
    FACTION_BR,
    FACTION_KU,
    FACTION_CO,
]

# GUNS

LIGHTGUN = 'light'
HEAVYGUN = 'heavy'
CIVGUN = 'civilian'
PIRATEGUN = 'pirate'
HUNTERGUN = 'hunter'
SHIELDGUN = 'shield'

# MISSILE

MAIN_MISSILE = 'missile_main'
FAST_MISSILE = 'missile_fast'
MAIN_SUPER_MISSILE = 'missile_main_super'
SHIELD_MISSILE = 'missile_shield'
CD_MISSILE = 'missile_cd'
TORPEDO_MISSILE = 'missile_torp'
MINE_CIV = 'mine_civ'
MINE_PROF = 'mine_prof'
MINE_MIL = 'mine_mil'
CM = 'cm'

DEBUG_CLASSES = [1, 2, 3, 4, 5, 6]
DEBUG_CLASSES_SHIELDGUN = [1, 3, 4]

WEAPON_RH = 1
WEAPON_LI = 2
WEAPON_BR = 3
WEAPON_KU = 4
WEAPON_BW = 5

EQUIP_RH = 'rh'
EQUIP_LI = 'li'
EQUIP_BR = 'br'
EQUIP_KU = 'ku'
EQUIP_BW = 'bw'

# MISC EQUIP TYPES

GEN_MAIN = 20
GEN_CIV = 21
GEN_PIRATE = 22

RH_MAIN = 1
RH_CIV = 2
RH_PIRATE = 3

LI_MAIN = 4
LI_CIV = 5
LI_PIRATE = 6

BR_MAIN = 7
BR_CIV = 8
BR_PIRATE = 9

KU_MAIN = 10
KU_CIV = 11
KU_PIRATE = 12

CO_ORDER = 13
CO_CORSAIR = 14
CO_OUTCAST = 15

TYPE_PER_GEN_TYPE = {
    EQUIP_RH: {
        GEN_MAIN: RH_MAIN,
        GEN_CIV: RH_CIV,
        GEN_PIRATE: RH_PIRATE,
    },

    EQUIP_LI: {
        GEN_MAIN: LI_MAIN,
        GEN_CIV: LI_CIV,
        GEN_PIRATE: LI_PIRATE,
    },

    EQUIP_BR: {
        GEN_MAIN: BR_MAIN,
        GEN_CIV: BR_CIV,
        GEN_PIRATE: BR_PIRATE,
    },

    EQUIP_KU: {
        GEN_MAIN: KU_MAIN,
        GEN_CIV: KU_CIV,
        GEN_PIRATE: KU_PIRATE,
    },

    EQUIP_BW: {
        GEN_MAIN: CO_ORDER,
        GEN_CIV: CO_OUTCAST,
        GEN_PIRATE: CO_CORSAIR,
    }

}

# COMMODITY

DEFAULT = 'default'
BASIC = 'basic'
ROID = 'roid'
ALLOY = 'alloy'
PRODUCT = 'product'
LUXURY = 'luxury'
CONTRABAND = 'contraband'

TERRAFORM_MINERALS = 'terraform_minerals'
TERRAFORM_GASES = 'terraform_gases'
LASER_BEAM_PARS = 'laserbeam_parts'

BASIC_WATER = 'water'
BASIC_OXYGEN = 'oxygen'
BASIC_FOOD = 'food'
BASIC_CONSUMER = 'consumer'
BASIC_MEDS = 'meds'
BASIC_WEAPONS = 'weapons'
BASIC_TOXIC = 'toxic'

METAL = 'metal'
POWER_SOLAR_EMPTY = 'power_solar_empty'
POWER_SOLAR = 'power_solar'
ALLOY_BASIC = 'alloy'
GAS_BALLOONS = 'gas_balloons'
WATER_EXTRA = 'water_extra'
GAS_FUEL = 'gas_fuel'

DIAMONDS = 'diamonds'
LUXURY_DIAMONDS = 'luxury_diamonds'
NIOBIUM = 'niobium'
PROD_MACHINES = 'prod_machines'
STATION_PANELS = 'station_panels'
ALLOY_HEAVY = 'alloy_heavy'
ROID_MINER_PARTS = 'roid_miner_parts'
SMELTER_PARTS = 'smelter_parts'
SHIP_HULL_PANELS = 'ship_hull_panels'

BERILIUM = 'berilium'
NICOLLUM = 'nicollum'
LUXURY_GOODS = 'luxury_goods'
TLR_PARTS = 'tlr_parts'
ENGINE_PARTS = 'engine_parts'
JUMPGATE_PARTS = 'jumpgate_parts'
ALLOY_TEMPERATURE = 'alloy_temperature'
MINING_EQUIPMENT = 'mining_equipment'
POLYMERS = 'polymers'

URANIUM = 'uranium'
PLUMBUM = 'plumbum'
REACTORS = 'reactors'
MOX_FUEL = 'mox_fuel'
AMMUNITION = 'ammunition'
LUXURY_FOOD = 'luxury_food'
ALLOY_RADIATION = 'alloy_radiation'
GREENHOUSE_PARTS = 'greenhouse_parts'
DEFENCE_SYSTEMS = 'defence_systems'

GOLD = 'gold'
SILVER = 'silver'
ELECTRONICS = 'electronics'
LUXURY_GOLD = 'luxury_gold'
OPTICAL_CHIPS = 'optical_chips'
ALLOY_CONDUCTOR = 'alloy_conductor'
GAS_MINER_PARTS = 'gas_miner_parts'
SOLAR_PLANT_PARTS = 'solar_plant_parts'
RESEARCH_EQUIP = 'research_equip'
