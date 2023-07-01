from world.equipment import Equipment
from world.npc import NPC

DIVIDER = "\n"
CLASS_INTERCEPTOR = 'class_interceptor'
CLASS_ELITE = 'class_elite_fighter'

CLASS_RHEINLAND_INTERCEPTOR = 'class_rheinland_interceptor'
CLASS_RHEINLAND_ELITE = 'class_rheinland_elite'
CLASS_RHEINLAND_FIGHTER_ONLY = 'class_rheinland_fighter_only'

CLASS_LIBERTY_INTERCEPTOR = 'class_liberty_interceptor'
CLASS_LIBERTY_ELITE = 'class_liberty_elite'
CLASS_LIBERTY_FIGHTER_ONLY = 'class_liberty_fighter_only'

CLASS_BRETONIA_INTERCEPTOR = 'class_bretonia_interceptor'
CLASS_BRETONIA_ELITE = 'class_bretonia_elite'
CLASS_BRETONIA_FIGHTER_ONLY = 'class_bretonia_fighter_only'

CLASS_KUSARI_INTERCEPTOR = 'class_kusari_interceptor'
CLASS_KUSARI_ELITE = 'class_kusari_elite'
CLASS_KUSARI_FIGHTER_ONLY = 'class_kusari_fighter_only'

CLASS_CORSAIR_INTERCEPTOR = 'class_corsair_interceptor'
CLASS_CORSAIR_ELITE = 'class_corsair_elite'
CLASS_CORSAIR_FIGHTER_ONLY = 'class_corsair_fighter_only'

CLASS_GENERIC_INTERCEPTOR = 'class_generic_interceptor'
CLASS_GENERIC_ELITE = 'class_generic_elite'
CLASS_GENERIC_FIGHTER_ONLY = 'class_generic_fighter_only'

HP_PCT_ENGINE_SINGLE = 1
HP_PCT_ENGINE_DOUBLE_SAME = 1
HP_PCT_ENGINE_DOUBLE_MAIN = 1
HP_PCT_ENGINE_DOUBLE_SECOND = 1
HP_PCT_ENGINE_DOUBLE_SECOND = 1
HP_PCT_ENGINE_TRIPLE_SAME = 1
HP_PCT_ENGINE_TRIPLE_MAIN = 1
HP_PCT_ENGINE_TRIPLE_SECONDARY = 1

HP_PCT_WING = 1
HP_PCT_TAIL = 1
HP_PCT_MISC = 1
HP_PCT_FIN = 1
HP_PCT_FIN_WITH_ENGINE = 1

EXPL_RESIST_ENGINE = 0.25
EXPL_RESIST_WING = 0.5
EXPL_RESIST_MISC = 1

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
    COLLISION_HIT_PTS_PERCENT = {}
    COLLISION_EXPLOSION_RESISTANCE = {}

    HULL_HIT_PTS = None

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

    def get_shiparch_params():
        params = {}

        for hp_key, hp_pct in COLLISION_HIT_PTS_PERCENT.values():
            params[hp_key] = HULL_HIT_PTS * hp_pct

        for resist_key, resist_val in COLLISION_EXPLOSION_RESISTANCE.values():
            params[resist_key] = resist_val

        return params


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


# RHEINLAND


class Dagger(ShipInterceptor, Ship1):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_RHEINLAND_INTERCEPTOR]

    ARCHETYPE = 'bw_fighter'
    TEMPLATE_CODE = 'bwf'
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

    COLLISION_HIT_PTS_PERCENT = {
        'bwf_wing_hit_pts': HP_PCT_WING,
        'bwf_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bwf_wing_expl_resist': EXPL_RESIST_WING,
        'bwf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Banshee(ShipInterceptor, Ship2):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_RHEINLAND_INTERCEPTOR]

    ARCHETYPE = 'rh_fighter'
    TEMPLATE_CODE = 'rf'
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

    COLLISION_HIT_PTS_PERCENT = {
        'rf_wing_hit_pts': HP_PCT_WING,
        'rf_engine_hit_pts': HP_PCT_ENGINE_SINGLE, 
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'rf_wing_expl_resist': EXPL_RESIST_WING,
        'rf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Stiletto(ShipFighter, Ship1):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE, CLASS_RHEINLAND_FIGHTER_ONLY]

    ARCHETYPE = 'bw_elite'
    TEMPLATE_CODE = 'bwe'
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

    COLLISION_HIT_PTS_PERCENT = {
        'bwe_wing1_hit_pts': ,
        'bwe_wing2_hit_pts': ,
        'bwe_engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
        'bwe_engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bwe_wing1_expl_resist': EXPL_RESIST_WING,
        'bwe_wing2_expl_resist': EXPL_RESIST_WING,
        'bwe_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'bwe_engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Sabre(ShipFighter, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE, CLASS_RHEINLAND_FIGHTER_ONLY]

    ARCHETYPE = 'bw_elite2'
    TEMPLATE_CODE = 'bwe2'
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

    COLLISION_HIT_PTS_PERCENT = {
        'bwe2_wing1_hit_pts': ,
        'bwe2_wing2_hit_pts': ,
        'bwe2_engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
        'bwe2_engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bwe2_wing1_expl_resist': EXPL_RESIST_WING,
        'bwe2_wing2_expl_resist': EXPL_RESIST_WING,
        'bwe2_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'bwe2_engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Valkyrie(ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE]

    ARCHETYPE = 'rh_elite'
    TEMPLATE_CODE = 're'
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

    COLLISION_HIT_PTS_PERCENT = {
        're_wing_hit_pts': HP_PCT_WING,
        're_tail_hit_pts': HP_PCT_TAIL,
        're_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        're_wing_expl_resist': EXPL_RESIST_WING,
        're_tail_expl_resist': EXPL_RESIST_WING,
        're_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class ValkyrieMk2(ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_RHEINLAND_ELITE]

    ARCHETYPE = 'rh_elite2'
    TEMPLATE_CODE = 're2'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        're2_wing_hit_pts': HP_PCT_WING,
        're2_tail_hit_pts': HP_PCT_TAIL,
        're2_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        're2_wing_expl_resist': EXPL_RESIST_WING,
        're2_tail_expl_resist': EXPL_RESIST_WING,
        're2_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Humpback(ShipFreighter):
    ARCHETYPE = 'rh_freighter'
    TEMPLATE_CODE = 'rfr'

    COLLISION_HIT_PTS_PERCENT = {
        'rfr_panel_hit_pts': ,
        'rfr_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'rfr_panel_expl_resist': EXPL_RESIST_WING,
        'rfr_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# LIBERTY


class Piranha(ShipInterceptor, Ship1):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_LIBERTY_INTERCEPTOR]

    ARCHETYPE = 'bh_fighter'
    TEMPLATE_CODE = 'bhf'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'bhf_fin_hit_pts': HP_PCT_FIN,
        'bhf_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bhf_fin_expl_resist': EXPL_RESIST_MISC,
        'bhf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Patriot(ShipInterceptor, Ship2):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_LIBERTY_INTERCEPTOR]

    ARCHETYPE = 'li_fighter'
    TEMPLATE_CODE = 'lf'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'lf_fin_hit_pts': HP_PCT_FIN,
        'lf_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'lf_fin_expl_resist': EXPL_RESIST_MISC,  
        'lf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Barracuda(ShipFighter, Ship1):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE, CLASS_LIBERTY_FIGHTER_ONLY]

    ARCHETYPE = 'bh_elite'
    TEMPLATE_CODE = 'bhe'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'bhe_fin1_hit_pts': HP_PCT_FIN,
        'bhe_fin2_hit_pts': HP_PCT_FIN_WITH_ENGINE,
        'bhe_wing_hit_pts': HP_PCT_WING,
        'bhe_engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
        'bhe_engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bhe_fin1_expl_resist': EXPL_RESIST_MISC,
        'bhe_fin2_expl_resist': EXPL_RESIST_MISC,
        'bhe_wing_expl_resist': EXPL_RESIST_WING,
        'bhe_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'bhe_engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Hammerhead(ShipFighter, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE, CLASS_LIBERTY_FIGHTER_ONLY]

    ARCHETYPE = 'bh_elite2'
    TEMPLATE_CODE = 'bhe2'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'bhe2_fin1_hit_pts': HP_PCT_FIN,
        'bhe2_fin2_hit_pts': HP_PCT_FIN_WITH_ENGINE,
        'bhe2_wing_hit_pts': HP_PCT_WING,
        'bhe2_engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
        'bhe2_engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bhe2_fin1_expl_resist': EXPL_RESIST_MISC,
        'bhe2_fin2_expl_resist': EXPL_RESIST_MISC,
        'bhe2_wing_expl_resist': EXPL_RESIST_WING,
        'bhe2_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'bhe2_engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Defender(ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE]

    ARCHETYPE = 'li_elite'
    TEMPLATE_CODE = 'le'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'le_wing_hit_pts': HP_PCT_WING,
        'le_spoiler_hit_pts': HP_PCT_TAIL,
        'le_engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_MAIN,
        'le_engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SECOND,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'le_wing_expl_resist': EXPL_RESIST_WING,
        'le_spoiler_expl_resist': EXPL_RESIST_WING,
        'le_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'le_engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class DefenderJuni(ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_LIBERTY_ELITE]

    ARCHETYPE = 'li_elite2'
    TEMPLATE_CODE = 'le2'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'le2_wing_hit_pts': HP_PCT_WING,
        'le2_spoiler_hit_pts': HP_PCT_TAIL,
        'le2_engine1_hit_pts': HP_PCT_ENGINE_DOUBLE_MAIN,
        'le2_engine2_hit_pts': HP_PCT_ENGINE_DOUBLE_SECOND,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'le2_wing_expl_resist': EXPL_RESIST_WING,
        'le2_spoiler_expl_resist': EXPL_RESIST_WING,
        'le2_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'le2_engine2_expl_resist': EXPL_RESIST_ENGINE,
    }


class Rhino(ShipFreighter):
    ARCHETYPE = 'li_freighter'
    TEMPLATE_CODE = 'lfr'

    COLLISION_HIT_PTS_PERCENT = {
        'lfr_panel_hit_pts': ,
        'lfr_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'lfr_panel_expl_resist': EXPL_RESIST_WING,
        'lfr_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# BRETONIA


class Legionnaire(ShipInterceptor, Ship1):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_BRETONIA_INTERCEPTOR]

    ARCHETYPE = 'co_fighter'
    TEMPLATE_CODE = 'cf'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'cf_wing_hit_pts': HP_PCT_WING,
        'cf_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'cf_wing_expl_resist': EXPL_RESIST_WING,
        'cf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Cavalier(ShipInterceptor, Ship2):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_BRETONIA_INTERCEPTOR]

    ARCHETYPE = 'br_fighter'
    TEMPLATE_CODE = 'bf'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'bf_tail_hit_pts': HP_PCT_TAIL,
        'bf_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bf_tail_expl_resist': EXPL_RESIST_WING,
        'bf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Centurion(ShipFighter, Ship1):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE, CLASS_BRETONIA_FIGHTER_ONLY]

    ARCHETYPE = 'co_elite'
    TEMPLATE_CODE = 'ce'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'ce_wing_hit_pts': HP_PCT_WING,
        'ce_fin_hit_pts': HP_PCT_FIN,
        'ce_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'ce_wing_expl_resist': EXPL_RESIST_WING,
        'ce_fin_expl_resist': EXPL_RESIST_MISC,
        'ce_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Titan(ShipFighter, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE, CLASS_BRETONIA_FIGHTER_ONLY]

    ARCHETYPE = 'co_elite2'
    TEMPLATE_CODE = 'ce2'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'ce2_wing_hit_pts': HP_PCT_WING,
        'ce2_fin_hit_pts': HP_PCT_FIN,
        'ce2_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'ce2_wing_expl_resist': EXPL_RESIST_WING,
        'ce2_fin_expl_resist': EXPL_RESIST_MISC,
        'ce2_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Crusader(ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE]

    ARCHETYPE = 'br_elite'
    TEMPLATE_CODE = 'be'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'be_wing_hit_pts': HP_PCT_WING,
        'be_tail_hit_pts': HP_PCT_TAIL,
        'be_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'be_wing_expl_resist': EXPL_RESIST_WING,
        'be_tail_expl_resist': EXPL_RESIST_WING,
        'be_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class CrusaderMk2(ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_BRETONIA_ELITE]

    ARCHETYPE = 'br_elite2'
    TEMPLATE_CODE = 'be2'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'be2_wing_hit_pts': HP_PCT_WING,
        'be2_tail_hit_pts': HP_PCT_TAIL,
        'be2_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME, 
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'be2_wing_expl_resist': EXPL_RESIST_WING,
        'be2_tail_expl_resist': EXPL_RESIST_WING,
        'be2_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Clydesdale(ShipFreighter):
    ARCHETYPE = 'br_freighter'
    TEMPLATE_CODE = 'bfr'

    COLLISION_HIT_PTS_PERCENT = {
        'bfr_wing_hit_pts': HP_PCT_WING,
        'bfr_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bfr_wing_expl_resist': EXPL_RESIST_WING,
        'bfr_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# KUSARI


class Hawk(ShipInterceptor, Ship1):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_KUSARI_INTERCEPTOR]

    ARCHETYPE = 'ge_fighter4'
    TEMPLATE_CODE = 'gf4'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'gf4_wing_hit_pts': HP_PCT_WING,
        'gf4_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'gf4_wing_expl_resist': EXPL_RESIST_WING,
        'gf4_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Drake(ShipInterceptor, Ship2):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_KUSARI_INTERCEPTOR]

    ARCHETYPE = 'ku_fighter'
    TEMPLATE_CODE = 'kf'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'kf_wing_hit_pts': HP_PCT_MISC,
        'kf_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'kf_wing_expl_resist': EXPL_RESIST_MISC,
        'kf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Falcon(ShipFighter, Ship1):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE, CLASS_KUSARI_FIGHTER_ONLY]

    ARCHETYPE = 'ge_fighter5'
    TEMPLATE_CODE = 'gf5'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'gf5_wing_hit_pts': HP_PCT_WING,
        'gf5_fin_hit_pts': HP_PCT_FIN,
        'gf5_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'gf5_wing_expl_resist': EXPL_RESIST_WING,
        'gf5_fin_expl_resist': EXPL_RESIST_MISC,
        'gf5_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Eagle(ShipFighter, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE, CLASS_KUSARI_FIGHTER_ONLY]

    ARCHETYPE = 'ge_fighter6'
    TEMPLATE_CODE = 'gf6'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'gf6_wing_hit_pts': HP_PCT_WING,
        'gf6_fin_hit_pts': HP_PCT_FIN,
        'gf6_btmwing_hit_pts': HP_PCT_WING,
        'gf6_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'gf6_wing_expl_resist': EXPL_RESIST_WING,
        'gf6_fin_expl_resist': EXPL_RESIST_MISC,
        'gf6_btmwing_expl_resist': EXPL_RESIST_WING,
        'gf6_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Dragon(ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE]

    ARCHETYPE = 'ku_elite'
    TEMPLATE_CODE = 'ke'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'ke_wing_hit_pts': HP_PCT_MAIN,
        'ke_tail_hit_pts': HP_PCT_TAIL,
        'ke_spike_hit_pts': HP_PCT_WING,
        'ke_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'ke_wing_expl_resist': EXPL_RESIST_MISC,
        'ke_tail_expl_resist': EXPL_RESIST_WING,
        'ke_spike_expl_resist': EXPL_RESIST_WING,
        'ke_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class DragonMk2(ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_KUSARI_ELITE]

    ARCHETYPE = 'ku_elite2'
    TEMPLATE_CODE = 'ke2'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'ke2_wing_hit_pts': HP_PCT_MAIN,
        'ke2_tail_hit_pts': HP_PCT_TAIL,
        'ke2_spike_hit_pts': HP_PCT_WING,
        'ke2_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'ke2_wing_expl_resist': EXPL_RESIST_MISC,
        'ke2_tail_expl_resist': EXPL_RESIST_WING,
        'ke2_spike_expl_resist': EXPL_RESIST_WING,
        'ke2_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Dron(ShipFreighter):
    ARCHETYPE = 'ku_freighter'
    TEMPLATE_CODE = 'kfr'

    COLLISION_HIT_PTS_PERCENT = {
        'kfr_wing_hit_pts': HP_PCT_WING,
        'kfr_engine_hit_pts': ,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'kfr_wing_expl_resist': EXPL_RESIST_MISC,
        'kfr_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# CORSAIR / ORDER


class Bloodhound(ShipFighter, Ship1):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_CORSAIR_ELITE, CLASS_CORSAIR_FIGHTER_ONLY]

    ARCHETYPE = 'pi_fighter'
    TEMPLATE_CODE = 'pe'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'pf_fin_hit_pts': HP_PCT_FIN,
        'pf_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'pf_fin_expl_resist': EXPL_RESIST_MISC,
        'pf_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Wolfhound(ShipFighter, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_CORSAIR_ELITE, CLASS_CORSAIR_FIGHTER_ONLY]

    ARCHETYPE = 'pi_elite'
    TEMPLATE_CODE = 'pe'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'pe_fin_hit_pts': HP_PCT_FIN,
        'pe_engine_hit_pts': HP_PCT_ENGINE_TRIPLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'pe_fin_expl_resist': EXPL_RESIST_MISC,
        'pe_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Anubis(ShipElite, Ship3):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_CORSAIR_ELITE]

    ARCHETYPE = 'or_elite'
    TEMPLATE_CODE = 'oe'
    TORPEDO_HP = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'oe_wing_hit_pts': HP_PCT_WING,
        'oe_engine1_hit_pts': HP_PCT_ENGINE_TRIPLE_MAIN,
        'oe_engine2_hit_pts': HP_PCT_ENGINE_TRIPLE_SECONDARY,
        'oe_engine3_hit_pts': HP_PCT_ENGINE_TRIPLE_SECONDARY,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'oe_wing_expl_resist': EXPL_RESIST_WING,
        'oe_engine1_expl_resist': EXPL_RESIST_ENGINE,
        'oe_engine2_expl_resist': EXPL_RESIST_ENGINE,
        'oe_engine3_expl_resist': EXPL_RESIST_ENGINE,
    }


class Mule(ShipFreighter):
    ARCHETYPE = 'pi_freighter'
    TEMPLATE_CODE = 'pfr'

    COLLISION_HIT_PTS_PERCENT = {
        'pfr_wing_hit_pts': HP_PCT_WING,
        'pfr_fin_hit_pts': HP_PCT_FIN,
        'pfr_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'pfr_wing_expl_resist': EXPL_RESIST_WING,
        'pfr_fin_expl_resist': EXPL_RESIST_MISC,
        'pfr_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


# GENERIC


class Dromader(ShipFreighter):
    ARCHETYPE = 'bw_freighter'
    TEMPLATE_CODE = 'bwfr'

    COLLISION_HIT_PTS_PERCENT = {
        'bwfr_wing_hit_pts': HP_PCT_WING,
        'bwfr_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'bwfr_wing_expl_resist': EXPL_RESIST_WING,
        'bwfr_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class CSV(ShipFreighter):
    ARCHETYPE = 'ge_csv'
    TEMPLATE_CODE = 'csv'


class Armored(ShipFreighter):
    ARCHETYPE = 'ge_armored'
    TEMPLATE_CODE = 'armored'


class Starflier(ShipInterceptor, Ship1):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_GENERIC_INTERCEPTOR]

    ARCHETYPE = 'ge_fighter'
    TEMPLATE_CODE = 'gf'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'gf1_wing_hit_pts': HP_PCT_WING,
        'gf1_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'gf1_wing_expl_resist': EXPL_RESIST_WING,
        'gf1_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Startracker(ShipInterceptor, Ship2):
    EXTRA_CLASSES = [CLASS_INTERCEPTOR, CLASS_GENERIC_INTERCEPTOR]

    ARCHETYPE = 'ge_fighter2'
    TEMPLATE_CODE = 'gf'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'gf2_wing_hit_pts': HP_PCT_WING,
        'gf2_engine_hit_pts': HP_PCT_ENGINE_SINGLE,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'gf2_wing_expl_resist': EXPL_RESIST_WING,
        'gf2_engine_expl_resist': EXPL_RESIST_ENGINE,
    }


class Starblazer(ShipElite, Ship2):
    EXTRA_CLASSES = [CLASS_ELITE, CLASS_GENERIC_ELITE]

    ARCHETYPE = 'ge_fighter3'
    TEMPLATE_CODE = 'gf'
    HP_TORPEDO = 'HpTorpedo01'

    COLLISION_HIT_PTS_PERCENT = {
        'gf3_wing_hit_pts': HP_PCT_WING,
        'gf3_engine_hit_pts': HP_PCT_ENGINE_DOUBLE_SAME,
    }

    COLLISION_EXPLOSION_RESISTANCE = {
        'gf3_wing_expl_resist': EXPL_RESIST_WING,
        'gf3_engine_expl_resist': EXPL_RESIST_ENGINE,
    }
