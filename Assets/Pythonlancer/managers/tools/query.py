def validate_eq(value):
    if type(value) is not list:
        raise Exception('Eq classes should be list')
    return value


class Gun:
    def __init__(self, gun, eq_classes):
        self.gun = gun
        self.eq_classes = validate_eq(eq_classes)


class GenericGun:
    def __init__(self, generic_kind, eq_classes):
        self.generic_kind = generic_kind
        self.eq_classes = validate_eq(eq_classes)


class MiscEquip:
    def __init__(self, eq_type, eq_classes):
        self.eq_type = eq_type
        self.eq_classes = validate_eq(eq_classes)


class Engine(MiscEquip):
    pass


class Power(MiscEquip):
    pass


class Shield(MiscEquip):
    pass


class Thruster(MiscEquip):
    pass


class Ship:
    def __init__(self, ship):
        self.eq_type = eq_type
        self.eq_classes = validate_eq(eq_classes)
