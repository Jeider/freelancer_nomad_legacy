from world.ship import Ship
from templates.shiparch import ShiparchTemplate


class ShiparchManager(object):

    def __init__(self):
        self.params = {}
        self.ships = []

        for ship in Ship.subclasses:
            instance = ship()
            self.params.update(instance.get_shiparch_params())
            self.ships.append(instance)

    def get_file_content(self):
        return ShiparchTemplate().format(self.params)


