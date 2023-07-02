from managers.misc_equip import MiscEquipManager
from managers.weapon import WeaponManager
from managers.population import PopulationManager
from managers.shiparch import ShiparchManager


INITIAL_STRING_ID = 280000


class LancerCore(object):

	def __init__(self):
		self.misc_equip = MiscEquipManager(INITIAL_STRING_ID)
		self.weapons = WeaponManager(self.misc_equip.last_string_id)
		self.population = PopulationManager(self.misc_equip, self.weapons)
		self.shiparch = ShiparchManager()
