from world.equipment import Equipment, Engine

def main():
    engines = []

    for engine_type in Engine.ALL_ENGINES:
        for shipclass in Equipment.SHIPCLASSES:
            for equipment_class in Equipment.BASE_CLASSES:
                engine = Engine(engine_type, shipclass, equipment_class, 500, 200)
                engines.append(engine)

                # print(engine.get_equip())
                # print('')

    import ipdb
    ipdb.set_trace()

main()




