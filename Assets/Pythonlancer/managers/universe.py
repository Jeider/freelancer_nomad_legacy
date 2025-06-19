from templates.solar.hacker_panel import HackerPanelManager
from templates.hardcoded_inis.universe import UniverseTemplate
from templates.hardcoded_inis.missions import MBasesTemplate
from templates.hardcoded_inis.root import DockKeyTemplate

from universe.root import UniverseRoot
from universe.sirius import *  # initialize system objects
from universe.system import SiriusSystem
from universe.markets import Market

from tools.data_folder import DataFolder

from text.dividers import SINGLE_DIVIDER, DIVIDER


class UniverseManager:

    def __init__(self, lancer_core):
        self.core = lancer_core

        self.ids = self.core.ids.universe
        self.key_ids = self.core.ids.key

        self.hacker_panels_manager = HackerPanelManager()
        self.universe_root = UniverseRoot()

        self.misc_equip = self.core.misc_equip
        self.weapons = self.core.weapons
        self.shiparch = self.core.shiparch

        self.bases_db = {}
        self.bases_list = []

        self.equip_dealers = []
        self.commodity_dealers = []
        self.ship_dealers = []
        self.loadouts = []

        self.asteroid_definitions = []
        self.templated_nebulas = []
        self.interior_files = {}
        self.interior_definitions = []
        self.mbases_content = []

        self.keys = []

        self.load_systems()

        self.get_universe_root().do_post_init_actions()

        self.core.store.compile_producers()

        for base in self.bases_list:
            base.compile_base()

        self.load_system_trade_connections()

        self.core.store.compile_consumers()

        for base in self.bases_list:
            base.post_store_load()

        self.load_interiors()

        self.sync_data()

    def get_random_hacker_panel(self):
        return self.hacker_panels_manager.get_random_hacker_panel()

    def get_universe_root(self):
        return self.universe_root

    def get_base_by_name(self, base_name):
        try:
            return self.bases_db[base_name]
        except IndexError:
            raise Exception('Base %s isnt presented in universe' % base_name)

    def load_systems(self):
        for system_class in SiriusSystem.subclasses:
            system = system_class(self.core, self, ids=self.ids, key_ids=self.key_ids)
            self.universe_root.add_system(system)
            if system.have_dynamic_content():
                self.loadouts += system.loadouts
                self.asteroid_definitions += system.asteroid_definitions
                self.templated_nebulas += system.templated_nebulas
                self.keys += system.keys

                for dockable in system.get_dockable_objects():
                    if dockable.IS_BASE and dockable.have_equip_dealer():
                        self.equip_dealers.append(
                            Market(
                                base_nickname=dockable.get_base_nickname(),
                                items=dockable.EQUIP_SET.get_equip_items(
                                    core=self.core,
                                    root_weapon_faction=dockable.WEAPON_FACTION,
                                    root_misc_equip_type=dockable.get_equip_type(),
                                ),
                            )
                        )
                    if dockable.IS_BASE and dockable.have_shipdealer():
                        self.ship_dealers.append(
                            Market(
                                base_nickname=dockable.get_base_nickname(),
                                items=dockable.SHIP_SET.get_ships(
                                    core=self.core,
                                ),
                            )
                        )

                    if dockable.have_trader():
                        system.add_base(dockable)

    def load_system_trade_connections(self):
        for the_system in self.universe_root.get_systems():
            the_system.load_trade_connections()

    def load_interiors(self):
        for the_system in self.universe_root.get_systems():
            if the_system.have_dynamic_content():
                interior_definitions, interior_files, mbases_content = the_system.get_interiors_data()
                self.interior_definitions += interior_definitions
                self.interior_files.update(interior_files)
                self.mbases_content += mbases_content

    def get_market_equip(self):
        return DIVIDER.join([dealer.get_market_content() for dealer in self.equip_dealers])

    def get_market_ships(self):
        return DIVIDER.join([dealer.get_market_content() for dealer in self.ship_dealers])

    def get_market_commodities(self):
        return DIVIDER.join([base.get_commodity_market().get_market_content() for base in self.bases_list])

    def get_bases_store_debug_info(self):
        return DIVIDER.join([base.get_debug_table() for base in self.bases_list])

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
        # return ';blank'
        # Remove key good to keep keys silent
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
