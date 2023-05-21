from world.equipment import Equipment, MainMiscEquip
from world.power import Power
from world.engine import Engine
from world.shield import Shield, ShieldNPC
from world.thruster import Thruster


def main():
    engines = []
    powerplants = []
    shields = []
    npc_shields = []
    thrusters = []

    for equip_type in MainMiscEquip.ALL_EQUIP_TYPES:
        for equipment_class in Equipment.BASE_CLASSES:
            for shipclass in Equipment.SHIPCLASSES:
                engine = Engine(equip_type, shipclass, equipment_class, 500, 200)
                engines.append(engine)


                power = Power(equip_type, shipclass, equipment_class, 500, 200)
                powerplants.append(power)

                shield = Shield(equip_type, shipclass, equipment_class, 500, 200)
                shields.append(shield)

                npc_shield = ShieldNPC(equip_type, shipclass, equipment_class, 500, 200)
                npc_shields.append(npc_shield)

            thruster = Thruster(equip_type, equipment_class, 500, 200)
            thrusters.append(thruster)

    import ipdb
    ipdb.set_trace()

main()




# print(engine.get_good())
# print('')

