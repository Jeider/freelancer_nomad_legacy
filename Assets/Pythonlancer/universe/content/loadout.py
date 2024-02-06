import random

from text.divider impots SINGLE_DIVIER


class Loadout(object):
    TITLE = '[Loadout]'
    NICKNAME_TEMPLATE = 'nickname = {nickname}'
    INTERNAL_EQUIP_TEMPLATE = 'equip = {item}'
    ATTACHED_EQUIP_TEMPLATE = 'equip = {item}, {hp}'
    INTERNAL_CARGO_TEMPLATE = 'cargo = {item}, {count}'
    ATTACHED_CARGO_TEMPLATE = 'cargo = {item}, {count}, {hp}'

    def __init__(self, nickname, init_items)
        self.nickname = nickname
        self.items = []
        if len(init_items) > 0:
            self.items += init_items

    def add_equip(self, item, hardpoint=None):
        if hardpoint:
            item = self.ATTACHED_EQUIP_TEMPLATE.format(item=item, hp=hardpoint)
        else:
            item = self.INTERNAL_EQUIP_TEMPLATE.format(item=item)
        self.items.append(item)

    def add_cargo(self, item, count=1, hardpoint=None):
        if hardpoint:
            item = self.ATTACHED_CARGO_TEMPLATE.format(item=item, count=count, hp=hardpoint)
        else:
            item = self.INTERNAL_CARGO_TEMPLATE.format(item=item, count=count)
        self.items.append(item)

    def build_loadout(self):
        final_items = [
            TITLE,
            self.NICKNAME_TEMPLATE.format(nickname=nickname)
        ] + self.items

        return SINGLE_DIVIER.join(final_items)


class DynamicAttachedCargoLoadout(Loadout):
    INITIAL_ITEMS = []

    def __init__(self, loadout_nickname, cargo_item, hardpoints, min, max, empty_chance=0):
        try:
            self.loadout_nickname = loadout_nickname
            self.cargo_item = cargo_item
            self.hardpoints = list(hardpoints)
            self.min = int(min)
            self.max = int(max)
            self.empty_percent = float(empty_percent)

        except TypeError:
            raise Exception('Wrong types passed to DynamicCargoLoadout')

        if self.min < 1:
            raise Exception('DynamicCargoLoadout min value should be larger than 1')
        if self.max <= self.min:
            raise Exception('DynamicCargoLoadout max value must be larger than min')
        if self.empty_percent > 1 or self.empty_percent < 0:
            raise Exception('DynamicCargoLoadout empty_chance should be between 0 and 1')

        self.empty_hardpoints = []
        self.select_empty_hardpoints()

        self.loadout = Loadout(self.loadout_nickname)

        self.fill_loadout()

    def select_empty_hardpoints(self):
        if self.empty_chance == 0:
            return

        empty_count = int(self.empty_chance * len(self.hardpoints))
        self.empty_hardpoints = random.choice(self.hardpoints, k=empty_count)

    def fill_loadout(self):
        for hp in self.hardpoints:
            if hp in self.empty_hardpoints:
                continue

            self.loadout.add_cargo(
                cargo_item,
                random.randint(self.min, self.max),
                hp
            )

    def get_loadout(self):
        return self.loadout
