from managers.misc import MiscEquipManager
from managers.weapon import WeaponManager
from managers.population import PopulationManager


class LancerCore(object):

	def __init__(self):
		self.misc_equip = MiscEquipManager()
		self.weapons = WeaponManager()
		self.population = PopulationManager()

