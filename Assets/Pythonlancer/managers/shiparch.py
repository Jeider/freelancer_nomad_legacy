from world.ship import *
from templates.shiparch import ShiparchTemplate


class ShiparchManager(object):
    SHIPS = [
        Dagger,
        Banshee,
        Stiletto,
        Sabre,
        Valkyrie,
        ValkyrieMk2,
        Humpback,

        Piranha,
        Patriot,
        Barracuda,
        Hammerhead,
        Defender,
        DefenderJuni,
        Rhino,

        Legionnaire,
        Cavalier,
        Centurion,
        Titan,
        Crusader,
        CrusaderMk2,
        Clydesdale,

        Hawk,
        Drake,
        Falcon,
        Eagle,
        Dragon,
        DragonMk2,
        Dron,

        Bloodhound,
        Wolfhound,
        Anubis,
        Mule,

        Dromader,
        CSV,
        Armored,
        Starflier,

        Startracker,
        Starblazer,
    ]

    def __init__(self):
        self.params = {}
        self.ships = []

        for ship in self.SHIPS:
            instance = ship()
            self.params.update(instance.get_shiparch_params())
            self.ships.append(instance)

    def get_file_content(self):
        return ShiparchTemplate().format(self.params)


