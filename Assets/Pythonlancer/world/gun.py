from world.equipment import DefaultGood
from world.weapon import Weapon


class Gun(Weapon, DefaultGood):
    DROP_CHANCE = 5

    RH_LIGHTGUN = 'rh_lightgun'
    RH_HEAVYGUN = 'rh_heavygun'
    RH_CIVGUN = 'rh_civgun'
    RH_HUNTERGUN = 'rh_huntergun'
    RH_SHIELDGUN = 'rh_shieldgun'
    RH_PIRATEGUN = 'rh_pirategun'
    RH_HESSIANGUN = 'rh_heassiangun'
    RH_JUNKERGUN = 'rh_junkergun'

    RH_GUNS = [
        {
            'base_nickname': RH_LIGHTGUN,
            'model': Weapon.RH_GAMMA_BEAMER,
            'equip_type': Weapon.EQUIP_MAIN,
            'refire_rate': Weapon.REFIRE_RATE_6,
            'muzzle_velocity': 700,
            'lifetime': 1.0,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': RH_HEAVYGUN,
            'model': Weapon.RH_PROTON_BLASTER,
            'equip_type': Weapon.EQUIP_MAIN,
            'refire_rate': Weapon.REFIRE_RATE_2,
            'muzzle_velocity': 500,
            'lifetime': 1.2,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': RH_CIVGUN,
            'model': Weapon.GE_SHREDDER_SHOTGUN,
            'equip_type': Weapon.EQUIP_CIV,
            'refire_rate': Weapon.REFIRE_RATE_4,
            'muzzle_velocity': 600,
            'lifetime': 0.8,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': RH_HUNTERGUN,
            'model': Weapon.GE_SHREDDER_SHOTGUN,
            'equip_type': Weapon.EQUIP_PIRATE,
            'refire_rate': Weapon.REFIRE_RATE_8,
            'muzzle_velocity': 750,
            'lifetime': 0.8,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': RH_SHIELDGUN,
            'model': Weapon.RH_PROTON_BLASTER,
            'equip_type': Weapon.EQUIP_MAIN,
            'refire_rate': Weapon.REFIRE_RATE_4,
            'muzzle_velocity': 600,
            'lifetime': 1.0,
            'ids_name': 1,
            'ids_info': 1,
            'shieldgun': True,
        },
        {
            'base_nickname': RH_PIRATEGUN,
            'model': Weapon.CO_RAILDADDY,
            'equip_type': Weapon.EQUIP_CIV,
            'refire_rate': Weapon.REFIRE_RATE_8,
            'muzzle_velocity': 750,
            'lifetime': 0.8,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': RH_HESSIANGUN,
            'model': Weapon.RH_GAMMA_BEAMER,
            'equip_type': Weapon.EQUIP_PIRATE,
            'refire_rate': Weapon.REFIRE_RATE_6,
            'muzzle_velocity': 700,
            'lifetime': 1,
            'ids_name': 1,
            'ids_info': 1,
        },
        {
            'base_nickname': RH_JUNKERGUN,
            'model': Weapon.CO_RAILDADDY,
            'equip_type': Weapon.EQUIP_PIRATE,
            'refire_rate': Weapon.REFIRE_RATE_8,
            'muzzle_velocity': 600,
            'lifetime': 1,
            'ids_name': 1,
            'ids_info': 1,
        },
    ]


    def get_price(self):
        return 100  # TODO: correct price

    def get_icon(self):
        icon = self.ICON_PER_WEAPON_MODEL[self.model]
        return Icon.get_icon_path(icon)

