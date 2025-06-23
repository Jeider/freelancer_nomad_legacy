import random

from text.dividers import SINGLE_DIVIDER


class Loadout(object):
    TITLE = '[Loadout]'
    NICKNAME_TEMPLATE = 'nickname = {nickname}'
    INTERNAL_EQUIP_TEMPLATE = 'equip = {item}'
    ATTACHED_EQUIP_TEMPLATE = 'equip = {item}, {hp}'
    INTERNAL_CARGO_TEMPLATE = 'cargo = {item}, {count}'
    ATTACHED_CARGO_TEMPLATE = 'cargo = {item}, {count}, {hp}'

    def __init__(self, loadout_nickname, init_items=None):
        self.loadout_nickname = loadout_nickname
        self.items = []
        if init_items is not None and len(init_items) > 0:
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
            self.TITLE,
            self.NICKNAME_TEMPLATE.format(nickname=self.loadout_nickname)
        ] + self.items

        return SINGLE_DIVIDER.join(final_items)

    def get_loadout_nickname(self):
        return self.loadout_nickname

    def get_loadout(self):
        return self.loadout


class DynamicAttachedCargoLoadout(Loadout):
    def __init__(self, loadout_nickname, cargo_item, hardpoints, min, max, empty_chance=0, init_items=None):
        try:
            self.loadout_nickname = loadout_nickname
            self.cargo_item = cargo_item
            self.hardpoints = list(hardpoints)
            self.min = int(min)
            self.max = int(max)
            self.empty_chance = float(empty_chance)
            self.init_items = list(init_items) if init_items and len(init_items) > 0 else None

        except TypeError:
            raise Exception('Wrong types passed to DynamicAttachedCargoLoadout')

        if self.min < 1:
            raise Exception('DynamicAttachedCargoLoadout min value should be larger than 1')
        if self.max <= self.min:
            raise Exception('DynamicAttachedCargoLoadout max value must be larger than min')
        if self.empty_chance > 1 or self.empty_chance < 0:
            raise Exception('DynamicAttachedCargoLoadout empty_chance should be between 0 and 1')

        self.empty_hardpoints = []
        self.select_empty_hardpoints()

        self.loadout = Loadout(self.loadout_nickname, init_items=init_items)

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
                self.cargo_item,
                random.randint(self.min, self.max),
                hp
            )


class DynamicInternalCargoLoadout(Loadout):
    def __init__(self, loadout_nickname, cargo_item, min, max, init_items=None):
        try:
            self.loadout_nickname = loadout_nickname
            self.cargo_item = cargo_item
            self.min = int(min)
            self.max = int(max)
            self.init_items = list(init_items) if init_items and len(init_items) > 0 else None

        except TypeError:
            raise Exception('Wrong types passed to DynamicInternalCargoLoadout')

        if self.min < 1:
            raise Exception('DynamicInternalCargoLoadout min value should be larger than 1')
        if self.max <= self.min:
            raise Exception('DynamicInternalCargoLoadout max value must be larger than min')

        self.loadout = Loadout(self.loadout_nickname, init_items=init_items)

        self.fill_loadout()

    def fill_loadout(self):
        self.loadout.add_cargo(
            self.cargo_item,
            random.randint(self.min, self.max),
        )


class SingleInternalCargoLoadout(Loadout):
    def __init__(self, loadout_nickname, cargo_item, init_items=None):
        try:
            self.loadout_nickname = loadout_nickname
            self.cargo_item = cargo_item
            self.init_items = list(init_items) if init_items and len(init_items) > 0 else None

        except TypeError:
            raise Exception('Wrong types passed to DynamicInternalCargoLoadout')

        self.loadout = Loadout(self.loadout_nickname, init_items=init_items)

        self.fill_loadout()

    def fill_loadout(self):
        self.loadout.add_cargo(
            self.cargo_item,
            1,
        )


class SingleAttachedItemLoadout(Loadout):
    def __init__(self, loadout_nickname, equip_item, hardpoint, init_items=None):
        try:
            self.loadout_nickname = loadout_nickname
            self.equip_item = equip_item
            self.hardpoint = hardpoint
            self.init_items = list(init_items) if init_items and len(init_items) > 0 else None

        except TypeError:
            raise Exception('Wrong types passed to DynamicInternalCargoLoadout')

        self.loadout = Loadout(self.loadout_nickname, init_items=init_items)

        self.fill_loadout()

    def fill_loadout(self):
        self.loadout.add_cargo(
            self.equip_item,
            1,
        )
        self.loadout.add_equip(
            'key_marker',
            self.hardpoint,
        )
