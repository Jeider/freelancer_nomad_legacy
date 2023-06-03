from world.weapon import Gun


class WeaponManager(object):
    RH_LIGHTGUN = 'rh_lightgun'
    RH_HEAVYGUN = 'rh_heavygun'
    RH_CIVGUN = 'rh_civgun'
    RH_HUNTERGUN = 'rh_huntergun'
    RH_SHIELDGUN = 'rh_shieldgun'
    RH_PIRATEGUN = 'rh_pirategun'
    RH_HESSIANGUN = 'rh_heassiangun'
    RH_JUNKERGUN = 'rh_junkergun'

    GUNS = [
        {
            'base_nickname': WeaponManager.RH_LIGHTGUN,
            'model': Gun.RH_GAMMA_BEAMER,
            'equip_type': Gun.EQUIP_MAIN,
            'refire_rate': Gun.REFIRE_RATE_6,
            'muzzle_velocity': 700,
            'lifetime': 1.0,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': WeaponManager.RH_HEAVYGUN,
            'model': Gun.RH_PROTON_BLASTER,
            'equip_type': Gun.EQUIP_MAIN,
            'refire_rate': Gun.REFIRE_RATE_2,
            'muzzle_velocity': 500,
            'lifetime': 1.2,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': WeaponManager.RH_CIVGUN,
            'model': Gun.GE_SHREDDER_SHOTGUN,
            'equip_type': Gun.EQUIP_CIV,
            'refire_rate': Gun.REFIRE_RATE_4,
            'muzzle_velocity': 600,
            'lifetime': 0.8,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': WeaponManager.RH_HUNTERGUN,
            'model': Gun.GE_SHREDDER_SHOTGUN,
            'equip_type': Gun.EQUIP_PIRATE,
            'refire_rate': Gun.REFIRE_RATE_8,
            'muzzle_velocity': 750,
            'lifetime': 0.8,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': WeaponManager.RH_SHIELDGUN,
            'model': Gun.RH_PROTON_BLASTER,
            'equip_type': Gun.EQUIP_MAIN,
            'refire_rate': Gun.REFIRE_RATE_4,
            'muzzle_velocity': 600,
            'lifetime': 1.0,
            'ids_name': 1,
            'ids_info': 1,
            'shieldgun': True,
        },
        {
            'base_nickname': WeaponManager.RH_PIRATEGUN,
            'model': Gun.CO_RAILDADDY,
            'equip_type': Gun.EQUIP_CIV,
            'refire_rate': Gun.REFIRE_RATE_8,
            'muzzle_velocity': 750,
            'lifetime': 0.8,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': WeaponManager.RH_HESSIANGUN,
            'model': Gun.RH_GAMMA_BEAMER,
            'equip_type': Gun.EQUIP_PIRATE,
            'refire_rate': Gun.REFIRE_RATE_6,
            'muzzle_velocity': 700,
            'lifetime': 1,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': WeaponManager.RH_JUNKERGUN,
            'model': Gun.CO_RAILDADDY,
            'equip_type': Gun.EQUIP_PIRATE,
            'refire_rate': Gun.REFIRE_RATE_8,
            'muzzle_velocity': 600,
            'lifetime': 1,
            'ids_name': 1,
            'ids_info': 1,
        },
    ]

    def __init__(self):
        self.guns_db = {}

        self.load_game_data()

    def load_game_data():
        for gun in self.GUNS:
            for equipment_class in Equipment.BASE_CLASSES:
                self.guns_db[gun['base_nickname']][equipment_class] = Gun(equipment_class=equipment_class, faction=Equipment.FACTION_RH, **gun)

    def get_gun(self, gun_base_nickname, equipment_class):
        return self.guns_db[gun_base_nickname][equipment_class]
