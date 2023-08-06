
class ArmorNPC():

    ARMOR_NPC_TEMPLATE = '''[Armor]
nickname = {nickname}
hit_pts_scale = {armor_scale}
'''
    
    def __init__(self, armor_index, armor_scale):
        self.armor_index = armor_index
        self.armor_scale = armor_scale

    def get_nickname(self):
        return 'npc_armor_{index}'.format(index=self.armor_index)

    def get_armor_scale(self):
        return self.armor_scale

    def get_armor_npc_template_params(self):
        return {
            'nickname': self.get_nickname(),
            'armor_scale': self.get_armor_scale(),
        }

    def get_equip(self):
        return self.ARMOR_NPC_TEMPLATE.format(**self.get_armor_npc_template_params())
