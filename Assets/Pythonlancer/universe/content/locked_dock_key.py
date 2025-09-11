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

    EQUIP_TEMPLATE = '''
    
[LootCrate]
nickname = loot_{key_equip}
DA_archetype = equipment\\models\\hardware\\ge_shield_capacitor.3db
material_library = equipment\\models\\ge_equip.mat
LODranges = 0, 1
hit_pts = 25000
mass = 10
explosion_arch = {tractored_explosion}
tractored_explosion = {tractored_explosion}

[Munition]
nickname = {key_equip}
loot_appearance = loot_{key_equip}
units_per_container = 16
hp_type = hp_gun
requires_ammo = true
hit_pts = 2
one_shot_sound = fire_missile_regular
detonation_dist = 4
lifetime = 1
Motor = rh_missile_01_motor
force_gun_ori = false
const_effect = rh_missile02_drive
HP_trail_parent = HPExhaust
seeker = LOCK
time_to_lock = 0
seeker_range = 1
seeker_fov_deg = 1
max_angular_velocity = 1
DA_archetype = equipment\\models\\hardware\\ge_shield_capacitor.3db
material_library = equipment\\models\\ge_equip.mat
ids_name = {ids_name}
ids_info = {ids_info}
mass = 10
volume = 0.000000
tractored_explosion = {tractored_explosion}
'''

    INTIIAL_WORLD_TEMPLATE = ''';{base_nickname}
locked_gate = {int_hash}
npc_locked_gate = {int_hash}'''
    STORY_TEMPLATE = 'Act_LockDock = Player, {base_nickname}, lock'
    
    def __init__(self, locked_base, key_fx, key_name):
        self.locked_base = locked_base
        self.base_nickname = self.locked_base.get_base_nickname()
        self.equip_name = self.create_equip_name()
        self.key_fx = key_fx
        self.ids_name = self.locked_base.system.key_ids.new_name(key_name)

    def create_equip_name(self):
        return self.EQUIP_NAME_TEMPLATE.format(base_name=self.base_nickname)

    def get_equip_name(self):
        return self.equip_name

    def get_ids_name(self):
        return self.ids_name.id

    def get_ids_info(self):
        return 1

    def get_dock_key(self):
        return self.DOCK_KEY_TEMPLATE.format(key_equip=self.equip_name, base_name=self.locked_base.get_inspace_nickname())

    def get_equip(self):
        return self.EQUIP_TEMPLATE.format(
            key_equip=self.equip_name,
            tractored_explosion=self.key_fx,
            ids_name=self.get_ids_name(),
            ids_info=self.get_ids_info()
        )

    def get_good(self):
        return self.GOOD_TEMPLATE.format(key_equip=self.equip_name)

    def get_initial_world(self):
        return self.INTIIAL_WORLD_TEMPLATE.format(
            base_nickname=self.base_nickname,
            int_hash=CreateId.get_int_id(self.locked_base.get_inspace_nickname())
        )

    def get_story(self):
        return self.STORY_TEMPLATE.format(base_nickname=self.base_nickname)
