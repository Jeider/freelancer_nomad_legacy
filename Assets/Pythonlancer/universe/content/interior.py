from text.dividers import DIVIDER

ROOM_FOLDER_RH = 'RH'
ROOM_FOLDER_LI = 'LI'
ROOM_FOLDER_BR = 'BR'
ROOM_FOLDER_KU = 'KU'
ROOM_FOLDER_CO = 'CO'

BAR = 'Bar'
DECK = 'Deck'
SHIPDEALER = 'ShipDealer'

ROOM_BATTLESHIP_DECK = 'battleship_deck'
ROOM_BATTLESHIP_NOSHIP_DECK = 'battleship_noship_deck'  # deck without shipdealer
ROOM_BATTLESHIP_BAR = 'battleship_bar'
ROOM_BATTLESHIP_BAR_MSN = 'battleship_bar_mil'
ROOM_BATTLESHIP_BAR_ALONE = 'battleship_bar_alone'  # bar without shipdealer
ROOM_BATTLESHIP_BAR_ALONE_MSN = 'battleship_bar_alone_mil'  # bar without shipdealer

ROOM_OUTPOST_DECK = 'outpost_deck'
ROOM_OUTPOST_BAR = 'outpost_bar'
ROOM_OUTPOST_BAR_MSN = 'outpost_bar_mil'

ROOM_OUTPOST_SHIP_DECK = 'outpost_ship_deck'
ROOM_OUTPOST_SHIP_BAR = 'outpost_ship_bar'
ROOM_OUTPOST_SHIP_BAR_MSN = 'outpost_ship_bar_mil'
ROOM_OUTPOST_SHIPDEALER = 'outpost_shipdealer'

ROOM_STATION_DECK = 'station_deck'
ROOM_STATION_BAR = 'station_bar'
ROOM_STATION_BAR_MSN = 'station_bar_mil'

ROOM_STATION_SHIP_DECK = 'station_ship_deck'
ROOM_STATION_SHIP_BAR = 'station_ship_bar'
ROOM_STATION_SHIP_BAR_MSN = 'station_ship_bar_mil'
ROOM_STATION_SHIPDEALER = 'station_shipdealer'

EQUIP_DEPOT_DECK = 'equip_depot_deck'

BASE_INFO_TEMPLATE = '''[BaseInfo]
nickname = {base_nickname}
start_room = {start_room}'''

ROOM_TEMPLATE = '''[Room]
nickname = {room_name}
file = {destination}'''

DEFAULT_DESTINATION_TEMLATE = 'UNIVERSE\\ROOM\\{room_subfolder}\\{room_file}.ini'
OVERRIDED_DESTINATION_TEMLATE = 'UNIVERSE\\{systems_folder}\\{system_folder}\\ROOM\\{room_file}.ini'

MBASE_ROOT_TEMPLATE = '''[MBase]
nickname = {base_name}
local_faction = {faction}
diff = 1
msg_id_prefix = {audio_prefix}'''

MBASE_MVENDOR = '''[MVendor]
num_offers = 8, 12'''

MBASE_MAIN_FACTION_TEMPLATE = '''[BaseFaction]
faction = {faction}
weight = 90
offers_missions = true
mission_type = DestroyMission, 0.000000, 0.112387, 100'''

MBASE_MAIN_FACTION_TEMPLATE_NO_MISSION = '''[BaseFaction]
faction = {faction}
weight = 90
offers_missions = false'''

MBASE_SECOND_FACTION_TEMPLATE = '''[BaseFaction]
faction = {faction}
weight = 1
offers_missions = false'''

ALL_ON_DECK_DEALERS_TEMPLATE = '''[MRoom]
nickname = Deck
character_density = 3
fixture = {trader}, Zs/NPC/Trader/01/A/Stand, scripts\\vendors\\li_commtrader_fidget.thn, trader
fixture = {equip}, Zs/NPC/Equipment/01/A/Stand, scripts\\vendors\\li_equipdealer_fidget.thn, Equipment
fixture = {shipdealer}, Zs/NPC/Shipdealer/01/A/Stand, scripts\\vendors\\li_shipdealer_fidget.thn, ShipDealer'''

DECK_DEALERS_TEMPLATE = '''[MRoom]
nickname = Deck
character_density = 2
fixture = {trader}, Zs/NPC/Trader/01/A/Stand, scripts\\vendors\\li_commtrader_fidget.thn, trader
fixture = {equip}, Zs/NPC/Equipment/01/A/Stand, scripts\\vendors\\li_equipdealer_fidget.thn, Equipment

[MRoom]
nickname = ShipDealer
character_density = 1
fixture = {shipdealer}, Zs/NPC/Shipdealer/01/A/Stand, scripts\\vendors\\li_shipdealer_fidget.thn, ShipDealer'''

DECK_DEALERS_ONLY_TEMPLATE = '''[MRoom]
nickname = Deck
character_density = 2
fixture = {trader}, Zs/NPC/Trader/01/A/Stand, scripts\\vendors\\li_commtrader_fidget.thn, trader
fixture = {equip}, Zs/NPC/Equipment/01/A/Stand, scripts\\vendors\\li_equipdealer_fidget.thn, Equipment'''

SINGLE_CHAR_DEALERS_TEMPLATE = '''[MRoom]
nickname = Equipment
character_density = 1
fixture = {equip}, Zs/NPC/Equipment/01/A/Stand, scripts\\vendors\\li_equipdealer_fidget.thn, Equipment

[MRoom]
nickname = trader
character_density = 1
fixture = {trader}, Zs/NPC/Trader/01/A/Stand, scripts\\vendors\\li_commtrader_fidget.thn, trader

[MRoom]
nickname = ShipDealer
character_density = 1
fixture = {shipdealer}, Zs/NPC/Shipdealer/01/A/Stand, scripts\\vendors\\li_shipdealer_fidget.thn, ShipDealer'''

EQUIPDEALER_NAME_TEMPLATE = '{base_name}_fix_equipdealer'
COMMTRADER_NAME_TEMPLATE = '{base_name}_fix_commtrader'
SHIPDEALER_NAME_TEMPLATE = '{base_name}_fix_shipdealer'

INTERIOR_BG_CROW = 'crow_exclusion'
INTERIOR_BG_BARRIER_CLOUD = 'exclusion_barrier_m7'
INTERIOR_BH_BIZMARK = 'rh_biz_nebula'


class Interior(object):
    START_ROOM = None
    ROOMS = {}
    PIRATE_BAR = False
    CUSTOM_INTERIOR_FILE = False
    DEALER_PLACEMENTS_TEMPLATE = None
    OFFER_MISSIONS = True

    def __init__(self, base_instance, room_subfolder):
        self.base_instance = base_instance
        self.base_nickname = self.base_instance.get_base_nickname()
        self.room_subfolder = room_subfolder

        if not self.CUSTOM_INTERIOR_FILE and not self.room_subfolder:
            raise Exception('room subfolder not defined for %s' % self.__class__.__name__)

    def get_mbase(self):
        entries = []

        base_name = self.base_instance.get_base_nickname()

        entries.append(
            MBASE_ROOT_TEMPLATE.format(
                base_name=base_name,
                faction=self.base_instance.get_faction(),
                audio_prefix=self.base_instance.get_audio_prefix(),
            )
        )

        if self.OFFER_MISSIONS:
            entries.append(MBASE_MVENDOR)
            entries.append(
                MBASE_MAIN_FACTION_TEMPLATE.format(
                    faction=self.base_instance.FACTION,
                )
            )
        else:
            entries.append(
                MBASE_MAIN_FACTION_TEMPLATE_NO_MISSION.format(
                    faction=self.base_instance.FACTION,
                )
            )

        second_factions = self.get_second_factions()

        for faction in second_factions:
            entries.append(
                MBASE_SECOND_FACTION_TEMPLATE.format(faction=faction)
            )

        if self.base_instance.DEALERS:

            if not self.DEALER_PLACEMENTS_TEMPLATE:
                raise Exception('unknown dealers template of interior for base %s' % self.base_instance.__class__.__name__)

            equipdealer_name = EQUIPDEALER_NAME_TEMPLATE.format(base_name=base_name)
            commtrader_name = COMMTRADER_NAME_TEMPLATE.format(base_name=base_name)
            shipdealer_name = SHIPDEALER_NAME_TEMPLATE.format(base_name=base_name)

            entries.append(self.base_instance.DEALERS.get_equip(equipdealer_name))
            entries.append(self.base_instance.DEALERS.get_trader(commtrader_name))
            entries.append(self.base_instance.DEALERS.get_shipdealer(shipdealer_name))

            entries.append(
                self.DEALER_PLACEMENTS_TEMPLATE.format(
                    equip=equipdealer_name,
                    trader=commtrader_name,
                    shipdealer=shipdealer_name,
                )
            )

        return DIVIDER.join(entries)

    def get_second_factions(self):
        is_lawful = self.base_instance.is_lawful()
        init_factions_list = self.base_instance.system.LAWFUL_FACTIONS if is_lawful else self.base_instance.system.UNLAWFUL_FACTIONS
        factions_list = init_factions_list.copy()
        factions_list.remove(self.base_instance.FACTION)
        return factions_list


class CustomFileInterior(Interior):
    CUSTOM_INTERIOR_FILE = True
    HAVE_BAR = False
    HAVE_EQUIP = False
    HAVE_TRADER = False
    HAVE_SHIPDEALER = False

    def have_bar(self):
        return self.HAVE_BAR

    def have_equip(self):
        return self.HAVE_EQUIP

    def have_trader(self):
        return self.HAVE_TRADER

    def have_shipdealer(self):
        return self.HAVE_SHIPDEALER


class CustomFullSingleRoomInterior(CustomFileInterior):
    CUSTOM_INTERIOR_FILE = True
    HAVE_BAR = True
    HAVE_EQUIP = True
    HAVE_TRADER = True
    HAVE_SHIPDEALER = True
    DEALER_PLACEMENTS_TEMPLATE = ALL_ON_DECK_DEALERS_TEMPLATE


class CustomFullSplitRoomInterior(CustomFileInterior):
    CUSTOM_INTERIOR_FILE = True
    HAVE_BAR = True
    HAVE_EQUIP = True
    HAVE_TRADER = True
    HAVE_SHIPDEALER = True
    DEALER_PLACEMENTS_TEMPLATE = SINGLE_CHAR_DEALERS_TEMPLATE


class GenericInterior(Interior):
    def get_base_info(self):
        if self.CUSTOM_INTERIOR_FILE:
            raise Exception('This base interior marker as custom %s' % self.base_instance.__class__.__name__)

        items = [
            BASE_INFO_TEMPLATE.format(
                base_nickname=self.base_nickname,
                start_room=self.START_ROOM,
            )
        ]
        for room_name, room_file in self.ROOMS.items():
            room_subfolder = self.room_subfolder
            if room_name == BAR and self.PIRATE_BAR:
                room_subfolder = ROOM_FOLDER_CO

            items.append(
                ROOM_TEMPLATE.format(
                    room_name=room_name,
                    destination=DEFAULT_DESTINATION_TEMLATE.format(
                        room_subfolder=room_subfolder,
                        room_file=room_file
                    )
                )
            )

        return DIVIDER.join(items)

    def have_bar(self):
        return BAR in self.ROOMS

    def have_equip(self):
        # TODO: custom decks?
        return DECK in self.ROOMS

    def have_trader(self):
        # TODO: custom decks?
        return DECK in self.ROOMS

    def have_shipdealer(self):
        return SHIPDEALER in self.ROOMS


class BattleshipInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_BATTLESHIP_DECK,
        BAR: ROOM_BATTLESHIP_BAR_MSN,
    }
    DEALER_PLACEMENTS_TEMPLATE = ALL_ON_DECK_DEALERS_TEMPLATE


class BattleshipNoshipInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_BATTLESHIP_NOSHIP_DECK,
        BAR: ROOM_BATTLESHIP_BAR_ALONE_MSN,
    }
    DEALER_PLACEMENTS_TEMPLATE = DECK_DEALERS_ONLY_TEMPLATE


class OutpostInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_OUTPOST_DECK,
        BAR: ROOM_OUTPOST_BAR_MSN,
    }
    DEALER_PLACEMENTS_TEMPLATE = DECK_DEALERS_TEMPLATE


class OutpostShipdealerInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_OUTPOST_SHIP_DECK,
        BAR: ROOM_OUTPOST_SHIP_BAR_MSN,
        SHIPDEALER: ROOM_OUTPOST_SHIPDEALER,
    }
    DEALER_PLACEMENTS_TEMPLATE = DECK_DEALERS_TEMPLATE


class StationInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_STATION_DECK,
        BAR: ROOM_STATION_BAR_MSN,
    }
    DEALER_PLACEMENTS_TEMPLATE = DECK_DEALERS_TEMPLATE


class StationShipdealerInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_STATION_SHIP_DECK,
        BAR: ROOM_STATION_SHIP_BAR_MSN,
        SHIPDEALER: ROOM_STATION_SHIPDEALER,
    }
    DEALER_PLACEMENTS_TEMPLATE = DECK_DEALERS_TEMPLATE


class StationBshbarInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_STATION_DECK,
        BAR: ROOM_BATTLESHIP_BAR_ALONE_MSN,
    }
    DEALER_PLACEMENTS_TEMPLATE = DECK_DEALERS_TEMPLATE


class StationShipdealerBshbarInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_STATION_SHIP_DECK,
        BAR: ROOM_BATTLESHIP_BAR_MSN,
        SHIPDEALER: ROOM_STATION_SHIPDEALER,
    }
    DEALER_PLACEMENTS_TEMPLATE = DECK_DEALERS_TEMPLATE


class PirateBar(object):
    PIRATE_BAR = True


class PirateOutpostInterior(PirateBar, OutpostInterior):
    pass


class PirateOutpostShipdealerInterior(PirateBar, OutpostShipdealerInterior):
    pass


class PirateStationInterior(PirateBar, StationInterior):
    ROOMS = {
        DECK: ROOM_STATION_DECK,
        BAR: ROOM_OUTPOST_BAR_MSN,
    }


class PirateStationShipdealerInterior(PirateBar, StationShipdealerInterior):
    ROOMS = {
        DECK: ROOM_STATION_SHIP_DECK,
        BAR: ROOM_OUTPOST_SHIP_BAR_MSN,
        SHIPDEALER: ROOM_STATION_SHIPDEALER,
    }


class EquipDeckInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: EQUIP_DEPOT_DECK,
    }