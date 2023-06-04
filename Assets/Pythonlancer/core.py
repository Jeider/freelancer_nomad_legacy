from managers.misc_equip import MiscEquipManager
from managers.weapon import WeaponManager
from managers.population import PopulationManager


class LancerCore(object):

	def __init__(self):
		self.misc_equip = MiscEquipManager()
		self.weapons = WeaponManager()
		self.population = PopulationManager(self.misc_equip, self.weapons)
