from templates.solar.hacker_panel import HackerPanelManager
from templates.hardcoded_inis.universe import UniverseTemplate
from templates.hardcoded_inis.missions import MBasesTemplate
from templates.hardcoded_inis.root import DockKeyTemplate

from universe.root import UniverseRoot
from universe.sirius import *  # initialize system objects
from universe.system import SiriusSystem
from universe.base import Base, EQUIP_CLASSES_PER_LEVEL
from universe.markets import EquipDealer, ShipDealer

from world.equipment import Equipment

from tools.data_folder import DataFolder

from text.dividers import SINGLE_DIVIDER, DIVIDER


class UniverseManager:

    def __init__(self, lancer_core):
        self.core = lancer_core

        self.hacker_panels_manager = HackerPanelManager()
        self.universe_root = UniverseRoot()

        self.misc_equip = self.core.misc_equip
        self.weapons = self.core.weapons
        self.shiparch = self.core.shiparch

        self.systems = []
        self.bases = []
        self.equip_dealers_list = []
        self.ship_dealers_list = []
        self.loadouts = []

        self.asteroid_definitions = []
        self.templated_nebulas = []
        self.interior_files = {}
        self.interior_definitions = []
        self.mbases_content = []

        self.keys = []

        self.load_systems()
        self.load_bases()

        self.get_universe_root().do_post_init_actions()

        self.sync_data()

    def get_random_hacker_panel(self):
        return self.hacker_panels_manager.get_random_hacker_panel()

    def get_universe_root(self):
        return self.universe_root

    def load_systems(self):
        for system in SiriusSystem.subclasses:
            system = system(self)
            self.universe_root.add_system(system)
            if system.have_dynamic_content():
                self.loadouts += system.loadouts
                self.asteroid_definitions += system.asteroid_definitions
                self.templated_nebulas += system.templated_nebulas
                self.keys += system.keys

                interior_definitions, interior_files, mbases_content = system.get_interiors_data()
                self.interior_definitions += interior_definitions
                self.interior_files.update(interior_files)
                self.mbases_content += mbases_content

    def load_bases(self):
        for base_class in Base.subclasses:
            base = base_class()
            self.bases.append(base)

            if base.LEVEL:
                equip_items = self.load_base_equip_items(base)
                dealer = EquipDealer(base.NAME, equip_items)
                self.equip_dealers_list.append(dealer)

            if len(base.SHIPS) > 0:
                dealer = ShipDealer(base.NAME, [self.shiparch.get_ship_by_archetype(ship.ARCHETYPE) for ship in base.SHIPS])
                self.ship_dealers_list.append(dealer)

    def load_base_equip_items(self, base):
        items = []
        if base.GUN:
            equip_classes = base.get_gun_classes()
            for equip_class in equip_classes:
                items.append(self.weapons.get_gun(base.GUN, equip_class))

        if base.ENGINE:
            equip_classes = base.get_engine_classes()
            for equip_class in equip_classes:
                for shipclass in Equipment.SHIPCLASSES:
                    items.append(self.misc_equip.get_engine(shipclass, base.ENGINE, equip_class))

        if base.POWER:
            equip_classes = base.get_power_classes()
            for equip_class in equip_classes:
                for shipclass in Equipment.SHIPCLASSES:
                    items.append(self.misc_equip.get_powerplant(shipclass, base.POWER, equip_class))

        if base.SHIELD:
            equip_classes = base.get_shield_classes()
            for equip_class in equip_classes:
                for shipclass in Equipment.SHIPCLASSES:
                    items.append(self.misc_equip.get_shield(shipclass, base.SHIELD, equip_class))

        if base.THRUSTER:
            equip_classes = base.get_thruster_classes()
            for equip_class in equip_classes:
                items.append(self.misc_equip.get_thruster(base.THRUSTER, equip_class))

        return items

    def get_market_equip(self):
        return DIVIDER.join([dealer.get_market_content() for dealer in self.equip_dealers_list])

    def get_market_ships(self):
        return DIVIDER.join([dealer.get_market_content() for dealer in self.ship_dealers_list])

    def get_system_loadouts(self):
        return DIVIDER.join([loadout.build_loadout() for loadout in self.loadouts])

    def get_system_asteroid_definitions(self):
        return [asteroid_definition.get_file_content() for asteroid_definition in self.asteroid_definitions]

    def get_interior_definitions(self):
        return DIVIDER.join(self.interior_definitions)

    def get_system_definitions(self):
        return DIVIDER.join(system.get_universe_definition() for system in self.universe_root.get_all_systems())

    def get_universe_file_content(self):
        return UniverseTemplate().format({
            'generated_bases': self.get_interior_definitions(),
            'generated_systems': self.get_system_definitions(),
        })

    def get_mbases_content(self):
        return DIVIDER.join(self.mbases_content)

    def get_mbases_file_content(self):
        return MBasesTemplate().format({'generated': self.get_mbases_content()})

    def get_key_initial_world(self):
        return DIVIDER.join([key.get_initial_world() for key in self.keys])

    def get_key_equip(self):
        return DIVIDER.join([key.get_equip() for key in self.keys])

    def get_key_good(self):
        return DIVIDER.join([key.get_good() for key in self.keys])

    def get_key_story(self):
        return SINGLE_DIVIDER.join([key.get_story() for key in self.keys])

    def get_dock_key(self):
        return DIVIDER.join([key.get_dock_key() for key in self.keys])

    def get_dock_key_file_content(self):
        return DockKeyTemplate().format({'generated': self.get_dock_key()})

    def sync_data(self):
        if not self.core.write:
            return

        DataFolder.sync_universe(self.get_universe_file_content())
        DataFolder.sync_mbases(self.get_mbases_file_content())
        DataFolder.sync_dock_key(self.get_dock_key_file_content())

        for the_system in self.universe_root.get_all_systems():
            if not the_system.ALLOW_SYNC:
                continue

            DataFolder.sync_system(the_system.NAME, the_system.SYSTEMS_ROOT, the_system.SYSTEM_FOLDER, the_system.get_content())

        DataFolder.sync_solar_gen_loadouts(self.get_system_loadouts())

        for definition in self.asteroid_definitions:
            DataFolder.sync_asteroid_definition(definition.get_file_name(), definition.zone.SUBFOLDER, definition.get_file_content())

        for tpl_nebula in self.templated_nebulas:
            DataFolder.sync_templated_nebula(tpl_nebula.get_file_name(), tpl_nebula.GENERATED_NEBULA_SUBFOLDER, tpl_nebula.get_file_content())

        for file_name, content in self.interior_files.items():
            DataFolder.sync_interior(file_name, content)
