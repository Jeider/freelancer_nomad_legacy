from templates.space_objects.pirate_base_bizmark import PirateBaseBizmark

base = PirateBaseBizmark()

instance = base.get_instance(new_space_object_name=None, move_to=(60000, 0, 0))

print(instance)
