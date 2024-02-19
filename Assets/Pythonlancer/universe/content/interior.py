from text.dividers import DIVIDER

INTERIOR_FOLDER_RH = 'RH'
INTERIOR_FOLDER_LI = 'LI'
INTERIOR_FOLDER_BR = 'BR'
INTERIOR_FOLDER_KU = 'KU'
INTERIOR_FOLDER_CO = 'CO'

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


class Interior(object):
    START_ROOM = None
    ROOMS = {}
    PIRATE_BAR = False
    CUSTOM_INTERIOR_FILE = False

    def __init__(self, base_instance, interior_subfolder):
        self.base_instance = base_instance
        self.base_nickname = self.base_instance.get_base_nickname()
        self.interior_subfolder = interior_subfolder

        if not self.CUSTOM_INTERIOR_FILE and not self.interior_subfolder:
            raise Exception('interior subfolder not defined for %s' % self.__class__.__name__)

    def get_mbase(self):
        entries = []
        enties.append(
            MBASE_ROOT_TEMPLATE.format(
                base_name=base_instance.get_base_nickname(),
                faction=base_instance.get_faction(),
                audio_prefix=base_instance.get_audio_prefix(),
            )
        )
        return DIVIDER.join(entries)



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


class CustomMainRoomInterior(CustomFileInterior):
    CUSTOM_INTERIOR_FILE = True
    HAVE_BAR = True
    HAVE_EQUIP = True
    HAVE_TRADER = True
    HAVE_SHIPDEALER = False


class CustomFullRoomInterior(CustomFileInterior):
    CUSTOM_INTERIOR_FILE = True
    HAVE_BAR = True
    HAVE_EQUIP = True
    HAVE_TRADER = True
    HAVE_SHIPDEALER = True


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
            room_subfolder = self.interior_subfolder
            if room_name == BAR and self.PIRATE_BAR:
                room_subfolder = INTERIOR_FOLDER_CO

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


class BattleshipNoshipInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_BATTLESHIP_NOSHIP_DECK,
        BAR: ROOM_BATTLESHIP_BAR_ALONE_MSN,
    }


class OutpostInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_OUTPOST_DECK,
        BAR: ROOM_OUTPOST_BAR_MSN,
    }


class OutpostShipdealerInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_OUTPOST_SHIP_DECK,
        BAR: ROOM_OUTPOST_SHIP_BAR_MSN,
        SHIPDEALER: ROOM_OUTPOST_SHIPDEALER,
    }


class StationInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_STATION_DECK,
        BAR: ROOM_STATION_BAR_MSN,
    }


class StationShipdealerInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_STATION_SHIP_DECK,
        BAR: ROOM_STATION_SHIP_BAR_MSN,
        SHIPDEALER: ROOM_STATION_SHIPDEALER,
    }


class StationBshbarInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_STATION_DECK,
        BAR: ROOM_BATTLESHIP_BAR_ALONE_MSN,
    }


class StationShipdealerBshbarInterior(GenericInterior):
    START_ROOM = DECK
    ROOMS = {
        DECK: ROOM_STATION_SHIP_DECK,
        BAR: ROOM_BATTLESHIP_BAR_MSN,
        SHIPDEALER: ROOM_STATION_SHIPDEALER,
    }


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
