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

    def add_equip(self, item, count=1, hardpoint=None):
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

 



class DynamicLoadout(object):



    '''
    [Loadout]

equip = attached_xast_exploder, HpFX01
equip = attached_xast_exploder, HpFX02
equip = attached_xast_exploder, HpFX03
equip = attached_xast_exploder, HpFX04
equip = attached_xast_exploder, HpFX05
equip = attached_xast_exploder, HpFX06
equip = attached_xast_exploder, HpFX07
equip = attached_xast_exploder, HpFX08
equip = attached_xast_exploder, HpFX09
equip = attached_xast_exploder, HpFX10