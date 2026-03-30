from world.ship import Ship
from world.capital import Capital
from text.dividers import DIVIDER

from world.simples import *

from tools.data_folder import DataFolder

SHIPARCH_TEMPLATE = 'hardcoded_inis/static_content/shiparch.ini'
FUSE_GEN_CAPITAL = 'fuse_gen_capital'

SHIPARCH2_TEMPLATE = 'hardcoded_inis/shiparch/shiparch2.ini'
PLAYERSHIPS_TEMPLATE_FORMAT = 'hardcoded_inis/shiparch/playerships/{archetype}.ini'
CAPSHIPS_TEMPLATE_FORMAT = 'hardcoded_inis/shiparch/capships/{archetype}.ini'


class ShiparchManager:
    def __init__(self, lancer_core):
        self.core = lancer_core
        self.misc_equip = self.core.misc_equip
        self.ids = self.core.ids.ship_dbg

        self.params = {}
        self.ships = []
        self.ships_db = {}
        self.capitals = []
        self.capitals_db = {}

        self.shiparch_context = {}
        self.shiparch_loaded = False

        for ship in Ship.subclasses:
            if ship.VISUAL != VIS_DEFAULT:
                print(f"{ship} skipped in shiparch v1")
                continue

            instance = ship(self.ids)
            self.shiparch_context[ship.TEMPLATE_CODE] = instance
            self.ships.append(instance)
            self.ships_db[instance.ARCHETYPE] = instance

        for capital in Capital.subclasses:
            if capital.is_skip_v1():
                print(f"{capital} skipped in shiparch v1")
                continue

            instance = capital(self.ids)
            self.shiparch_context[capital.TEMPLATE_CODE] = instance
            self.capitals.append(instance)
            self.capitals_db[instance.ARCHETYPE] = instance

        self.sync_data()

    def get_ship_by_class(self, ship_class):
        return self.ships_db[ship_class.ARCHETYPE]

    def get_ship_by_archetype(self, archetype):
        return self.ships_db[archetype]

    def validate_shiparch(self):
        for ship in self.ships:
            if not ship.is_used():
                raise Exception(f'ship {ship} is not used')

    def get_shiparch_content(self):
        shiparch = self.core.tpl_manager.get_result(SHIPARCH_TEMPLATE, self.shiparch_context)
        self.validate_shiparch()
        self.shiparch_loaded = True
        return shiparch

    def get_ship_goods(self):
        data = []

        for ship in self.ships:
            shipclass = ship.EQUIPMENT_SHIPCLASS
            equip_type = ship.PACKAGE_EQUIPMENT_TYPE
            equipment_class = ship.get_package_equipment_class()

            engine = self.misc_equip.get_engine(shipclass, equip_type, equipment_class).get_nickname()
            power = self.misc_equip.get_powerplant(shipclass, equip_type, equipment_class).get_nickname()
            shield = self.misc_equip.get_shield(shipclass, equip_type, equipment_class).get_nickname()

            data.append(ship.get_hull())
            data.append(ship.get_package(shield, engine, power, ship.PACKAGE_LIGHT))

        return DIVIDER.join(data)

    def get_fuses(self):
        fuses = []
        for capital in self.capitals:
            fuses.append(capital.get_part_fuses_definitions())
        return DIVIDER.join(fuses)

    def sync_data(self):
        if not self.core.write:
            return
        data_folder = DataFolder(build_to_folder=self.core.build_folder)
        data_folder.sync_shiparch(self.get_shiparch_content())
        data_folder.sync_fuse(FUSE_GEN_CAPITAL, self.get_fuses())


class SimplesStorage:
    TEMPLATE_FORMAT = 'hardcoded_inis/shiparch/simples/{storage}.ini'
    TEMPLATE = None
    VISUALS = []

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)
    def __init__(self, tpl_manager):
        self.tpl_manager = tpl_manager

    def get_template_name(self):
        if self.TEMPLATE is None:
            raise Exception(f"{self} have no template")
        return self.TEMPLATE

    def get_template(self):
        return self.TEMPLATE_FORMAT.format(storage=self.get_template_name())

    def get_visuals(self):
        if len(self.VISUALS) == 0:
            raise Exception(f"{self} have no template")
        return self.VISUALS

    def get_content(self):
        template = self.get_template()
        content = []
        for visual in self.get_visuals():
            context = {
                'prefix': PREFIX_PER_VIS[visual],
            }
            content.append(
                self.tpl_manager.get_result(template, context)
            )
        return DIVIDER.join(content)


class GenericSimples(SimplesStorage):
    TEMPLATE = 'generic'
    VISUALS = [VIS_DEFAULT]  # just run it once


class MainSimples(SimplesStorage):
    TEMPLATE = 'pir_nmd'
    VISUALS = [VIS_DEFAULT, VIS_PIRATE, VIS_NOMAD]


class MainAndJackSimples(SimplesStorage):
    TEMPLATE = 'pir_nmd_jack'
    VISUALS = [VIS_DEFAULT, VIS_PIRATE, VIS_NOMAD, VIS_JACK_RAZOR]


class ShiparchManagerV2:
    def __init__(self, lancer_core):
        self.core = lancer_core
        self.misc_equip = self.core.misc_equip
        self.ids = self.core.ids.ship

        self.params = {}
        self.ships = []
        self.ships_db = {}
        self.capitals = []
        self.capitals_db = {}
        self.shiparch_loaded = False

        playerships_content = []
        for ship in Ship.subclasses:
            instance = ship(self.ids)
            self.ships.append(instance)
            self.ships_db[instance.get_archetype()] = instance

            template = PLAYERSHIPS_TEMPLATE_FORMAT.format(archetype=instance.get_clean_archetype())
            playerships_content.append(
                self.core.tpl_manager.get_result(template, {
                    'prefix': instance.get_visual_prefix(),
                    instance.TEMPLATE_CODE: instance,
                })
            )


        capships_content = []
        for capital in Capital.subclasses:
            instance = capital(self.ids)
            self.capitals.append(instance)
            self.capitals_db[instance.get_archetype()] = instance

            template = CAPSHIPS_TEMPLATE_FORMAT.format(archetype=instance.get_clean_archetype())
            capships_content.append(
                self.core.tpl_manager.get_result(template, {
                    'prefix': instance.get_visual_prefix(),
                    instance.TEMPLATE_CODE: instance,
                })
            )

        self.shiparch_context = {
            'simples_pir_nmd': MainSimples(self.core.tpl_manager).get_content(),
            'simples_generic': GenericSimples(self.core.tpl_manager).get_content(),
            'simples_pir_nmd_jack': MainAndJackSimples(self.core.tpl_manager).get_content(),
            'playerships': DIVIDER.join(playerships_content),
            'capships': DIVIDER.join(capships_content),
        }

        self.sync_data()

    def get_ship_by_class(self, ship_class):
        return self.ships_db[ship_class.ARCHETYPE]

    def get_ship_by_archetype(self, archetype):
        return self.ships_db[archetype]

    def validate_shiparch(self):
        for ship in self.ships:
            if not ship.is_used():
                raise Exception(f'ship {ship} is not used')

    def get_shiparch_content(self):
        shiparch = self.core.tpl_manager.get_result(SHIPARCH2_TEMPLATE, self.shiparch_context)
        self.validate_shiparch()
        self.shiparch_loaded = True
        return shiparch

    def get_ship_goods(self):
        data = []

        for ship in self.ships:
            shipclass = ship.EQUIPMENT_SHIPCLASS
            equip_type = ship.PACKAGE_EQUIPMENT_TYPE
            equipment_class = ship.get_package_equipment_class()

            engine = self.misc_equip.get_engine(shipclass, equip_type, equipment_class).get_nickname()
            power = self.misc_equip.get_powerplant(shipclass, equip_type, equipment_class).get_nickname()
            shield = self.misc_equip.get_shield(shipclass, equip_type, equipment_class).get_nickname()

            data.append(ship.get_hull())
            data.append(ship.get_package(shield, engine, power, ship.PACKAGE_LIGHT))

        return DIVIDER.join(data)

    def get_fuses(self):
        fuses = []
        for capital in self.capitals:
            fuses.append(capital.get_part_fuses_definitions())
        return DIVIDER.join(fuses)

    def sync_data(self):
        if not self.core.write:
            return
        data_folder = DataFolder(build_to_folder=self.core.build_folder)
        data_folder.sync_shiparch_alt(self.get_shiparch_content())  # Temporary!
        # data_folder.sync_fuse(FUSE_GEN_CAPITAL, self.get_fuses())
