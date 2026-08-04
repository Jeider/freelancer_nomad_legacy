from tools.create_id import CreateId

from text.dividers import SINGLE_DIVIDER


class LockedDockKey(object):

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
    
    def __init__(self, system, key_archetype_nickname,
                 locked_bases, unlocks_bases,
                 key_fx=None, key_name=None, key_description=None):
        self.system = system
        self.key_archetype_nickname = key_archetype_nickname
        if len(locked_bases) == 0:
            raise Exception('Locked bases should be list and not null')
        self.locked_bases = locked_bases
        self.unlocks_bases = unlocks_bases

        self.unlockable = len(unlocks_bases) > 0

        if self.unlockable:
            if key_fx is None:
                raise Exception(f'Key {key_archetype_nickname} is unlockable and key_fx is required')
            if key_name is None:
                raise Exception(f'Key {key_archetype_nickname} is unlockable and key_name is required')
            if key_description is None:
                raise Exception(f'Key {key_archetype_nickname} is unlockable and key_description is required')

            self.equip_name = key_archetype_nickname
            self.key_fx = key_fx
            self.ids_name = self.system.key_ids.new_name(key_name)
            self.ids_info = self.system.key_ids.new_info(key_description)

    def get_equip_name(self):
        return self.equip_name

    def get_ids_name(self):
        return self.ids_name.id

    def get_ids_info(self):
        return self.ids_info.id

    def get_dock_key(self):
        if not self.unlockable:
            return ''  # Allow key to be unlocked by something else

        items = [f'key = {self.equip_name}']
        for b in self.unlocks_bases:
            items.append(
                f'docks = {b}'
            )
        items.append('mounted = false')
        return SINGLE_DIVIDER.join(items)

    def get_equip(self):
        if not self.unlockable:
            return ''  # Do not make key unlock equip, because it isn't required

        return self.EQUIP_TEMPLATE.format(
            key_equip=self.equip_name,
            tractored_explosion=self.key_fx,
            ids_name=self.get_ids_name(),
            ids_info=self.get_ids_info()
        )

    def get_good(self):
        if not self.unlockable:
            return ''  # Do not make key unlock equip, because it isn't required

        return self.GOOD_TEMPLATE.format(key_equip=self.equip_name)

    def get_initial_world(self):
        items = [f';{self.key_archetype_nickname}']
        for b in self.locked_bases:
            int_hash = CreateId.get_int_id(b)
            items.append(f'locked_gate = {int_hash}')
            items.append(f'npc_locked_gate = {int_hash}')
        return SINGLE_DIVIDER.join(items)

    def get_new_player(self):
        items = [f';{self.key_archetype_nickname}']
        for b in self.locked_bases:
            int_hash = CreateId.get_int_id(b)
            items.append(f'locked_gate = {int_hash}')
        return SINGLE_DIVIDER.join(items)

    def get_story(self):
        items = []
        for b in self.locked_bases:
            items.append(f'Act_LockDock = Player, {b}, lock')
        return SINGLE_DIVIDER.join(items)
