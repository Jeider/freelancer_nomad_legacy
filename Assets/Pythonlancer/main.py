from world.equipment import Equipment, MainMiscEquip
from world.engine import Engine


def main():
    engines = []

    for equip_type in MainMiscEquip.ALL_EQUIP_TYPES:
        for shipclass in Equipment.SHIPCLASSES:
            for equipment_class in Equipment.BASE_CLASSES:
                engine = Engine(equip_type, shipclass, equipment_class, 500, 200)
                engines.append(engine)

                print(engine.get_good())
                print('')

    # import ipdb
    # ipdb.set_trace()

main()




