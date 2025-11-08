from world.equipment import MainMiscEquip, Equipment, DefaultGood, MainEquipPrice
from world import level


class ArmorNPC:

    ARMOR_NPC_TEMPLATE = '''[Armor]
nickname = {nickname}
hit_pts_scale = {armor_scale}
'''
    
    def __init__(self, ship_type, ship_class, armor_index, armor_scale):
        self.ship_type = ship_type
        self.ship_class = ship_class
        self.armor_index = armor_index
        self.armor_scale = armor_scale

    def get_nickname(self):
        return f'npc_armor_{self.ship_type}_{self.ship_class}_scale_{self.armor_index}'

    def get_armor_scale(self):
        return self.armor_scale

    def get_armor_npc_template_params(self):
        return {
            'nickname': self.get_nickname(),
            'armor_scale': self.get_armor_scale(),
        }

    def get_equip(self):
        return self.ARMOR_NPC_TEMPLATE.format(**self.get_armor_npc_template_params())

class PlayerArmor(MainEquipPrice, DefaultGood, MainMiscEquip):
    SCALE_MULTIPLIER_PER_FACTION = {
        MainMiscEquip.FACTION_RH: 0.75,
        MainMiscEquip.FACTION_LI: 1,
        MainMiscEquip.FACTION_BR: 1.25,
        MainMiscEquip.FACTION_KU: 0.5,
        MainMiscEquip.FACTION_CO: 1.5,
    }
    VOLUME_PER_FACTION = {
        MainMiscEquip.FACTION_RH: 6,
        MainMiscEquip.FACTION_LI: 8,
        MainMiscEquip.FACTION_BR: 10,
        MainMiscEquip.FACTION_KU: 4,
        MainMiscEquip.FACTION_CO: 12,
    }
    MODEL_PER_FACTION = {
        MainMiscEquip.FACTION_RH: 'equipment\\models\\hardware\\rh_combat_armor.3db',
        MainMiscEquip.FACTION_LI: 'equipment\\models\\hardware\\li_policing_armor.3db',
        MainMiscEquip.FACTION_BR: 'equipment\\models\\hardware\\br_protective_armor.3db',
        MainMiscEquip.FACTION_CO: 'equipment\\models\\hardware\\br_stealth_armor.3db',
        MainMiscEquip.FACTION_KU: 'equipment\\models\\hardware\\ku_guard_armor.3db',
    }

    ICON_PER_FACTION = {
        MainMiscEquip.FACTION_RH: 'equipment\\models\\icons\\rh\\rh_armor.3db',
        MainMiscEquip.FACTION_LI: 'equipment\\models\\icons\\li\\li_armor.3db',
        MainMiscEquip.FACTION_BR: 'equipment\\models\\icons\\br\\br_armor01.3db',
        MainMiscEquip.FACTION_CO: 'equipment\\models\\icons\\br\\br_armor02.3db',
        MainMiscEquip.FACTION_KU: 'equipment\\models\\icons\\ku\\ku_armor.3db',
    }

    ARMOR_HIT_PTS = 1000

    RH_THRUSTER_ICON = 'equipment\\models\\icons\\rh\\rh_afterburn.3db'
    LI_THRUSTER_ICON = 'equipment\\models\\icons\\li\\li_afterburn.3db'
    BR_THRUSTER_ICON = 'equipment\\models\\icons\\br\\br_afterburn.3db'
    KU_THRUSTER_ICON = 'equipment\\models\\icons\\ku\\ku_afterburn.3db'
    CO_THRUSTER_ICON = 'equipment\\models\\icons\\co\\co_afterburn.3db'

    MAX_PRICE = 240000

    def get_market_level(self):
        return level.MAIN_LEVELS[self.equipment_class]

    def get_nickname(self):
        return '{name}_player_armor_{digit}'.format(
            name=self.get_base_nickname(),
            digit=self.get_equipment_class_digit()
        )

    def get_armor_hit_pts(self):
        return self.ARMOR_HIT_PTS

    def get_da_archetype(self):
        return self.MODEL_PER_FACTION[self.get_faction()]

    def get_volume(self):
        return self.VOLUME_PER_FACTION[self.get_faction()]

    def get_armor_scale(self):
        return (self.rate / 2 * self.SCALE_MULTIPLIER_PER_FACTION[self.get_faction()]) + 1

    def get_icon(self):
        return self.ICON_PER_FACTION[self.get_faction()]

    def get_equip(self):
        return f'''[Armor]
nickname = {self.get_nickname()}
DA_archetype = {self.get_da_archetype()}
material_library = Equipment\\models\\hardware.mat
ids_name = {self.get_ids_name()}
ids_info = {self.get_ids_info()}
HP_child = HpMount
explosion_resistance = 0.25
debris_type = debris_normal
parent_impulse = 20
child_impulse = 80
hit_pts = {self.get_armor_hit_pts()}
volume = {self.get_volume()}
mass = 10
LODranges = 0, 600
lootable = false
hit_pts_scale = {self.get_armor_scale()}
'''

    RU_NAME_PER_TYPE = {
        MainMiscEquip.RH_MAIN: 'Броня Авангард',
        MainMiscEquip.RH_CIV: 'Броня Реванш',
        MainMiscEquip.RH_PIRATE: 'Броня Кондор',

        MainMiscEquip.LI_MAIN: 'Броня Экспресс',
        MainMiscEquip.LI_CIV: 'Броня Церадин',
        MainMiscEquip.LI_PIRATE: 'Броня Поинт Блек',

        MainMiscEquip.BR_MAIN: 'Броня Рабинтекс',
        MainMiscEquip.BR_CIV: 'Броня Интегрис',
        MainMiscEquip.BR_PIRATE: 'Броня Протект-Тех',

        MainMiscEquip.KU_MAIN: 'Броня Арамид',
        MainMiscEquip.KU_CIV: 'Броня Гранит',
        MainMiscEquip.KU_PIRATE: 'Броня Корунд',

        MainMiscEquip.CO_ORDER: 'Доспехи Марса',
        MainMiscEquip.CO_CORSAIR: 'Плитник',
        MainMiscEquip.CO_OUTCAST: 'Кевлар',
    }

    EN_NAME_PER_TYPE = {
        MainMiscEquip.RH_MAIN: 'Vanguard Armor',
        MainMiscEquip.RH_CIV: 'Revenge Armor',
        MainMiscEquip.RH_PIRATE: 'Condor Armor',

        MainMiscEquip.LI_MAIN: 'Express Armor',
        MainMiscEquip.LI_CIV: 'Ceradin Armor',
        MainMiscEquip.LI_PIRATE: 'Point Black Armor',

        MainMiscEquip.BR_MAIN: 'Rabintex Armor',
        MainMiscEquip.BR_CIV: 'Integris Armor',
        MainMiscEquip.BR_PIRATE: 'Protect-Tex Armor',

        MainMiscEquip.KU_MAIN: 'Aramid Armor',
        MainMiscEquip.KU_CIV: 'Granite Armor',
        MainMiscEquip.KU_PIRATE: 'Corundum Armor',

        MainMiscEquip.CO_ORDER: 'Armor of Mars',
        MainMiscEquip.CO_CORSAIR: 'Plate Armor',
        MainMiscEquip.CO_OUTCAST: 'Kevlar Armor',
    }

    def get_max_price(self):
        return self.MAX_PRICE

    def get_ru_base_name(self):
        return self.RU_NAME_PER_TYPE[self.equip_type]

    def get_ru_name(self):
        return '{model} {mark}'.format(
            model=self.get_ru_base_name(),
            mark=self.get_mark_name(),
        )

    def get_ru_fullname(self):
        return self.get_ru_name()

    def get_en_base_name(self):
        return self.EN_NAME_PER_TYPE[self.equip_type]

    def get_en_name(self):
        return '{model} {mark}'.format(
            model=self.get_en_base_name(),
            mark=self.get_mark_name(),
        )

    def get_en_fullname(self):
        return self.get_en_name()

    def get_ru_volume_text(self):
        return f'Объем в трюме: {int(self.get_volume())}'

    def get_en_volume_text(self):
        return f'Cargo space: {int(self.get_volume())}'

    def get_ru_description_content(self):
        content = []

        efficient_text = self.get_ru_equip_efficienty()
        if efficient_text:
            content.append(efficient_text)

        faction_features_text = RU_FEATURES_PER_FACTION.get(self.get_faction())
        if faction_features_text:
            content.append(faction_features_text)

        content.append(self.get_ru_volume_text())
        content.append(RU_SCALE_HINT)

        return content

    def get_en_description_content(self):
        content = []

        efficient_text = self.get_en_equip_efficienty()
        if efficient_text:
            content.append(efficient_text)

        faction_features_text = EN_FEATURES_PER_FACTION.get(self.get_faction())
        if faction_features_text:
            content.append(faction_features_text)

        content.append(self.get_en_volume_text())
        content.append(EN_SCALE_HINT)

        return content


RU_FEATURES_PER_FACTION = {
    MainMiscEquip.FACTION_RH: 'Рейнландская броня умеренно эффектвно упрочняет корпус и занимает не так много места в трюме',
    MainMiscEquip.FACTION_LI: 'Броня Либерти сбалансированно упрочняет корпус корабля за счет места в трюме',
    MainMiscEquip.FACTION_BR: 'Бретонская броня имеет отличную прочность за счет большего занимаемого объема трюма',
    MainMiscEquip.FACTION_KU: 'Броня, сделанная в Кусари, имеет наименьший бонус к прочности корпуса, но при этом занимает меньше всего места в трюме',
    MainMiscEquip.FACTION_CO: 'Броня кораблей пограничных миров максимально улучшает корпус корабля за счет значительного объема занимаемого места в трюме',
}

RU_SCALE_HINT = 'Бонус: броня увеличивает эффективность ваших наноботов'


EN_FEATURES_PER_FACTION = {
    MainMiscEquip.FACTION_RH: 'Rheinland armor efficiently improves your hull and requires less cargo hold space',
    MainMiscEquip.FACTION_LI: 'Liberty armor moderate improves ship hull and requires moderate cargo hold space',
    MainMiscEquip.FACTION_BR: 'Bretonia armor considerable improves shill hull with huge requirements of cargo hold space',
    MainMiscEquip.FACTION_KU: 'Kusari armor have less hull improvements with less requires of cargo hold space',
    MainMiscEquip.FACTION_CO: 'Border World armor have maximal improvements to ship hull, but requires huge space in cargo hold',
}

EN_SCALE_HINT = 'Bonus: armor increases efficiency of your nanobots'
