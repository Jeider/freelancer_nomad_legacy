
class ArmorNPC():

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
