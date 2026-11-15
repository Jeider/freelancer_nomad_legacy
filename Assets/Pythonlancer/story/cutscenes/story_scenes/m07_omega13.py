"""m07_omega13: постановка для ручного редактирования.

Точки: SCENES/m07_omega13.blend → DUMPS/m07_omega13.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy,
    AudioAnimEvent,
    CameraAnimEvent,
    Character,
    ConnectHardpointEvent,
    Equipment,
    Light,
    LightAnimEvent,
    LookAtCamera,
    MAIN,
    MotionEvent,
    MoveEvent,
    NeckIkEvent,
    PlayerShip,
    Prop,
    RotateAxisEvent,
    Ship,
    Solar,
    Sound,
    SoundEvent,
    SpatialSound,
    StaticCamera,
)
from story.cutscenes.anim import (
    Male,
)
from story.cutscenes.source_extensions import (
    SourceAlchemyAnimEvent,
    SourceAttachEvent,
    preserve_entity,
    preserve_spatial,
)
from story import actors


class PropPlanet1(Solar):
    COMPOUND_TEMPLATE_NAME = 'planet_mercury_5000'
    SRT_GRP = 0
    USR_FLG = 0


class PropBlackhole(Solar):
    COMPOUND_TEMPLATE_NAME = 'BlackHoleSun'
    SRT_GRP = 0
    USR_FLG = 0


class PropTheStars(Prop):
    COMPOUND_TEMPLATE_NAME = 'new_generic'
    SRT_GRP = -100
    USR_FLG = 1


class PropTheBackground(Prop):
    COMPOUND_TEMPLATE_NAME = 'om13_nebula'
    SRT_GRP = -100
    USR_FLG = 1


class PropGun01(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_mass_driver'
    SRT_GRP = 0
    USR_FLG = 0


class PropGun02(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_mass_driver'
    SRT_GRP = 0
    USR_FLG = 0


class PropLauncher01(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_slugger_launcher'
    SRT_GRP = 0
    USR_FLG = 0


class PropCockpitGun01(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_mass_driver'
    SRT_GRP = 0
    USR_FLG = 0


class PropCockpitGun02(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_mass_driver'
    SRT_GRP = 0
    USR_FLG = 0


class PropMissile01(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_slugger_missile'
    SRT_GRP = 0
    USR_FLG = 0


class PropMissile02(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_slugger_missile'
    SRT_GRP = 0
    USR_FLG = 0


class PropRockfordChair(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_pilot_chair'
    SRT_GRP = 0
    USR_FLG = 0


class PropRockfordFront(Ship):
    COMPOUND_TEMPLATE_NAME = 'ge_fighter6'
    SRT_GRP = 0
    USR_FLG = 0


class PropPlayership(Ship):
    COMPOUND_TEMPLATE_NAME = 'PlayerShip'
    SRT_GRP = 0
    USR_FLG = 0


class PropTheCockpit(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_cockpit'
    SRT_GRP = 0
    USR_FLG = 0


class PropCase(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_case'
    SRT_GRP = 0
    USR_FLG = 0


class PropPanel(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_panel'
    SRT_GRP = 0
    USR_FLG = 0


class PropCrystal(Prop):
    COMPOUND_TEMPLATE_NAME = 'Blixx_crystal'
    SRT_GRP = 0
    USR_FLG = 0


class PropTome(Prop):
    COMPOUND_TEMPLATE_NAME = 'tome_075'
    SRT_GRP = 0
    USR_FLG = 0


class PropChair(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_pilot_chair'
    SRT_GRP = 0
    USR_FLG = 0


class PropRockfordCockpit(Ship):
    COMPOUND_TEMPLATE_NAME = 'ge_fighter6'
    SRT_GRP = 0
    USR_FLG = 0



class M07Omega13Scene(Scene):
    DUMP_FILE = 'm07_omega13'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        DX_m07_omega13_0010_trent = Sound(root=self, name='DX_m07_omega13_0010_trent', sound='DX_m07_omega13_0010_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_omega13_0010_trent, userprops={'category': 'Audio'})
        DX_m07_omega13_0050b_trent = Sound(root=self, name='DX_m07_omega13_0050b_trent', sound='DX_m07_omega13_0050b_trent',
            attenuation=0, dmin=50, dmax=1000, priority=None)
        preserve_entity(DX_m07_omega13_0050b_trent, userprops={'category': 'Audio'})
        music_background = Sound(root=self, name='music_background', sound='rtc_m07_the_hitman', attenuation=-20, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(music_background, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        Light_SPACE_background = Light(root=self, name='Light_SPACE_background', point_name='Light_SPACE_background',
            extra_name='', light_group=7, diffuse=[1, 0.8823529, 0.7058824], ambient=[0.05, 0.05, 0.05],
            direction=[-1, 0, 1], light_type='L_DIRECT', on=True, range=2000, cutoff=90, theta=90, color=[255, 255, 255],
            attenuation=[1, 0, 4e-06])
        preserve_entity(Light_SPACE_background, flags='HIDDEN', lightprops={'specular': [1, 1, 1]})
        Light_SPACE_playership = Light(root=self, name='Light_SPACE_playership', point_name='Light_SPACE_playership',
            extra_name='', light_group=4, diffuse=[1, 0.8823529, 0.7058824], ambient=[0.05, 0.05, 0.05],
            direction=[-1, 0, -1], light_type='L_DIRECT', on=True, range=2000, cutoff=90, theta=90, color=[255, 255, 255],
            attenuation=[1, 0, 4e-06])
        preserve_entity(Light_SPACE_playership, flags='HIDDEN', lightprops={'specular': [1, 1, 1]})
        Light_SPACE_playership_shield_fx = Light(root=self, name='Light_SPACE_playership_shield_fx',
            point_name='Light_SPACE_playership_shield_fx', extra_name='', light_group=4, diffuse=[0, 0, 0],
            ambient=[0, 0, 0], direction=[-1, 0, -1], light_type='L_DIRECT', on=False, range=2000, cutoff=90, theta=90,
            color=[255, 255, 255], attenuation=[1, 0, 4e-06])
        preserve_entity(Light_SPACE_playership_shield_fx, flags='HIDDEN', lightprops={'specular': [1, 1, 1]})
        Light_SPACE_rockford_intro = Light(root=self, name='Light_SPACE_rockford_intro',
            point_name='Light_SPACE_rockford_intro', extra_name='', light_group=5, diffuse=[1, 0.8823529, 0.7058824],
            ambient=[0.05, 0.05, 0.05], direction=[-1, 0, -1], light_type='L_DIRECT', on=True, range=2000, cutoff=90,
            theta=90, color=[255, 255, 255], attenuation=[1, 0, 4e-06])
        preserve_entity(Light_SPACE_rockford_intro, flags='HIDDEN', lightprops={'specular': [1, 1, 1]})
        Light_SPACE_rockford_front = Light(root=self, name='Light_SPACE_rockford_front',
            point_name='Light_SPACE_rockford_front', extra_name='', light_group=5, diffuse=[1, 0.8823529, 0.7058824],
            ambient=[0.05, 0.05, 0.05], direction=[-1, 0, 1], light_type='L_DIRECT', on=False, range=2000, cutoff=90,
            theta=90, color=[255, 255, 255], attenuation=[1, 0, 4e-06])
        preserve_entity(Light_SPACE_rockford_front, flags='HIDDEN', lightprops={'specular': [1, 1, 1]})
        Light_ROOM = Light(root=self, name='Light_ROOM', point_name='Light_ROOM', extra_name='', light_group=0,
            diffuse=[0.6, 0.6, 0.6], ambient=[0.15, 0.15, 0.15], direction=[0, 0, -1], light_type='L_DIRECT', on=True,
            range=2000, cutoff=90, theta=90, color=[255, 255, 255], attenuation=[1, 0, 4e-06])
        preserve_entity(Light_ROOM, flags='HIDDEN', lightprops={'specular': [1, 1, 1]})
        Light_shield_damage = Light(root=self, name='Light_shield_damage', point_name='Light_shield_damage', extra_name='',
            light_group=0, diffuse=[0, 0, 0], ambient=[0, 0, 0], direction=[0, 0, -1], light_type='L_DIRECT', on=True,
            range=5000, cutoff=98.999977, theta=90, color=[255, 255, 255], attenuation=[1, 0, 0])
        preserve_entity(Light_shield_damage)
        Light_ROOM_backside = Light(root=self, name='Light_ROOM_backside', point_name='Light_ROOM_backside', extra_name='',
            light_group=0, diffuse=[0.5, 0.5, 0.5], ambient=[0.25, 0.25, 0.25], direction=[0, 0, 1], light_type='L_DIRECT',
            on=False, range=2000, cutoff=90, theta=90, color=[255, 255, 255], attenuation=[1, 0, 4e-06])
        preserve_entity(Light_ROOM_backside, flags='HIDDEN', lightprops={'specular': [1, 1, 1]})
        Light_ROOM_backside_nomad_light = Light(root=self, name='Light_ROOM_backside_nomad_light',
            point_name='Light_ROOM_backside_nomad_light', extra_name='', light_group=0, diffuse=[0.6, 0.5, 0.9],
            ambient=[0.6, 0.1, 0.8], direction=[0, 0, 1], light_type='L_DIRECT', on=False, range=2000, cutoff=90, theta=90,
            color=[255, 255, 255], attenuation=[1, 0, 4e-06])
        preserve_entity(Light_ROOM_backside_nomad_light, flags='HIDDEN', lightprops={'specular': [1, 1, 1]})
        Light_gun01_flash = Light(root=self, name='Light_gun01_flash', point_name='Light_gun01_flash', extra_name='',
            light_group=5, diffuse=[0, 0, 0], ambient=[0, 0, 0], direction=[0, 0, 1], light_type='L_POINT', on=True,
            range=3, cutoff=98.999977, theta=90, color=[255, 255, 255], attenuation=[0.8000000119, 0, 0.0399999991])
        preserve_entity(Light_gun01_flash)
        Light_gun02_flash = Light(root=self, name='Light_gun02_flash', point_name='Light_gun02_flash', extra_name='',
            light_group=5, diffuse=[0, 0, 0], ambient=[0, 0, 0], direction=[0, 0, 1], light_type='L_POINT', on=True,
            range=3, cutoff=98.999977, theta=90, color=[255, 255, 255], attenuation=[0.8000000119, 0, 0.0399999991])
        preserve_entity(Light_gun02_flash)
        Ship_l_elite_1_engine_li_small_1 = SpatialSound(root=self, name='Ship_l_elite_1_engine_li_small_1',
            sound='engine_br_small', attenuation=-3, dmin=40, dmax=50, priority=None)
        preserve_entity(Ship_l_elite_1_engine_li_small_1, userprops={'category': 'Audio'})
        blackhole_ring = Alchemy(root=self, name='blackhole_ring', particles='Intro_volcanoplanet_sun',
            point_name='blackhole_ring', sparam=0)
        preserve_entity(blackhole_ring, lt_grp=7, flags='LIT_DYNAMIC')
        blackhole_lighting = Alchemy(root=self, name='blackhole_lighting', particles='gf_neutronstar',
            point_name='blackhole_lighting', sparam=0)
        preserve_entity(blackhole_lighting, lt_grp=6, flags='LIT_DYNAMIC')
        planet_1 = PropPlanet1(root=self, name='planet_1', light_group=7, init_point='planet_1', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(planet_1, userprops={'category': 'Solar'})
        blackhole = PropBlackhole(root=self, name='blackhole', light_group=7, init_point='blackhole', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(blackhole, userprops={'category': 'Solar'})
        gatling = Sound(root=self, name='gatling', sound='rtc_m07_gatling', attenuation=-15, dmin=490, dmax=500,
            priority='Story_Sound_1')
        preserve_entity(gatling, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        shield1 = Sound(root=self, name='shield1', sound='sh_li01', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(shield1, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        shield2 = Sound(root=self, name='shield2', sound='sh_li02', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(shield2, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        shield3 = Sound(root=self, name='shield3', sound='sh_li03', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(shield3, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        shield_offline = Sound(root=self, name='shield_offline', sound='cruise_disrupt', attenuation=0, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(shield_offline, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        transponder_reveal = Sound(root=self, name='transponder_reveal', sound='cloak_no_gunboat', attenuation=-5, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(transponder_reveal, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        transponder_activates = Sound(root=self, name='transponder_activates', sound='cloak_no_battleship', attenuation=-5,
            dmin=50, dmax=300, priority='Story_Sound_1')
        preserve_entity(transponder_activates, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        missile_rolling = Sound(root=self, name='missile_rolling', sound='tractor_interrupted', attenuation=-5, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(missile_rolling, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        missile_loaded = Sound(root=self, name='missile_loaded', sound='tractor_loot_grabbed', attenuation=-5, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(missile_loaded, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        missile_launch = Sound(root=self, name='missile_launch', sound='fire_missile_homing', attenuation=-1, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(missile_launch, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        missile_travel = SpatialSound(root=self, name='missile_travel', sound='engine_thruster', attenuation=-50, dmin=0.5,
            dmax=1, priority=None)
        preserve_entity(missile_travel, userprops={'category': 'Audio'})
        missile_travel2 = SpatialSound(root=self, name='missile_travel2', sound='engine_thruster', attenuation=-15,
            dmin=0.5, dmax=1, priority=None)
        preserve_entity(missile_travel2, userprops={'category': 'Audio'})
        click1 = Sound(root=self, name='click1', sound='sfx_ui_react_accept02', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(click1, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        click2 = Sound(root=self, name='click2', sound='sfx_ui_react_data01', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(click2, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        click3 = Sound(root=self, name='click3', sound='sfx_ui_react_data02', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        preserve_entity(click3, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        init_systems = Sound(root=self, name='init_systems', sound='sfx_ui_react_request01', attenuation=-10, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(init_systems, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        system_error1 = Sound(root=self, name='system_error1', sound='sfx_ui_react_accept01', attenuation=-10, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(system_error1, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        system_error2 = Sound(root=self, name='system_error2', sound='sfx_ui_react_denied01', attenuation=-5, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(system_error2, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        system_success = Sound(root=self, name='system_success', sound='sfx_ui_react_processing01', attenuation=-5, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(system_success, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        fx_player_trapped = Alchemy(root=self, name='fx_player_trapped', particles='ms6_trapped',
            point_name='fx_player_trapped', sparam=0)
        preserve_entity(fx_player_trapped, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_shield_offline = Alchemy(root=self, name='fx_shield_offline', particles='gf_li_bang01',
            point_name='fx_shield_offline', sparam=0)
        preserve_entity(fx_shield_offline, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_crystal_light = Alchemy(root=self, name='fx_crystal_light', particles='ms7_crystal_fx',
            point_name='fx_crystal_light', sparam=0)
        preserve_entity(fx_crystal_light, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_crystal_touch = Alchemy(root=self, name='fx_crystal_touch', particles='ms7_crystal_touch',
            point_name='fx_crystal_touch', sparam=0)
        preserve_entity(fx_crystal_touch, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_crystal_touch_mega_effect = Alchemy(root=self, name='fx_crystal_touch_mega_effect', particles='no_cloakeffect05',
            point_name='fx_crystal_touch_mega_effect', sparam=0)
        preserve_entity(fx_crystal_touch_mega_effect, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_crystal_touch_mega_effect2 = Alchemy(root=self, name='fx_crystal_touch_mega_effect2',
            particles='no_cloakeffect05', point_name='fx_crystal_touch_mega_effect2', sparam=0)
        preserve_entity(fx_crystal_touch_mega_effect2, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_player_transponding = Alchemy(root=self, name='fx_player_transponding', particles='no_cloakeffect05',
            point_name='fx_player_transponding', sparam=0)
        preserve_entity(fx_player_transponding, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_player_transponding2 = Alchemy(root=self, name='fx_player_transponding2', particles='gf_nomad_kernel',
            point_name='fx_player_transponding2', sparam=0)
        preserve_entity(fx_player_transponding2, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_player_transponding3 = Alchemy(root=self, name='fx_player_transponding3', particles='no_cloakeffect05',
            point_name='fx_player_transponding3', sparam=0)
        preserve_entity(fx_player_transponding3, flags='LIT_DYNAMIC+LIT_AMBIENT')
        the_stars = PropTheStars(root=self, name='the_stars', light_group=110, init_point='the_stars',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(the_stars, srt_grp=-100, usr_flg=1, userprops={'category': 'Prop'})
        the_background = PropTheBackground(root=self, name='the_background', light_group=110, init_point='the_background',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(the_background, srt_grp=-100, usr_flg=1, userprops={'category': 'Prop'})
        fx_rockford_engine01 = Alchemy(root=self, name='fx_rockford_engine01', particles='gf_br_smallengine02_fire',
            point_name='fx_rockford_engine01', sparam=0)
        preserve_entity(fx_rockford_engine01, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_rockford_engine02 = Alchemy(root=self, name='fx_rockford_engine02', particles='gf_br_smallengine02_fire',
            point_name='fx_rockford_engine02', sparam=0)
        preserve_entity(fx_rockford_engine02, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun01 = PropGun01(root=self, name='gun01', light_group=5, init_point='gun01', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(gun01, userprops={'category': 'Equipment'})
        gun02 = PropGun02(root=self, name='gun02', light_group=5, init_point='gun02', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(gun02, userprops={'category': 'Equipment'})
        launcher01 = PropLauncher01(root=self, name='launcher01', light_group=5, init_point='launcher01',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(launcher01, userprops={'category': 'Equipment'})
        cockpit_gun01 = PropCockpitGun01(root=self, name='cockpit_gun01', light_group=5, init_point='cockpit_gun01',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(cockpit_gun01, userprops={'category': 'Equipment'})
        cockpit_gun02 = PropCockpitGun02(root=self, name='cockpit_gun02', light_group=5, init_point='cockpit_gun02',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(cockpit_gun02, userprops={'category': 'Equipment'})
        missile01 = PropMissile01(root=self, name='missile01', light_group=5, init_point='missile01', rotate_from_quat=True,
            use_ambient=True)
        preserve_entity(missile01, userprops={'category': 'Equipment'})
        missile02 = PropMissile02(root=self, name='missile02', light_group=5, init_point='missile02', rotate_from_quat=True,
            use_ambient=True)
        preserve_entity(missile02, userprops={'category': 'Equipment'})
        fx_missile = Alchemy(root=self, name='fx_missile', particles='li_missile01_drive', point_name='fx_missile', sparam=0)
        preserve_entity(fx_missile, flags='LIT_DYNAMIC+LIT_AMBIENT')
        fx_missile_alt = Alchemy(root=self, name='fx_missile_alt', particles='li_missile01_drive',
            point_name='fx_missile_alt', sparam=0)
        preserve_entity(fx_missile_alt, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun01_proj_01 = Alchemy(root=self, name='gun01_proj_01', particles='rtc_sanctumgun_proj',
            point_name='gun01_proj_01', sparam=0)
        preserve_entity(gun01_proj_01, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun01_proj_02 = Alchemy(root=self, name='gun01_proj_02', particles='rtc_sanctumgun_proj',
            point_name='gun01_proj_02', sparam=0)
        preserve_entity(gun01_proj_02, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun02_proj_01 = Alchemy(root=self, name='gun02_proj_01', particles='rtc_sanctumgun_proj',
            point_name='gun02_proj_01', sparam=0)
        preserve_entity(gun02_proj_01, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun02_proj_02 = Alchemy(root=self, name='gun02_proj_02', particles='rtc_sanctumgun_proj',
            point_name='gun02_proj_02', sparam=0)
        preserve_entity(gun02_proj_02, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun_flash_01 = Alchemy(root=self, name='gun_flash_01', particles='rtc_sanctumgun_flash', point_name='gun_flash_01',
            sparam=0)
        preserve_entity(gun_flash_01, srt_grp=12, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun_flash_02 = Alchemy(root=self, name='gun_flash_02', particles='rtc_sanctumgun_flash', point_name='gun_flash_02',
            sparam=0)
        preserve_entity(gun_flash_02, srt_grp=12, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun_fireblast01 = Alchemy(root=self, name='gun_fireblast01', particles='gf_msn7_gunfire',
            point_name='gun_fireblast01', sparam=0)
        preserve_entity(gun_fireblast01, srt_grp=12, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun_fireblast02 = Alchemy(root=self, name='gun_fireblast02', particles='gf_msn7_gunfire',
            point_name='gun_fireblast02', sparam=0)
        preserve_entity(gun_fireblast02, srt_grp=12, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun_impact_01 = Alchemy(root=self, name='gun_impact_01', particles='gf_li_shield01', point_name='gun_impact_01',
            sparam=0)
        preserve_entity(gun_impact_01, srt_grp=12, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun_impact_02 = Alchemy(root=self, name='gun_impact_02', particles='gf_li_shield01', point_name='gun_impact_02',
            sparam=0)
        preserve_entity(gun_impact_02, srt_grp=12, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun_impact_03 = Alchemy(root=self, name='gun_impact_03', particles='gf_li_shield01', point_name='gun_impact_03',
            sparam=0)
        preserve_entity(gun_impact_03, srt_grp=12, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun_impact_04 = Alchemy(root=self, name='gun_impact_04', particles='gf_li_shield01', point_name='gun_impact_04',
            sparam=0)
        preserve_entity(gun_impact_04, srt_grp=12, flags='LIT_DYNAMIC+LIT_AMBIENT')
        gun_impact_05 = Alchemy(root=self, name='gun_impact_05', particles='gf_li_shield01', point_name='gun_impact_05',
            sparam=0)
        preserve_entity(gun_impact_05, srt_grp=12, flags='LIT_DYNAMIC+LIT_AMBIENT')
        trent = Character(root=self, actor=actors.Trent, light_group=0, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'Actor': 'Player', 'category': 'Character'})
        rockford = Character(root=self, actor=actors.Rockford, light_group=5, init_point='Char_rockford',
            rotate_from_quat=True, use_ambient=True, floor_height=0.5)
        preserve_entity(rockford, template_name='rockford', userprops={'actor': 'Rockford', 'category': 'Character'})
        rockford_chair = PropRockfordChair(root=self, name='rockford_chair', light_group=5, init_point='rockford_chair',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(rockford_chair, userprops={'category': 'Prop'})
        rockford_front = PropRockfordFront(root=self, name='rockford_front', light_group=5, init_point='rockford_front',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(rockford_front, userprops={'category': 'Spaceship'})
        PlayerShip = PropPlayership(root=self, name='PlayerShip', light_group=4, init_point='PlayerShip',
            rotate_from_quat=True, use_ambient=True)
        preserve_entity(PlayerShip, userprops={'category': 'Spaceship'})
        the_cockpit = PropTheCockpit(root=self, name='the_cockpit', light_group=0, init_point='the_cockpit',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(the_cockpit, userprops={'category': 'Prop'})
        case = PropCase(root=self, name='case', light_group=0, init_point='case', rotate_from_quat=True, use_ambient=True)
        preserve_entity(case, userprops={'category': 'Prop'})
        panel = PropPanel(root=self, name='panel', light_group=0, init_point='panel', rotate_from_quat=True,
            use_ambient=True)
        preserve_entity(panel, userprops={'category': 'Prop'})
        crystal = PropCrystal(root=self, name='crystal', light_group=0, init_point='crystal', rotate_from_quat=True,
            use_ambient=False)
        preserve_entity(crystal, userprops={'category': 'Prop'})
        tome = PropTome(root=self, name='tome', light_group=0, init_point='tome', rotate_from_quat=True, use_ambient=True)
        preserve_entity(tome, userprops={'category': 'Prop'})
        chair = PropChair(root=self, name='chair', light_group=0, init_point='chair', rotate_from_quat=True,
            use_ambient=True)
        preserve_entity(chair, userprops={'category': 'Prop'})
        rockford_cockpit = PropRockfordCockpit(root=self, name='rockford_cockpit', light_group=5,
            init_point='rockford_cockpit', rotate_from_quat=True, use_ambient=False)
        preserve_entity(rockford_cockpit, userprops={'category': 'Spaceship'})
        cam_start = LookAtCamera(root=self, name='cam_start', fov=12, farplane=5000, look_duration=70)
        preserve_entity(cam_start)
        cam_trent_pilot = LookAtCamera(root=self, name='cam_trent_pilot', fov=12, farplane=5000, look_duration=70)
        preserve_entity(cam_trent_pilot)
        cam_rockford_gunfire = LookAtCamera(root=self, name='cam_rockford_gunfire', fov=16, farplane=200000,
            look_duration=70)
        preserve_entity(cam_rockford_gunfire, cameraprops={'nearplane': 1})
        cam_trent_shield_damage = LookAtCamera(root=self, name='cam_trent_shield_damage', fov=12, farplane=200000,
            look_duration=70)
        preserve_entity(cam_trent_shield_damage)
        cam_shield_destroyed = StaticCamera(root=self, name='cam_shield_destroyed', fov=12, farplane=5000)
        preserve_entity(cam_shield_destroyed)
        cam_player_disappeared = StaticCamera(root=self, name='cam_player_disappeared', fov=12, farplane=5000)
        preserve_entity(cam_player_disappeared)
        cam_launcher_start = LookAtCamera(root=self, name='cam_launcher_start', fov=10, farplane=5000, look_duration=70)
        preserve_entity(cam_launcher_start)
        cam_flying_missile = StaticCamera(root=self, name='cam_flying_missile', fov=10, farplane=200000)
        preserve_entity(cam_flying_missile, cameraprops={'nearplane': 1})
        cam_flying_missile_near = StaticCamera(root=self, name='cam_flying_missile_near', fov=10, farplane=200000)
        preserve_entity(cam_flying_missile_near, cameraprops={'nearplane': 1})
        cam_trent_lookback = LookAtCamera(root=self, name='cam_trent_lookback', fov=12, farplane=200000, look_duration=70)
        preserve_entity(cam_trent_lookback)
        cam_trent_walkback = LookAtCamera(root=self, name='cam_trent_walkback', fov=10, farplane=200000, look_duration=70)
        preserve_entity(cam_trent_walkback)
        cam_trent_touch = LookAtCamera(root=self, name='cam_trent_touch', fov=8, farplane=200000, look_duration=70)
        preserve_entity(cam_trent_touch)
        cam_trent_missilewatch = LookAtCamera(root=self, name='cam_trent_missilewatch', fov=12, farplane=200000,
            look_duration=70)
        preserve_entity(cam_trent_missilewatch)

        # Вход / начальная постановка.
        t = 0
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='planet_1', angle=125, axis='Y_AXIS', duration=100,
            smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='planet_1', angle=450, axis='Z_AXIS', duration=100,
            smooth=False)
        blackhole_ring.start(group=MAIN, time_delay=t, duration=36000)
        blackhole_lighting.start(group=MAIN, time_delay=t, duration=36000)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='planet_1', angle=125, axis='Y_AXIS', duration=100,
            smooth=False)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='rockford_cockpit', anim='Sc_launch extend',
            duration=2, time_scale=35)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam_shield_destroyed', 'PlayerShip'], duration=70,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpPilot', target_type='HARDPOINT',
            flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['cam_player_disappeared', 'automarker_cam_player_disappeared_marker'], duration=70, offset=[0, 0, 0],
            up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpPilot', target_type='HARDPOINT', flags='LOOK_AT')
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='gun01', parent_name='rockford_front',
            duration=1000, target_hardpoint='HpConnect', parent_hardpoint='HpWeapon04')
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='gun02', parent_name='rockford_front',
            duration=1000, target_hardpoint='HpConnect', parent_hardpoint='HpWeapon03')
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='launcher01', parent_name='rockford_front',
            duration=1000, target_hardpoint='HpConnect', parent_hardpoint='HpWeapon02')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_rockford_engine01', 'rockford_front'],
            duration=1555, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpEngine01',
            target_type='HARDPOINT', flags='POSITION+ORIENTATION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_rockford_engine02', 'rockford_front'],
            duration=1555, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpEngine02',
            target_type='HARDPOINT', flags='POSITION+ORIENTATION')
        fx_rockford_engine01.start(group=MAIN, time_delay=t, duration=36000)
        fx_rockford_engine02.start(group=MAIN, time_delay=t, duration=36000)
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_rockford_engine01'], duration=0.5,
            psysprops={'sparam': 0.4})
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_rockford_engine02'], duration=0.5,
            psysprops={'sparam': 0.4})
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['rockford_chair', 'rockford_front'], duration=1555,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpPilot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        rockford.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=0.001)
        fx_player_trapped.start(group=MAIN, time_delay=t, duration=55)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_player_trapped', 'PlayerShip'], duration=260,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRoot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_start', target_name='automarker_cam_start_pos2',
            duration=6, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_start_focus',
            target_name='automarker_cam_start_marker_pos2', duration=6, smooth=True)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['Ship_l_elite_1_engine_li_small_1', 'rockford_front'], duration=60, offset=[0, 0, 0], up='Y_AXIS',
            front='NEG_Z_AXIS', target_part='HpEngine01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        Ship_l_elite_1_engine_li_small_1.start(group=MAIN, time_delay=t, duration=7, loop=True)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['gun_flash_01', 'gun01'], duration=11111,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFire01', target_type='HARDPOINT',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['gun_flash_02', 'gun02'], duration=11111,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFire01', target_type='HARDPOINT',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['gun01_proj_01', 'gun01'], duration=11111,
            offset=[0, 0, -4], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFire01', target_type='HARDPOINT',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['gun01_proj_02', 'gun01'], duration=11111,
            offset=[0, 0, -4], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFire01', target_type='HARDPOINT',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['gun02_proj_01', 'gun02'], duration=11111,
            offset=[0, 0, -4], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFire01', target_type='HARDPOINT',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['gun02_proj_02', 'gun02'], duration=11111,
            offset=[0, 0, -4], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFire01', target_type='HARDPOINT',
            flags='POSITION')
        t += 0.01
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['Char_rockford', 'rockford_front'], duration=1555,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpPilot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        t += 0.09
        cam_start.set(group=MAIN, time_delay=t)
        main_group.append_time(1)


        # Реплика 15 · trent · исходное время 1 с
        # Чёрт, Рокфорд, я обездвижен!
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(15)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        main_group.append_time(3)


        # Реплика 20 · rockford · исходное время 4 с
        # Я знаю.
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(20)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='rockford_front',
            target_name='automarker_mrk_rockford_fly_forward', duration=4, smooth=True, adjust_orient=False)
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_rockford_engine01'], duration=9,
            psysprops={'sparam': 1})
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_rockford_engine02'], duration=9,
            psysprops={'sparam': 1})
        t += 2
        cam_trent_pilot.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s020x_VanPelt_XC_CHRF_TYPE_000DN_06, duration=20,
            time_scale=1.6, start_time=0.2, loop=True)
        main_group.append_time(3.5)


        # Реплика 30 · trent · исходное время 7.5 с
        # Рокфорд, что происходит? Ты же агент СБА, ты должен мне помочь
        # Исходное окно facial: 15 с.
        t = 0
        trent.facial(group=MAIN, index=30, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-15.0)


        # Реплика 35 · trent · исходное время 7.5 с
        # Рокфорд, что происходит? Ты же агент СБА, ты должен мне помочь
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(35)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        t += 0.2
        click1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.3
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_SPACE_rockford_intro', duration=0,
            smooth=False, on=False)
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_rockford_engine01'], duration=2,
            psysprops={'sparam': 0.5})
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_rockford_engine02'], duration=2,
            psysprops={'sparam': 0.5})
        t += 0.2
        music_background.change_attenuation(group=MAIN, time_delay=t, duration=1, attenuation=0)
        t += 0.02
        music_background.start(group=MAIN, time_delay=t, duration=555, loop=True)
        t += 0.18
        click2.start(group=MAIN, time_delay=t, duration=5)
        t += 0.6
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_SPACE_rockford_front', duration=0,
            smooth=False, on=True)
        t += 0.1
        click3.start(group=MAIN, time_delay=t, duration=5)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='rockford_front',
            target_name='automarker_mrk_rockford_standing_before_fire', duration=0.001, smooth=True)
        t += 0.05
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['rockford_front', 'automarker_mrk_rockford_ready_to_fire_looking_point'], duration=1500,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        t += 0.05
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_mrk_rockford_ready_to_fire_looking_point',
            target_name='automarker_mrk_rockford_ready_to_fire_playerpoint', duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='rockford_front',
            target_name='automarker_mrk_rockford_ready_to_fire', duration=6.3, smooth=True)
        t += 0.6
        click1.start(group=MAIN, time_delay=t, duration=5)
        t += 0.2
        AudioAnimEvent(root=self, group=MAIN, time_delay=t, sound_name='DX_m07_omega13_0030_trent', duration=0.01,
            attenuation=-100)
        AudioAnimEvent(root=self, group=MAIN, time_delay=t, sound_name='DX_m07_omega13_0035_trent', duration=0.01,
            attenuation=0)
        cam_rockford_gunfire.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_rockford_gunfire',
            target_name='automarker_cam_rockford_gunfire_pos2', duration=6.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_rockford_gunfire_focus',
            target_name='automarker_cam_rockford_gunfire_marker_pos2', duration=5.5, smooth=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='rockford_front', anim='Sc_launch extend',
            duration=221, time_scale=0.9, start_time=4)
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='cockpit_gun01',
            parent_name='rockford_cockpit', duration=1000, target_hardpoint='HpConnect', parent_hardpoint='HpWeapon04')
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='cockpit_gun02',
            parent_name='rockford_cockpit', duration=1000, target_hardpoint='HpConnect', parent_hardpoint='HpWeapon03')
        main_group.append_time(4.5)


        # Реплика 40 · rockford · исходное время 12 с
        # Я не агент СБА.
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(40)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_rockford_engine01'], duration=2,
            psysprops={'sparam': 0.2})
        SourceAlchemyAnimEvent(root=self, group=MAIN, time_delay=t, targets=['fx_rockford_engine02'], duration=2,
            psysprops={'sparam': 0.2})
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='gun01', anim='Sc_fire', duration=9, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='gun02', anim='Sc_fire', duration=9, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='cockpit_gun01', anim='Sc_fire', duration=25, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='cockpit_gun02', anim='Sc_fire', duration=25, loop=True)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['gun_fireblast01', 'cockpit_gun01'], duration=11111,
            offset=[0, 0, -2], up='NEG_Z_AXIS', front='NEG_Y_AXIS', target_part='HpFire01', target_type='HARDPOINT',
            flags='POSITION')
        gun_fireblast01.start(group=MAIN, time_delay=t, duration=10)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['gun_fireblast01', 'Char_trent'], duration=70,
            offset=[0, 0, 0], up='NEG_Z_AXIS', front='Y_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['gun_fireblast02', 'cockpit_gun02'], duration=11111,
            offset=[0, 0, -2], up='NEG_Z_AXIS', front='NEG_Y_AXIS', target_part='HpFire01', target_type='HARDPOINT',
            flags='POSITION')
        gun_fireblast02.start(group=MAIN, time_delay=t, duration=10)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['gun_fireblast02', 'Char_trent'], duration=70,
            offset=[0, 0, 0], up='NEG_Z_AXIS', front='Y_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        t += 1.5
        gatling.start(group=MAIN, time_delay=t, duration=2.5)
        t += 0.5
        gun_flash_01.start(group=MAIN, time_delay=t, duration=6)
        gun_flash_02.start(group=MAIN, time_delay=t, duration=6)
        gun01_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['Light_gun01_flash', 'gun01'], duration=10,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFire01', target_type='HARDPOINT',
            flags='POSITION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['Light_gun02_flash', 'gun02'], duration=10,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFire01', target_type='HARDPOINT',
            flags='POSITION')
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.8, 0.8, 0.8])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.8, 0.8, 0.8], lt_range=3)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1])
        t += 0.05
        gun01_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5])
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], lt_range=5)
        t += 0.1
        gun01_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=4)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1])
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5])
        t += 0.05
        gun01_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0])
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.8, 0.8, 0.8])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.8, 0.8, 0.8])
        t += 0.1
        gun01_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=4)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_ROOM', duration=0, smooth=False,
            diffuse=[0.1, 0.1, 0.1], ambient=[0.05, 0.05, 0.05])
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], lt_range=3)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[0, 0, 0])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0])
        t += 0.05
        gun01_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5])
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1])
        t += 0.1
        gun01_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5])
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=4)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.3, 0.3, 0.3], ambient=[0.3, 0.3, 0.3])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.3, 0.3, 0.3], ambient=[0.3, 0.3, 0.3], lt_range=3)
        t += 0.05
        gun01_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=4)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0])
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5])
        t += 0.1
        gun01_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1])
        cam_trent_shield_damage.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trent_shield_damage',
            target_name='automarker_cam_trent_shield_damage_pos2', duration=2, smooth=False)
        gun_impact_01.start(group=MAIN, time_delay=t, duration=60)
        shield1.start(group=MAIN, time_delay=t, duration=60)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5])
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1])
        t += 0.05
        gun01_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], lt_range=3)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.25, 0.3, 0.5], ambient=[0.25, 0.3, 0.5])
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5)
        t += 0.1
        gun01_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.8, 0.8, 0.8])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.8, 0.8, 0.8], lt_range=3)
        gun_impact_02.start(group=MAIN, time_delay=t, duration=60)
        shield2.start(group=MAIN, time_delay=t, duration=60)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1])
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5])
        t += 0.05
        gun01_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5)
        gun_impact_03.start(group=MAIN, time_delay=t, duration=60)
        shield3.start(group=MAIN, time_delay=t, duration=60)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5])
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.25, 0.3, 0.5], ambient=[0.25, 0.3, 0.5])
        t += 0.1
        gun01_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0])
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5])
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun01_flash', duration=0.05, smooth=False,
            on=False)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_gun02_flash', duration=0.05, smooth=False,
            on=False)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1])
        t += 0.05
        gun01_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.05
        gun_impact_04.start(group=MAIN, time_delay=t, duration=60)
        shield2.start(group=MAIN, time_delay=t, duration=60)
        t += 0.2
        gun01_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.25, 0.3, 0.5], ambient=[0.25, 0.3, 0.5])
        t += 0.2
        gun_impact_05.start(group=MAIN, time_delay=t, duration=60)
        shield1.start(group=MAIN, time_delay=t, duration=60)
        t += 0.05
        gun01_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1])
        main_group.append_time(6)


        # Реплика 50 · trent · исходное время 18 с
        # Ты же уничтожишь артефакты.
        # Исходное окно facial: 15 с.
        t = 0
        gun01_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun_impact_01.start(group=MAIN, time_delay=t, duration=60)
        shield1.start(group=MAIN, time_delay=t, duration=60)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='automarker_trent_head_ik',
            duration=5, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        cam_trent_pilot.set(group=MAIN, time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.25, 0.3, 0.5], ambient=[0.25, 0.3, 0.5])
        t += 0.15
        gun01_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.25
        gun01_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1])
        gun_impact_02.start(group=MAIN, time_delay=t, duration=60)
        shield2.start(group=MAIN, time_delay=t, duration=60)
        t += 0.25
        gun01_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.25, 0.3, 0.5], ambient=[0.25, 0.3, 0.5])
        gun_impact_03.start(group=MAIN, time_delay=t, duration=60)
        shield3.start(group=MAIN, time_delay=t, duration=60)
        t += 0.2
        gun01_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1])
        t += 0.15
        gun01_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.05
        gun_impact_04.start(group=MAIN, time_delay=t, duration=60)
        shield2.start(group=MAIN, time_delay=t, duration=60)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.25, 0.3, 0.5], ambient=[0.25, 0.3, 0.5])
        t += 0.1
        gun01_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_01.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.2
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1])
        gun_impact_05.start(group=MAIN, time_delay=t, duration=60)
        shield1.start(group=MAIN, time_delay=t, duration=60)
        t += 0.05
        gun01_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        gun02_proj_02.start(group=MAIN, time_delay=t, duration=0.5)
        t += 0.25
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_shield_damage', duration=0.5, smooth=True,
            diffuse=[0, 0, 0], ambient=[0, 0, 0])
        gun_impact_01.start(group=MAIN, time_delay=t, duration=60)
        shield1.start(group=MAIN, time_delay=t, duration=60)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_shield_offline', 'PlayerShip'], duration=260,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRoot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_mrk_missile01_start_pos', 'launcher01'],
            duration=1, offset=[0, 0, 0.7], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFire01',
            target_type='HARDPOINT', flags='POSITION+ORIENTATION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t,
            targets=['automarker_mrk_missile01_ready_to_load', 'launcher01'], duration=1, offset=[0, 0, -0.5], up='Y_AXIS',
            front='NEG_Z_AXIS', target_part='HpFire01', target_type='HARDPOINT', flags='POSITION+ORIENTATION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_mrk_missile01_final_hp', 'launcher01'],
            duration=15, offset=[0, 0, -0.7], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFire01',
            target_type='HARDPOINT', flags='POSITION+ORIENTATION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['automarker_mrk_missile01_firepoint', 'launcher01'],
            duration=1, offset=[0, 0, -220], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFire01',
            target_type='HARDPOINT', flags='POSITION+ORIENTATION')
        t += 0.2
        cam_shield_destroyed.set(group=MAIN, time_delay=t)
        t += 0.2
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_SPACE_playership_shield_fx', duration=0,
            smooth=False, on=True, diffuse=[0.8, 0.9, 1], ambient=[0.8, 0.9, 1])
        fx_shield_offline.start(group=MAIN, time_delay=t, duration=60)
        shield_offline.start(group=MAIN, time_delay=t, duration=5)
        t += 0.01
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_SPACE_playership_shield_fx', duration=0.75,
            smooth=False, diffuse=[0, 0, 0], ambient=[0, 0, 0])
        t += 0.09
        gun_impact_02.start(group=MAIN, time_delay=t, duration=60)
        t += 0.3
        gun_impact_03.start(group=MAIN, time_delay=t, duration=60)
        t += 0.2
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_ROOM', duration=0, smooth=False,
            diffuse=[0.6, 0.6, 0.6], ambient=[0.3, 0.3, 0.3])
        t += 0.3
        gun_impact_04.start(group=MAIN, time_delay=t, duration=60)
        t += 0.4
        gun_impact_05.start(group=MAIN, time_delay=t, duration=60)
        t += 0.3
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_SPACE_playership_shield_fx', duration=0,
            smooth=False, on=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_launcher_start',
            target_name='automarker_cam_launcher_start_pos2', duration=6, smooth=True)
        t += 0.5
        cam_launcher_start.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=50, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-10)


        # Реплика 60 · rockford · исходное время 23 с
        # Артефакты переживут уничтожение корабля.
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(60)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_launcher_start_focus',
            target_name='automarker_cam_launcher_start_marker_pos2', duration=5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='missile01',
            target_name='automarker_mrk_missile01_start_pos', duration=0.01, smooth=False)
        t += 2
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='launcher01', anim='Sc_br_slugger_launcher', duration=1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='missile01',
            target_name='automarker_mrk_missile01_final_hp', duration=1.99, smooth=False)
        t += 0.5
        missile_rolling.start(group=MAIN, time_delay=t, duration=15)
        t += 1.3
        missile_loaded.start(group=MAIN, time_delay=t, duration=15)
        t += 0.199
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['missile01', 'launcher01'], duration=2,
            offset=[0, 0, -0.7], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFire01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        t += 0.001
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='launcher01', anim='Sc_br_slugger_launcher',
            duration=1, start_time=1, trans_time=0.25)
        t += 1
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='crystal', angle=90, axis='X_AXIS', duration=0,
            smooth=False)
        fx_crystal_light.start(group=MAIN, time_delay=t, duration=36000)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_crystal_light', 'crystal'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRoot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        transponder_reveal.start(group=MAIN, time_delay=t, duration=15)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_ROOM', duration=0, smooth=False, on=False)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_ROOM_backside', duration=0, smooth=False,
            on=True)
        cam_trent_lookback.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_270LV_XA_03, duration=113,
            time_scale=0.75)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='crystal', angle=35, axis='Y_AXIS', duration=0,
            smooth=False)
        t += 0.49
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=90, axis='Y_AXIS', duration=3,
            smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='chair', angle=90, axis='Y_AXIS', duration=3,
            smooth=False)
        t += 3.5
        cam_trent_walkback.set(group=MAIN, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='chair', angle=90, axis='Y_AXIS', duration=2,
            smooth=False)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_270LV_XA_10, duration=25, time_scale=0.6,
            start_time=1.8, trans_time=1)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent', target_name='crystal', duration=7,
            transition_duration=2, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='panel', target_name='automarker_mrk_panel_open',
            duration=3, smooth=True, adjust_orient=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='crystal', target_name='automarker_mrk_crystal_open',
            duration=3, smooth=True, adjust_orient=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='tome', target_name='automarker_mrk_tome_open',
            duration=3, smooth=True, adjust_orient=False)
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-5, axis='Y_AXIS', duration=1,
            smooth=False)
        t += 2.5
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['cam_flying_missile', 'missile01'], duration=70,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='', target_type='ROOT', flags='LOOK_AT')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_missile', 'missile01'], duration=25,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpExhaust', target_type='HARDPOINT',
            flags='POSITION')
        t += 1
        cam_flying_missile.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='missile01',
            target_name='automarker_mrk_missile01_final_hp', duration=0, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='missile01',
            target_name='automarker_mrk_missile01_firepoint', duration=18, smooth=False)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='launcher01', anim='Sc_br_slugger_launcher', duration=1)
        fx_missile.start(group=MAIN, time_delay=t, duration=10)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='missile01', angle=3600, axis='Z_AXIS',
            duration=25, smooth=False)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['missile_travel', 'missile01'], duration=15,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpEngine01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        missile_travel.start(group=MAIN, time_delay=t, duration=15, loop=True)
        missile_launch.start(group=MAIN, time_delay=t, duration=5)
        missile_travel.change_attenuation(group=MAIN, time_delay=t, duration=3, attenuation=-5)
        t += 4
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='missile02',
            target_name='automarker_mrk_missile02_start_pos', duration=0, smooth=False)
        t += 1
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_ROOM_backside', duration=0, smooth=False,
            on=False)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_ROOM', duration=0, smooth=False, on=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent',
            target_name='automarker_point_trent_before_touch', duration=0, smooth=False)
        t += 0.25
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='Char_trent', angle=-35, axis='Y_AXIS', duration=0,
            smooth=False)
        t += 0.75
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='crystal', target_name='automarker_mrk_crystal_open2',
            duration=0, smooth=True, adjust_orient=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_cam_trent_touch_focus',
            target_name='automarker_cam_trent_touch_marker_pos2', duration=7, smooth=True)
        t += 1
        missile_travel.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=-100)
        cam_trent_touch.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_trent_touch',
            target_name='automarker_cam_trent_touch_pos2', duration=10, smooth=True)
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_SPCBODY_s027x_Trent_XA_STND_000DN_16, duration=8.5,
            time_scale=0.3, start_time=4)
        t += 1
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_missile_alt', 'missile02'], duration=25,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpExhaust', target_type='HARDPOINT',
            flags='POSITION')
        t += 1
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='missile02',
            target_name='automarker_mrk_missile02_final_pos', duration=15, smooth=False)
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='missile02', angle=3600, axis='Z_AXIS',
            duration=25, smooth=False)
        fx_missile_alt.start(group=MAIN, time_delay=t, duration=25)
        t += 0.5
        ConnectHardpointEvent(root=self, group=MAIN, time_delay=t, target_name='crystal', parent_name='Char_trent',
            duration=20, target_hardpoint='HpProp_Connect', parent_hardpoint='HpLeftConnect')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_crystal_touch', 'crystal'], duration=60,
            offset=[0, 0.05, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpFX', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        fx_crystal_touch.start(group=MAIN, time_delay=t, duration=30)
        fx_crystal_touch_mega_effect.start(group=MAIN, time_delay=t, duration=30)
        transponder_activates.start(group=MAIN, time_delay=t, duration=15)
        t += 4.5
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_ROOM_backside_nomad_light', duration=0,
            smooth=False, on=True)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_ROOM_backside', duration=0, smooth=False,
            on=False)
        LightAnimEvent(root=self, group=MAIN, time_delay=t, object_name='Light_ROOM', duration=0, smooth=False, on=False)
        fx_crystal_touch_mega_effect2.start(group=MAIN, time_delay=t, duration=30)
        cam_trent_missilewatch.set(group=MAIN, time_delay=t)
        CameraAnimEvent(root=self, group=MAIN, time_delay=t, camera_name='cam_trent_missilewatch', duration=3, fov=4,
            smooth=True)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_player_transponding', 'PlayerShip'],
            duration=260, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRoot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_player_transponding2', 'PlayerShip'],
            duration=260, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRoot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_player_transponding3', 'PlayerShip'],
            duration=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpRoot', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION')
        t += 4
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='cam_flying_missile_near', angle=5, axis='Y_AXIS',
            duration=0, smooth=False)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['fx_missile', 'missile01'], duration=25,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpExhaust', target_type='HARDPOINT',
            flags='POSITION')
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, time_delay=t, object_name='cam_flying_missile_near', angle=-3, axis='X_AXIS',
            duration=0, smooth=False)
        t += 0.49
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='missile01',
            target_name='automarker_mrk_missile01_fly2_start_pos', duration=0, smooth=False)
        t += 0.5
        fx_player_transponding.start(group=MAIN, time_delay=t, duration=235)
        cam_flying_missile_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_flying_missile_near',
            target_name='automarker_cam_flying_missile_near_pos2', duration=10, smooth=False)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='missile01',
            target_name='automarker_mrk_missile01_fly2_final_pos', duration=10, smooth=False)
        SourceAttachEvent(root=self, group=MAIN, time_delay=t, targets=['missile_travel2', 'missile01'], duration=60,
            offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS', target_part='HpEngine01', target_type='HARDPOINT',
            flags='POSITION+ORIENTATION+ENTITY_RELATIVE')
        missile_travel2.start(group=MAIN, time_delay=t, duration=55, loop=True)
        fx_missile.start(group=MAIN, time_delay=t, duration=25)
        t += 2
        fx_player_transponding2.start(group=MAIN, time_delay=t, duration=2)
        t += 1
        fx_player_transponding3.start(group=MAIN, time_delay=t, duration=5)
        t += 1
        cam_player_disappeared.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='PlayerShip', target_name='offscreen', duration=0,
            smooth=False)
        t += 3
        missile_travel.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=-100)
        t += 5
        music_background.change_attenuation(group=MAIN, time_delay=t, duration=1, attenuation=-100)
        main_group.append_time(45.0)
        preserve_spatial(self.get_entity('the_stars'), source_basis=[[10, 0, 0], [0, 10, 0], [0, 0, 10]],
            reference_orientation=[1.0, -0.0, -0.0, -0.0])


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M07Omega13Scene
