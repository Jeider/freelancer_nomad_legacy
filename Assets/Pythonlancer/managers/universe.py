import pathlib
from templates.solar.hacker_panel import HackerPanelManager

from universe.universe import *
from universe.system import System
from universe.base import Base, EQUIP_CLASSES_PER_LEVEL
from universe.markets import EquipDealer, ShipDealer

from world.equipment import Equipment

from tools.data_folder import DataFolder

from text.dividers import SINGLE_DIVIDER, DIVIDER


class UniverseManager(object):

    def __init__(self, misc_equip, weapons, shiparch):
        self.hacker_panels_manager = HackerPanelManager()

        self.misc_equip = misc_equip
        self.weapons = weapons
        self.shiparch = shiparch

        self.systems = []
        self.system_content_test = []
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

        self.sync_data()

    def get_random_hacker_panel(self):
        return self.hacker_panels_manager.get_random_hacker_panel()

    def load_systems(self):
        for system in System.subclasses:
            if system.CONTENT:
                system = system(self)
                self.systems.append(system)
                self.system_content_test.append(system.system_content_str)
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

    def get_system_content_test(self):
        return DIVIDER.join(self.system_content_test)

    def get_system_loadouts(self):
        return DIVIDER.join([loadout.build_loadout() for loadout in self.loadouts])

    def get_system_asteroid_definitions(self):
        return [asteroid_definition.get_file_content() for asteroid_definition in self.asteroid_definitions]

    def get_interior_definitions(self):
        return DIVIDER.join(self.interior_definitions)

    def get_mbases_content(self):
        return DIVIDER.join(self.mbases_content)

    def get_key_initial_world(self):
        return DIVIDER.join([key.get_initial_world() for key in self.keys])

    def get_key_equip(self):
        return DIVIDER.join([key.get_equip() for key in self.keys])

    def get_key_good(self):
        return DIVIDER.join([key.get_good() for key in self.keys])

    def get_key_story(self):
        return DIVIDER.join([key.get_story() for key in self.keys])

    def get_dock_key(self):
        return DIVIDER.join([key.get_dock_key() for key in self.keys])

    def sync_data(self):
        for system in self.systems:
            if not system.ALLOW_SYNC:
                continue

            # print(f'sync sys {system.NAME}')
            DataFolder.sync_system_mod(system.NAME, system.SYSTEM_FOLDER, system.system_content_str)

        # print('sync solar gen loadouts')
        DataFolder.sync_solar_gen_loadouts(self.get_system_loadouts())

        for definition in self.asteroid_definitions:
            # print(f'sync ast definition {definition.NAME}')
            DataFolder.sync_asteroid_definition(definition.get_file_name(), definition.zone.SUBFOLDER, definition.get_file_content())

        for tpl_nebula in self.templated_nebulas:
            # print(f'sync templated nebula {tpl_nebula.FILE_NAME}')
            DataFolder.sync_templated_nebula(tpl_nebula.get_file_name(), tpl_nebula.GENERATED_NEBULA_SUBFOLDER, tpl_nebula.get_file_content())

        for file_name, content in self.interior_files.items():
            # print(f'sync interior {file_name}')
            DataFolder.sync_interior(file_name, content)
