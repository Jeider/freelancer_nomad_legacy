from tools.create_id import CreateId


class LockedDockKey(object):

    DOCK_KEY_TEMPLATE = '''key = {key_equip}
docks = {base_name}
mounted = false'''

    EQUIP_NAME_TEMPLATE = 'key_{base_name}_unlock'

    GOOD_TEMPLATE = '''[Good]
nickname = {key_equip}
equipment = {key_equip}
category = equipment
price = 1
item_icon = Equipment\\models\\commodities\\nn_icons\\COMMOD_credits.3db
combinable = true'''

    EQUIP_TEMPLATE = '''[ShieldGenerator]
nickname = {key_equip}
ids_name = 1
ids_info = 1
DA_archetype = polygon.cmp
HP_child = HpConnect
hit_pts = 5000
explosion_resistance = 0
debris_type = debris_normal
parent_impulse = 20
child_impulse = 80
volume = 0.000000
mass = 10
regeneration_rate = 0
max_capacity = 0
toughness = 10
hp_type = hp_freighter_shield_generator
constant_power_draw = 0
rebuild_power_draw = 0
separation_explosion = sever_debris
LODranges = 0, 1
lootable = true'''

    INTIIAL_WORLD_TEMPLATE = ''';{base_nickname}
locked_gate = {int_hash}
npc_locked_gate = {int_hash}'''
    STORY_TEMPLATE = 'Act_LockDock = Player, {base_nickname}, lock'
    
    def __init__(self, locked_base):
        self.locked_base = locked_base
        self.base_nickname = self.locked_base.get_base_nickname()
        self.equip_name = self.create_equip_name()

    def create_equip_name(self):
        return self.EQUIP_NAME_TEMPLATE.format(base_name=self.base_nickname)

    def get_equip_name(self):
        return self.equip_name

    def get_dock_key(self):
        return self.DOCK_KEY_TEMPLATE.format(key_equip=self.equip_name, base_name=self.locked_base.get_inspace_nickname())

    def get_equip(self):
        return self.EQUIP_TEMPLATE.format(key_equip=self.equip_name)

    def get_good(self):
        return self.GOOD_TEMPLATE.format(key_equip=self.equip_name)

    def get_initial_world(self):
        return self.INTIIAL_WORLD_TEMPLATE.format(
            base_nickname=self.base_nickname,
            int_hash=CreateId.get_int_id(self.locked_base.get_inspace_nickname())
        )

    def get_story(self):
        return self.STORY_TEMPLATE.format(base_nickname=self.base_nickname)
