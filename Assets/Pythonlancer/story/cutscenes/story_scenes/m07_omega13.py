"""m07_omega13: полная постановка из master; точки в m07_omega13.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Alchemy, AttachEvent, AudioAnimEvent, Character, ConnectHardpointEvent, Equipment, Light, LightAnimEvent, LookAtCamera, LookAtEvent, MAIN, Male, MotionEvent, MoveEvent, NeckIkEvent, Prop, RotateAxisEvent, Ship, Solar, Sound, SoundEvent, SpatialSound, StaticCamera,
)
from story.cutscenes.anim import (
    Male,
)
from story import actors


class Planet1Prop(Solar):
    COMPOUND_TEMPLATE_NAME = 'planet_mercury_5000'

class BlackholeProp(Solar):
    COMPOUND_TEMPLATE_NAME = 'BlackHoleSun'

class TheStarsProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'new_generic'
    SRT_GRP = -100
    USR_FLG = 1

class TheBackgroundProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'om13_nebula'
    SRT_GRP = -100
    USR_FLG = 1

class Gun01Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_mass_driver'

class Gun02Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_mass_driver'

class Launcher01Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_slugger_launcher'

class CockpitGun01Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_mass_driver'

class CockpitGun02Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_mass_driver'

class Missile01Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_slugger_missile'

class Missile02Prop(Equipment):
    COMPOUND_TEMPLATE_NAME = 'rtcprop_weapons_br_slugger_missile'

class RockfordChairProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_pilot_chair'

class RockfordFrontProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'ge_fighter6'

class PlayershipProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'PlayerShip'

class TheCockpitProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_cockpit'

class CaseProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_case'

class PanelProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_panel'

class CrystalProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'Blixx_crystal'

class TomeProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'tome_075'

class ChairProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'm7_pilot_chair'

class RockfordCockpitProp(Ship):
    COMPOUND_TEMPLATE_NAME = 'ge_fighter6'


class M07Omega13Scene(Scene):
    DUMP_FILE = 'm07_omega13'
    SCENE_AMBIENT = [0, 0, 0]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        music_background = Sound(root=self, name='music_background', sound='rtc_m07_the_hitman', attenuation=-20,
            dmin=50, dmax=300, priority='Story_Sound_1')
        light_space_background = Light(root=self, name='Light_SPACE_background',
            point_name='Light_SPACE_background', extra_name='', light_group=7, hidden=True, rotate_from_quat=True,
            diffuse=[1, 0.8823529, 0.7058824], ambient=[0.05, 0.05, 0.05], direction=[-1, 0, 1],
            light_type='L_DIRECT', range=2000, cutoff=90, theta=90, color=[255, 255, 255],
            attenuation=[1, 0, 4e-06], on=True, specular=[1, 1, 1])
        light_space_playership = Light(root=self, name='Light_SPACE_playership',
            point_name='Light_SPACE_playership', extra_name='', light_group=4, hidden=True, rotate_from_quat=True,
            diffuse=[1, 0.8823529, 0.7058824], ambient=[0.05, 0.05, 0.05], direction=[-1, 0, -1],
            light_type='L_DIRECT', range=2000, cutoff=90, theta=90, color=[255, 255, 255],
            attenuation=[1, 0, 4e-06], on=True, specular=[1, 1, 1])
        light_space_playership_shield_fx = Light(root=self, name='Light_SPACE_playership_shield_fx',
            point_name='Light_SPACE_playership_shield_fx', extra_name='', light_group=4, hidden=True,
            rotate_from_quat=True, diffuse=[0, 0, 0], ambient=[0, 0, 0], direction=[-1, 0, -1],
            light_type='L_DIRECT', range=2000, cutoff=90, theta=90, color=[255, 255, 255],
            attenuation=[1, 0, 4e-06], on=False, specular=[1, 1, 1])
        light_space_rockford_intro = Light(root=self, name='Light_SPACE_rockford_intro',
            point_name='Light_SPACE_rockford_intro', extra_name='', light_group=5, hidden=True,
            rotate_from_quat=True, diffuse=[1, 0.8823529, 0.7058824], ambient=[0.05, 0.05, 0.05],
            direction=[-1, 0, -1], light_type='L_DIRECT', range=2000, cutoff=90, theta=90, color=[255, 255, 255],
            attenuation=[1, 0, 4e-06], on=True, specular=[1, 1, 1])
        light_space_rockford_front = Light(root=self, name='Light_SPACE_rockford_front',
            point_name='Light_SPACE_rockford_front', extra_name='', light_group=5, hidden=True,
            rotate_from_quat=True, diffuse=[1, 0.8823529, 0.7058824], ambient=[0.05, 0.05, 0.05],
            direction=[-1, 0, 1], light_type='L_DIRECT', range=2000, cutoff=90, theta=90, color=[255, 255, 255],
            attenuation=[1, 0, 4e-06], on=False, specular=[1, 1, 1])
        light_room = Light(root=self, name='Light_ROOM', point_name='Light_ROOM', extra_name='', light_group=0,
            hidden=True, rotate_from_quat=True, diffuse=[0.6, 0.6, 0.6], ambient=[0.15, 0.15, 0.15],
            direction=[0, 0, -1], light_type='L_DIRECT', range=2000, cutoff=90, theta=90, color=[255, 255, 255],
            attenuation=[1, 0, 4e-06], on=True, specular=[1, 1, 1])
        light_shield_damage = Light(root=self, name='Light_shield_damage', point_name='Light_shield_damage',
            extra_name='', light_group=0, hidden=False, rotate_from_quat=True, diffuse=[0, 0, 0],
            ambient=[0, 0, 0], direction=[0, 0, -1], light_type='L_DIRECT', range=5000, cutoff=98.999977,
            theta=90, color=[255, 255, 255], attenuation=[1, 0, 0], on=True)
        light_room_backside = Light(root=self, name='Light_ROOM_backside', point_name='Light_ROOM_backside',
            extra_name='', light_group=0, hidden=True, rotate_from_quat=True, diffuse=[0.5, 0.5, 0.5],
            ambient=[0.25, 0.25, 0.25], direction=[0, 0, 1], light_type='L_DIRECT', range=2000, cutoff=90,
            theta=90, color=[255, 255, 255], attenuation=[1, 0, 4e-06], on=False, specular=[1, 1, 1])
        light_room_backside_nomad_light = Light(root=self, name='Light_ROOM_backside_nomad_light',
            point_name='Light_ROOM_backside_nomad_light', extra_name='', light_group=0, hidden=True,
            rotate_from_quat=True, diffuse=[0.6, 0.5, 0.9], ambient=[0.6, 0.1, 0.8], direction=[0, 0, 1],
            light_type='L_DIRECT', range=2000, cutoff=90, theta=90, color=[255, 255, 255],
            attenuation=[1, 0, 4e-06], on=False, specular=[1, 1, 1])
        light_gun01_flash = Light(root=self, name='Light_gun01_flash', point_name='Light_gun01_flash',
            extra_name='', light_group=5, hidden=False, rotate_from_quat=True, diffuse=[0, 0, 0],
            ambient=[0, 0, 0], direction=[0, 0, 1], light_type='L_POINT', range=3, cutoff=98.999977, theta=90,
            color=[255, 255, 255], attenuation=[0.8000000119, 0, 0.0399999991], on=True)
        light_gun02_flash = Light(root=self, name='Light_gun02_flash', point_name='Light_gun02_flash',
            extra_name='', light_group=5, hidden=False, rotate_from_quat=True, diffuse=[0, 0, 0],
            ambient=[0, 0, 0], direction=[0, 0, 1], light_type='L_POINT', range=3, cutoff=98.999977, theta=90,
            color=[255, 255, 255], attenuation=[0.8000000119, 0, 0.0399999991], on=True)
        ship_l_elite_1_engine_li_small_1 = SpatialSound(root=self, name='Ship_l_elite_1_engine_li_small_1',
            sound='engine_br_small', attenuation=-3, dmin=40, dmax=50, priority=None)
        blackhole_ring = Alchemy(root=self, name='blackhole_ring', particles='Intro_volcanoplanet_sun',
            point_name='blackhole_ring', sparam=0, light_group=7, sort_group=0, hidden=False, use_ambient=False)
        blackhole_lighting = Alchemy(root=self, name='blackhole_lighting', particles='gf_neutronstar',
            point_name='blackhole_lighting', sparam=0, light_group=6, sort_group=0, hidden=False,
            use_ambient=False)
        planet_1 = Planet1Prop(root=self, name='planet_1', light_group=7, init_point='planet_1',
            rotate_from_quat=True)
        blackhole = BlackholeProp(root=self, name='blackhole', light_group=7, init_point='blackhole',
            rotate_from_quat=True)
        gatling = Sound(root=self, name='gatling', sound='rtc_m07_gatling', attenuation=-15, dmin=490, dmax=500,
            priority='Story_Sound_1')
        shield1 = Sound(root=self, name='shield1', sound='sh_li01', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        shield2 = Sound(root=self, name='shield2', sound='sh_li02', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        shield3 = Sound(root=self, name='shield3', sound='sh_li03', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        shield_offline = Sound(root=self, name='shield_offline', sound='cruise_disrupt', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        transponder_reveal = Sound(root=self, name='transponder_reveal', sound='cloak_no_gunboat', attenuation=-5,
            dmin=50, dmax=300, priority='Story_Sound_1')
        transponder_activates = Sound(root=self, name='transponder_activates', sound='cloak_no_battleship',
            attenuation=-5, dmin=50, dmax=300, priority='Story_Sound_1')
        missile_rolling = Sound(root=self, name='missile_rolling', sound='tractor_interrupted', attenuation=-5,
            dmin=50, dmax=300, priority='Story_Sound_1')
        missile_loaded = Sound(root=self, name='missile_loaded', sound='tractor_loot_grabbed', attenuation=-5,
            dmin=50, dmax=300, priority='Story_Sound_1')
        missile_launch = Sound(root=self, name='missile_launch', sound='fire_missile_homing', attenuation=-1,
            dmin=50, dmax=300, priority='Story_Sound_1')
        missile_travel = SpatialSound(root=self, name='missile_travel', sound='engine_thruster', attenuation=-50,
            dmin=0.5, dmax=1, priority=None)
        missile_travel2 = SpatialSound(root=self, name='missile_travel2', sound='engine_thruster',
            attenuation=-15, dmin=0.5, dmax=1, priority=None)
        click1 = Sound(root=self, name='click1', sound='sfx_ui_react_accept02', attenuation=-15, dmin=50,
            dmax=300, priority='Story_Sound_1')
        click2 = Sound(root=self, name='click2', sound='sfx_ui_react_data01', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        click3 = Sound(root=self, name='click3', sound='sfx_ui_react_data02', attenuation=-15, dmin=50, dmax=300,
            priority='Story_Sound_1')
        init_systems = Sound(root=self, name='init_systems', sound='sfx_ui_react_request01', attenuation=-10,
            dmin=50, dmax=300, priority='Story_Sound_1')
        system_error1 = Sound(root=self, name='system_error1', sound='sfx_ui_react_accept01', attenuation=-10,
            dmin=50, dmax=300, priority='Story_Sound_1')
        system_error2 = Sound(root=self, name='system_error2', sound='sfx_ui_react_denied01', attenuation=-5,
            dmin=50, dmax=300, priority='Story_Sound_1')
        system_success = Sound(root=self, name='system_success', sound='sfx_ui_react_processing01',
            attenuation=-5, dmin=50, dmax=300, priority='Story_Sound_1')
        fx_player_trapped = Alchemy(root=self, name='fx_player_trapped', particles='ms6_trapped',
            point_name='fx_player_trapped', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_shield_offline = Alchemy(root=self, name='fx_shield_offline', particles='gf_li_bang01',
            point_name='fx_shield_offline', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_crystal_light = Alchemy(root=self, name='fx_crystal_light', particles='ms7_crystal_fx',
            point_name='fx_crystal_light', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_crystal_touch = Alchemy(root=self, name='fx_crystal_touch', particles='ms7_crystal_touch',
            point_name='fx_crystal_touch', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_crystal_touch_mega_effect = Alchemy(root=self, name='fx_crystal_touch_mega_effect',
            particles='no_cloakeffect05', point_name='fx_crystal_touch_mega_effect', sparam=0, light_group=0,
            sort_group=0, hidden=False, use_ambient=True)
        fx_crystal_touch_mega_effect2 = Alchemy(root=self, name='fx_crystal_touch_mega_effect2',
            particles='no_cloakeffect05', point_name='fx_crystal_touch_mega_effect2', sparam=0, light_group=0,
            sort_group=0, hidden=False, use_ambient=True)
        fx_player_transponding = Alchemy(root=self, name='fx_player_transponding', particles='no_cloakeffect05',
            point_name='fx_player_transponding', sparam=0, light_group=0, sort_group=0, hidden=False,
            use_ambient=True)
        fx_player_transponding2 = Alchemy(root=self, name='fx_player_transponding2', particles='gf_nomad_kernel',
            point_name='fx_player_transponding2', sparam=0, light_group=0, sort_group=0, hidden=False,
            use_ambient=True)
        fx_player_transponding3 = Alchemy(root=self, name='fx_player_transponding3', particles='no_cloakeffect05',
            point_name='fx_player_transponding3', sparam=0, light_group=0, sort_group=0, hidden=False,
            use_ambient=True)
        the_stars = TheStarsProp(root=self, name='the_stars', light_group=110, init_point='the_stars',
            rotate_from_quat=True)
        the_background = TheBackgroundProp(root=self, name='the_background', light_group=110,
            init_point='the_background', rotate_from_quat=True)
        fx_rockford_engine01 = Alchemy(root=self, name='fx_rockford_engine01',
            particles='gf_br_smallengine02_fire', point_name='fx_rockford_engine01', sparam=0, light_group=0,
            sort_group=0, hidden=False, use_ambient=True)
        fx_rockford_engine02 = Alchemy(root=self, name='fx_rockford_engine02',
            particles='gf_br_smallengine02_fire', point_name='fx_rockford_engine02', sparam=0, light_group=0,
            sort_group=0, hidden=False, use_ambient=True)
        gun01 = Gun01Prop(root=self, name='gun01', light_group=5, init_point='gun01', rotate_from_quat=True)
        gun02 = Gun02Prop(root=self, name='gun02', light_group=5, init_point='gun02', rotate_from_quat=True)
        launcher01 = Launcher01Prop(root=self, name='launcher01', light_group=5, init_point='launcher01',
            rotate_from_quat=True)
        cockpit_gun01 = CockpitGun01Prop(root=self, name='cockpit_gun01', light_group=5,
            init_point='cockpit_gun01', rotate_from_quat=True)
        cockpit_gun02 = CockpitGun02Prop(root=self, name='cockpit_gun02', light_group=5,
            init_point='cockpit_gun02', rotate_from_quat=True)
        missile01 = Missile01Prop(root=self, name='missile01', light_group=5, init_point='missile01',
            rotate_from_quat=True, use_ambient=True)
        missile02 = Missile02Prop(root=self, name='missile02', light_group=5, init_point='missile02',
            rotate_from_quat=True, use_ambient=True)
        fx_missile = Alchemy(root=self, name='fx_missile', particles='li_missile01_drive',
            point_name='fx_missile', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        fx_missile_alt = Alchemy(root=self, name='fx_missile_alt', particles='li_missile01_drive',
            point_name='fx_missile_alt', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        gun01_proj_01 = Alchemy(root=self, name='gun01_proj_01', particles='rtc_sanctumgun_proj',
            point_name='gun01_proj_01', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        gun01_proj_02 = Alchemy(root=self, name='gun01_proj_02', particles='rtc_sanctumgun_proj',
            point_name='gun01_proj_02', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        gun02_proj_01 = Alchemy(root=self, name='gun02_proj_01', particles='rtc_sanctumgun_proj',
            point_name='gun02_proj_01', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        gun02_proj_02 = Alchemy(root=self, name='gun02_proj_02', particles='rtc_sanctumgun_proj',
            point_name='gun02_proj_02', sparam=0, light_group=0, sort_group=0, hidden=False, use_ambient=True)
        gun_flash_01 = Alchemy(root=self, name='gun_flash_01', particles='rtc_sanctumgun_flash',
            point_name='gun_flash_01', sparam=0, light_group=0, sort_group=12, hidden=False, use_ambient=True)
        gun_flash_02 = Alchemy(root=self, name='gun_flash_02', particles='rtc_sanctumgun_flash',
            point_name='gun_flash_02', sparam=0, light_group=0, sort_group=12, hidden=False, use_ambient=True)
        gun_fireblast01 = Alchemy(root=self, name='gun_fireblast01', particles='gf_msn7_gunfire',
            point_name='gun_fireblast01', sparam=0, light_group=0, sort_group=12, hidden=False, use_ambient=True)
        gun_fireblast02 = Alchemy(root=self, name='gun_fireblast02', particles='gf_msn7_gunfire',
            point_name='gun_fireblast02', sparam=0, light_group=0, sort_group=12, hidden=False, use_ambient=True)
        gun_impact_01 = Alchemy(root=self, name='gun_impact_01', particles='gf_li_shield01',
            point_name='gun_impact_01', sparam=0, light_group=0, sort_group=12, hidden=False, use_ambient=True)
        gun_impact_02 = Alchemy(root=self, name='gun_impact_02', particles='gf_li_shield01',
            point_name='gun_impact_02', sparam=0, light_group=0, sort_group=12, hidden=False, use_ambient=True)
        gun_impact_03 = Alchemy(root=self, name='gun_impact_03', particles='gf_li_shield01',
            point_name='gun_impact_03', sparam=0, light_group=0, sort_group=12, hidden=False, use_ambient=True)
        gun_impact_04 = Alchemy(root=self, name='gun_impact_04', particles='gf_li_shield01',
            point_name='gun_impact_04', sparam=0, light_group=0, sort_group=12, hidden=False, use_ambient=True)
        gun_impact_05 = Alchemy(root=self, name='gun_impact_05', particles='gf_li_shield01',
            point_name='gun_impact_05', sparam=0, light_group=0, sort_group=12, hidden=False, use_ambient=True)
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        rockford = Character(root=self, actor=actors.Rockford, name='Char_rockford', light_group=5,
            init_point='Char_rockford', rotate_from_quat=True, use_ambient=True, appearance='rockford',
            actor_name='Rockford', floor_height=0.5)
        rockford_chair = RockfordChairProp(root=self, name='rockford_chair', light_group=5,
            init_point='rockford_chair', rotate_from_quat=True, use_ambient=True)
        rockford_front = RockfordFrontProp(root=self, name='rockford_front', light_group=5,
            init_point='rockford_front', rotate_from_quat=True)
        playership = PlayershipProp(root=self, name='PlayerShip', light_group=4, init_point='PlayerShip',
            rotate_from_quat=True, use_ambient=True)
        the_cockpit = TheCockpitProp(root=self, name='the_cockpit', light_group=0, init_point='the_cockpit',
            rotate_from_quat=True)
        case = CaseProp(root=self, name='case', light_group=0, init_point='case', rotate_from_quat=True,
            use_ambient=True)
        panel = PanelProp(root=self, name='panel', light_group=0, init_point='panel', rotate_from_quat=True,
            use_ambient=True)
        crystal = CrystalProp(root=self, name='crystal', light_group=0, init_point='crystal',
            rotate_from_quat=True)
        tome = TomeProp(root=self, name='tome', light_group=0, init_point='tome', rotate_from_quat=True,
            use_ambient=True)
        chair = ChairProp(root=self, name='chair', light_group=0, init_point='chair', rotate_from_quat=True,
            use_ambient=True)
        rockford_cockpit = RockfordCockpitProp(root=self, name='rockford_cockpit', light_group=5,
            init_point='rockford_cockpit', rotate_from_quat=True)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=12, look_duration=70)
        cam_trent_pilot = LookAtCamera(root=self, name='cam_trent_pilot', fov=12, look_duration=70)
        cam_rockford_gunfire = LookAtCamera(root=self, name='cam_rockford_gunfire', fov=16, farplane=200000,
            nearplane=1, look_duration=70)
        cam_trent_shield_damage = LookAtCamera(root=self, name='cam_trent_shield_damage', fov=12, farplane=200000,
            look_duration=70)
        cam_shield_destroyed = StaticCamera(root=self, name='cam_shield_destroyed', fov=12)
        cam_player_disappeared = StaticCamera(root=self, name='cam_player_disappeared', fov=12)
        cam_launcher_start = LookAtCamera(root=self, name='cam_launcher_start', fov=10, look_duration=70)
        cam_flying_missile = StaticCamera(root=self, name='cam_flying_missile', fov=10, farplane=200000,
            nearplane=1)
        cam_flying_missile_near = StaticCamera(root=self, name='cam_flying_missile_near', fov=10, farplane=200000,
            nearplane=1)
        cam_trent_lookback = LookAtCamera(root=self, name='cam_trent_lookback', fov=12, farplane=200000,
            look_duration=70)
        cam_trent_walkback = LookAtCamera(root=self, name='cam_trent_walkback', fov=10, farplane=200000,
            look_duration=70)
        cam_trent_touch = LookAtCamera(root=self, name='cam_trent_touch', fov=8, farplane=200000, look_duration=70)
        cam_trent_missilewatch = LookAtCamera(root=self, name='cam_trent_missilewatch', fov=12, farplane=200000,
            look_duration=70)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        RotateAxisEvent(root=self, group=MAIN, object_name=planet_1.name, angle=125, axis='Y_AXIS', duration=100,
            smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=planet_1.name, angle=450, axis='Z_AXIS', duration=100,
            smooth=False, time_delay=t)
        blackhole_ring.start(group=MAIN, duration=36000, time_delay=t)
        blackhole_lighting.start(group=MAIN, duration=36000, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=planet_1.name, angle=125, axis='Y_AXIS', duration=100,
            smooth=False, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=rockford_cockpit.name, anim='Sc_launch extend', duration=2,
            time_scale=35, time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_shield_destroyed.name, focus=playership.name, duration=70,
            target_type='HARDPOINT', target_part='HpPilot', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=cam_player_disappeared.name,
            focus=self.get_automarker_name('cam_player_disappeared_marker'), duration=70, target_type='HARDPOINT',
            target_part='HpPilot', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=gun01.name, parent_name=rockford_front.name,
            duration=1000, target_hardpoint='HpConnect', parent_hardpoint='HpWeapon04', time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=gun02.name, parent_name=rockford_front.name,
            duration=1000, target_hardpoint='HpConnect', parent_hardpoint='HpWeapon03', time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=launcher01.name, parent_name=rockford_front.name,
            duration=1000, target_hardpoint='HpConnect', parent_hardpoint='HpWeapon02', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_rockford_engine01.name, parent_name=rockford_front.name,
            duration=1555, target_part='HpEngine01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_rockford_engine02.name, parent_name=rockford_front.name,
            duration=1555, target_part='HpEngine02', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        fx_rockford_engine01.start(group=MAIN, duration=36000, time_delay=t)
        fx_rockford_engine02.start(group=MAIN, duration=36000, time_delay=t)
        fx_rockford_engine01.set_sparam(group=MAIN, duration=0.5, sparam=0.4, smooth=False, time_delay=t)
        fx_rockford_engine02.set_sparam(group=MAIN, duration=0.5, sparam=0.4, smooth=False, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=rockford_chair.name, parent_name=rockford_front.name,
            duration=1555, target_part='HpPilot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        rockford.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=0.001, time_delay=t)
        fx_player_trapped.start(group=MAIN, duration=55, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_player_trapped.name, parent_name=playership.name,
            duration=260, target_part='HpRoot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=ship_l_elite_1_engine_li_small_1.name,
            parent_name=rockford_front.name, duration=60, target_part='HpEngine01', target_type='HARDPOINT',
            adjust_pos=True, adjust_orient=True, entity_relative=True, up='Y_AXIS', front='NEG_Z_AXIS',
            time_delay=t)
        ship_l_elite_1_engine_li_small_1.start(group=MAIN, duration=7, loop=True, start_time=0, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=gun_flash_01.name, parent_name=gun01.name, duration=11111,
            target_part='HpFire01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=gun_flash_02.name, parent_name=gun02.name, duration=11111,
            target_part='HpFire01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=gun01_proj_01.name, parent_name=gun01.name, duration=11111,
            target_part='HpFire01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', offset_z=-4, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=gun01_proj_02.name, parent_name=gun01.name, duration=11111,
            target_part='HpFire01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', offset_z=-4, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=gun02_proj_01.name, parent_name=gun02.name, duration=11111,
            target_part='HpFire01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', offset_z=-4, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=gun02_proj_02.name, parent_name=gun02.name, duration=11111,
            target_part='HpFire01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', offset_z=-4, time_delay=t)
        t += 0.01
        AttachEvent(root=self, group=MAIN, target_name=rockford.name, parent_name=rockford_front.name,
            duration=1555, target_part='HpPilot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        t += 0.09
        cam_start.set(group=MAIN, time_delay=t)
        main_group.append_time(1)

        # m07_omega13 15: Trent.
        # Чёрт, Рокфорд, я обездвижен!
        line_sound = self.lookup_single_sound(15)
        SoundEvent(root=self, group=MAIN, sound_name=line_sound.get_nickname())
        main_group.append_time(3)

        # m07_omega13 20: Rockford.
        # Я знаю.
        t = 1
        MoveEvent(root=self, group=MAIN, object_name=rockford_front.name,
            target_name=self.get_automarker_name('mrk_rockford_fly_forward'), duration=4, smooth=True,
            adjust_pos=True, adjust_orient=False, time_delay=t)
        fx_rockford_engine01.set_sparam(group=MAIN, duration=9, sparam=1, smooth=False, time_delay=t)
        fx_rockford_engine02.set_sparam(group=MAIN, duration=9, sparam=1, smooth=False, time_delay=t)
        t += 2
        cam_trent_pilot.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_SPCBODY_s020x_VanPelt_XC_CHRF_TYPE_000DN_06, duration=20,
            time_scale=1.6, start_time=0.2, loop=True, time_delay=t)
        line_sound = self.lookup_single_sound(20)
        SoundEvent(root=self, group=MAIN, sound_name=line_sound.get_nickname())
        main_group.append_time(3.5)

        # m07_omega13 30: Trent.
        # Рокфорд, что происходит? Ты же агент СБА, ты должен мне помочь
        line_sound = self.lookup_single_sound(30)
        SoundEvent(root=self, group=MAIN, sound_name=line_sound.get_nickname())
        main_group.append_time(0)

        # m07_omega13 35: Trent.
        # Рокфорд, что происходит? Ты же агент СБА, ты должен мне помочь
        t = 0.2
        click1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.3
        LightAnimEvent(root=self, group=MAIN, object_name=light_space_rockford_intro.name, duration=0,
            smooth=False, on=False, time_delay=t)
        fx_rockford_engine01.set_sparam(group=MAIN, duration=2, sparam=0.5, smooth=False, time_delay=t)
        fx_rockford_engine02.set_sparam(group=MAIN, duration=2, sparam=0.5, smooth=False, time_delay=t)
        t += 0.2
        music_background.change_attenuation(group=MAIN, duration=1, attenuation=0, time_delay=t)
        t += 0.02
        music_background.start(group=MAIN, duration=555, loop=True, start_time=0, time_delay=t)
        t += 0.18
        click2.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.6
        LightAnimEvent(root=self, group=MAIN, object_name=light_space_rockford_front.name, duration=0,
            smooth=False, on=True, time_delay=t)
        t += 0.1
        click3.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=rockford_front.name,
            target_name=self.get_automarker_name('mrk_rockford_standing_before_fire'), duration=0.001,
            smooth=True, adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.05
        LookAtEvent(root=self, group=MAIN, point=rockford_front.name,
            focus=self.get_automarker_name('mrk_rockford_ready_to_fire_looking_point'), duration=1500,
            target_type='ROOT', target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        t += 0.05
        MoveEvent(root=self, group=MAIN,
            object_name=self.get_automarker_name('mrk_rockford_ready_to_fire_looking_point'),
            target_name=self.get_automarker_name('mrk_rockford_ready_to_fire_playerpoint'), duration=5,
            smooth=True, adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=rockford_front.name,
            target_name=self.get_automarker_name('mrk_rockford_ready_to_fire'), duration=6.3, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.6
        click1.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.2
        AudioAnimEvent(root=self, group=MAIN, sound_name='DX_m07_omega13_0030_trent', duration=0.01,
            attenuation=-100, time_delay=t)
        AudioAnimEvent(root=self, group=MAIN, sound_name='DX_m07_omega13_0035_trent', duration=0.01,
            attenuation=0, time_delay=t)
        cam_rockford_gunfire.set(group=MAIN, time_delay=t)
        cam_rockford_gunfire.move_cam(group=MAIN, index=2, duration=6.5, smooth=True, time_delay=t)
        cam_rockford_gunfire.move_focus(group=MAIN, index=2, duration=5.5, smooth=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=rockford_front.name, anim='Sc_launch extend', duration=221,
            time_scale=0.9, start_time=4, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=cockpit_gun01.name,
            parent_name=rockford_cockpit.name, duration=1000, target_hardpoint='HpConnect',
            parent_hardpoint='HpWeapon04', time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=cockpit_gun02.name,
            parent_name=rockford_cockpit.name, duration=1000, target_hardpoint='HpConnect',
            parent_hardpoint='HpWeapon03', time_delay=t)
        trent.facial(group=MAIN, index=35, auto_lip=True, extra_delay=0)

        # m07_omega13 40: Rockford.
        # Я не агент СБА.
        t = 0
        fx_rockford_engine01.set_sparam(group=MAIN, duration=2, sparam=0.2, smooth=False, time_delay=t)
        fx_rockford_engine02.set_sparam(group=MAIN, duration=2, sparam=0.2, smooth=False, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=gun01.name, anim='Sc_fire', duration=9, loop=True,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=gun02.name, anim='Sc_fire', duration=9, loop=True,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=cockpit_gun01.name, anim='Sc_fire', duration=25, loop=True,
            time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=cockpit_gun02.name, anim='Sc_fire', duration=25, loop=True,
            time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=gun_fireblast01.name, parent_name=cockpit_gun01.name,
            duration=11111, target_part='HpFire01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False,
            up='NEG_Z_AXIS', front='NEG_Y_AXIS', offset_z=-2, time_delay=t)
        gun_fireblast01.start(group=MAIN, duration=10, time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=gun_fireblast01.name, focus=trent.name, duration=70,
            target_type='ROOT', target_part='', up='NEG_Z_AXIS', front='Y_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=gun_fireblast02.name, parent_name=cockpit_gun02.name,
            duration=11111, target_part='HpFire01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False,
            up='NEG_Z_AXIS', front='NEG_Y_AXIS', offset_z=-2, time_delay=t)
        gun_fireblast02.start(group=MAIN, duration=10, time_delay=t)
        LookAtEvent(root=self, group=MAIN, point=gun_fireblast02.name, focus=trent.name, duration=70,
            target_type='ROOT', target_part='', up='NEG_Z_AXIS', front='Y_AXIS', time_delay=t)
        t += 1.5
        gatling.start(group=MAIN, duration=2.5, loop=False, start_time=0, time_delay=t)
        t += 0.5
        gun_flash_01.start(group=MAIN, duration=6, time_delay=t)
        gun_flash_02.start(group=MAIN, duration=6, time_delay=t)
        gun01_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=light_gun01_flash.name, parent_name=gun01.name,
            duration=10, target_part='HpFire01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=light_gun02_flash.name, parent_name=gun02.name,
            duration=10, target_part='HpFire01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5, time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.8, 0.8, 0.8], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.8, 0.8, 0.8], lt_range=3, time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], time_delay=t)
        t += 0.05
        gun01_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], lt_range=5, time_delay=t)
        t += 0.1
        gun01_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3, time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=4, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], time_delay=t)
        t += 0.05
        gun01_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.8, 0.8, 0.8], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.8, 0.8, 0.8], time_delay=t)
        t += 0.1
        gun01_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=4, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_room.name, duration=0, smooth=False,
            diffuse=[0.1, 0.1, 0.1], ambient=[0.05, 0.05, 0.05], time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], lt_range=3, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3, time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[0, 0, 0], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], time_delay=t)
        t += 0.05
        gun01_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], time_delay=t)
        t += 0.1
        gun01_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=4, time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.3, 0.3, 0.3], ambient=[0.3, 0.3, 0.3], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.3, 0.3, 0.3], ambient=[0.3, 0.3, 0.3], lt_range=3, time_delay=t)
        t += 0.05
        gun01_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=4, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], time_delay=t)
        t += 0.1
        gun01_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1], time_delay=t)
        cam_trent_shield_damage.set(group=MAIN, time_delay=t)
        cam_trent_shield_damage.move_cam(group=MAIN, index=2, duration=2, smooth=False, time_delay=t)
        gun_impact_01.start(group=MAIN, duration=60, time_delay=t)
        shield1.start(group=MAIN, duration=60, loop=False, start_time=0, time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], time_delay=t)
        t += 0.05
        gun01_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], lt_range=3, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.25, 0.3, 0.5], ambient=[0.25, 0.3, 0.5], time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5, time_delay=t)
        t += 0.1
        gun01_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.8, 0.8, 0.8], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.8, 0.8, 0.8], ambient=[0.8, 0.8, 0.8], lt_range=3, time_delay=t)
        gun_impact_02.start(group=MAIN, duration=60, time_delay=t)
        shield2.start(group=MAIN, duration=60, loop=False, start_time=0, time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1], time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], time_delay=t)
        t += 0.05
        gun01_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5, time_delay=t)
        gun_impact_03.start(group=MAIN, duration=60, time_delay=t)
        shield3.start(group=MAIN, duration=60, loop=False, start_time=0, time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.25, 0.3, 0.5], ambient=[0.25, 0.3, 0.5], time_delay=t)
        t += 0.1
        gun01_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[1, 1, 1], ambient=[1, 1, 1], lt_range=5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], lt_range=3, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            diffuse=[0.5, 0.5, 0.5], ambient=[0.5, 0.5, 0.5], time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun01_flash.name, duration=0.05, smooth=False,
            on=False, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_gun02_flash.name, duration=0.05, smooth=False,
            on=False, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1], time_delay=t)
        t += 0.05
        gun01_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.05
        gun_impact_04.start(group=MAIN, duration=60, time_delay=t)
        shield2.start(group=MAIN, duration=60, loop=False, start_time=0, time_delay=t)
        t += 0.2
        gun01_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.25, 0.3, 0.5], ambient=[0.25, 0.3, 0.5], time_delay=t)
        t += 0.2
        gun_impact_05.start(group=MAIN, duration=60, time_delay=t)
        shield1.start(group=MAIN, duration=60, loop=False, start_time=0, time_delay=t)
        t += 0.05
        gun01_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1], time_delay=t)
        line_sound = self.lookup_single_sound(40)
        SoundEvent(root=self, group=MAIN, sound_name=line_sound.get_nickname())
        main_group.append_time(6)

        # m07_omega13 50: Trent.
        # Ты же уничтожишь артефакты.
        t = 0
        gun01_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun_impact_01.start(group=MAIN, duration=60, time_delay=t)
        shield1.start(group=MAIN, duration=60, loop=False, start_time=0, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=1, time_delay=t)
        cam_trent_pilot.set(group=MAIN, time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.25, 0.3, 0.5], ambient=[0.25, 0.3, 0.5], time_delay=t)
        t += 0.15
        gun01_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.25
        gun01_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1], time_delay=t)
        gun_impact_02.start(group=MAIN, duration=60, time_delay=t)
        shield2.start(group=MAIN, duration=60, loop=False, start_time=0, time_delay=t)
        t += 0.25
        gun01_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.05
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.25, 0.3, 0.5], ambient=[0.25, 0.3, 0.5], time_delay=t)
        gun_impact_03.start(group=MAIN, duration=60, time_delay=t)
        shield3.start(group=MAIN, duration=60, loop=False, start_time=0, time_delay=t)
        t += 0.2
        gun01_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1], time_delay=t)
        t += 0.15
        gun01_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.05
        gun_impact_04.start(group=MAIN, duration=60, time_delay=t)
        shield2.start(group=MAIN, duration=60, loop=False, start_time=0, time_delay=t)
        t += 0.1
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.25, 0.3, 0.5], ambient=[0.25, 0.3, 0.5], time_delay=t)
        t += 0.1
        gun01_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_01.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.2
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.3, smooth=True,
            diffuse=[0.5, 0.6, 1], ambient=[0.5, 0.6, 1], time_delay=t)
        gun_impact_05.start(group=MAIN, duration=60, time_delay=t)
        shield1.start(group=MAIN, duration=60, loop=False, start_time=0, time_delay=t)
        t += 0.05
        gun01_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        gun02_proj_02.start(group=MAIN, duration=0.5, time_delay=t)
        t += 0.25
        LightAnimEvent(root=self, group=MAIN, object_name=light_shield_damage.name, duration=0.5, smooth=True,
            diffuse=[0, 0, 0], ambient=[0, 0, 0], time_delay=t)
        gun_impact_01.start(group=MAIN, duration=60, time_delay=t)
        shield1.start(group=MAIN, duration=60, loop=False, start_time=0, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_shield_offline.name, parent_name=playership.name,
            duration=260, target_part='HpRoot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('mrk_missile01_start_pos'),
            parent_name=launcher01.name, duration=1, target_part='HpFire01', target_type='HARDPOINT',
            adjust_pos=True, adjust_orient=True, up='Y_AXIS', front='NEG_Z_AXIS', offset_z=0.7, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('mrk_missile01_ready_to_load'),
            parent_name=launcher01.name, duration=1, target_part='HpFire01', target_type='HARDPOINT',
            adjust_pos=True, adjust_orient=True, up='Y_AXIS', front='NEG_Z_AXIS', offset_z=-0.5, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('mrk_missile01_final_hp'),
            parent_name=launcher01.name, duration=15, target_part='HpFire01', target_type='HARDPOINT',
            adjust_pos=True, adjust_orient=True, up='Y_AXIS', front='NEG_Z_AXIS', offset_z=-0.7, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=self.get_automarker_name('mrk_missile01_firepoint'),
            parent_name=launcher01.name, duration=1, target_part='HpFire01', target_type='HARDPOINT',
            adjust_pos=True, adjust_orient=True, up='Y_AXIS', front='NEG_Z_AXIS', offset_z=-220, time_delay=t)
        t += 0.2
        cam_shield_destroyed.set(group=MAIN, time_delay=t)
        t += 0.2
        LightAnimEvent(root=self, group=MAIN, object_name=light_space_playership_shield_fx.name, duration=0,
            smooth=False, on=True, diffuse=[0.8, 0.9, 1], ambient=[0.8, 0.9, 1], time_delay=t)
        fx_shield_offline.start(group=MAIN, duration=60, time_delay=t)
        shield_offline.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        t += 0.01
        LightAnimEvent(root=self, group=MAIN, object_name=light_space_playership_shield_fx.name, duration=0.75,
            smooth=False, diffuse=[0, 0, 0], ambient=[0, 0, 0], time_delay=t)
        t += 0.09
        gun_impact_02.start(group=MAIN, duration=60, time_delay=t)
        t += 0.3
        gun_impact_03.start(group=MAIN, duration=60, time_delay=t)
        t += 0.2
        LightAnimEvent(root=self, group=MAIN, object_name=light_room.name, duration=0, smooth=False,
            diffuse=[0.6, 0.6, 0.6], ambient=[0.3, 0.3, 0.3], time_delay=t)
        t += 0.3
        gun_impact_04.start(group=MAIN, duration=60, time_delay=t)
        t += 0.4
        gun_impact_05.start(group=MAIN, duration=60, time_delay=t)
        t += 0.3
        LightAnimEvent(root=self, group=MAIN, object_name=light_space_playership_shield_fx.name, duration=0,
            smooth=False, on=False, time_delay=t)
        cam_launcher_start.move_cam(group=MAIN, index=2, duration=6, smooth=True, time_delay=t)
        t += 0.5
        cam_launcher_start.set(group=MAIN, time_delay=t)
        trent.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0)

        # m07_omega13 60: Rockford.
        # Артефакты переживут уничтожение корабля.
        t = 0
        cam_launcher_start.move_focus(group=MAIN, index=2, duration=5, smooth=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=missile01.name,
            target_name=self.get_automarker_name('mrk_missile01_start_pos'), duration=0.01, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 2
        MotionEvent(root=self, group=MAIN, object_name=launcher01.name, anim='Sc_br_slugger_launcher', duration=1,
            time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=missile01.name,
            target_name=self.get_automarker_name('mrk_missile01_final_hp'), duration=1.99, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.5
        missile_rolling.start(group=MAIN, duration=15, loop=False, start_time=0, time_delay=t)
        t += 1.3
        missile_loaded.start(group=MAIN, duration=15, loop=False, start_time=0, time_delay=t)
        t += 0.199
        AttachEvent(root=self, group=MAIN, target_name=missile01.name, parent_name=launcher01.name, duration=2,
            target_part='HpFire01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True, up='Y_AXIS',
            front='NEG_Z_AXIS', offset_z=-0.7, time_delay=t)
        t += 0.001
        MotionEvent(root=self, group=MAIN, object_name=launcher01.name, anim='Sc_br_slugger_launcher', duration=1,
            start_time=1, trans_time=0.25, time_delay=t)
        t += 1
        RotateAxisEvent(root=self, group=MAIN, object_name=crystal.name, angle=90, axis='X_AXIS', duration=0,
            smooth=False, time_delay=t)
        fx_crystal_light.start(group=MAIN, duration=36000, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_crystal_light.name, parent_name=crystal.name,
            duration=60, target_part='HpRoot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        transponder_reveal.start(group=MAIN, duration=15, loop=False, start_time=0, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_room.name, duration=0, smooth=False, on=False,
            time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_room_backside.name, duration=0, smooth=False,
            on=True, time_delay=t)
        cam_trent_lookback.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TWSTS_LOOK_270LV_XA_03, duration=113, time_scale=0.75,
            time_delay=t)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, object_name=crystal.name, angle=35, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        t += 0.49
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=90, axis='Y_AXIS', duration=3,
            smooth=False, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=chair.name, angle=90, axis='Y_AXIS', duration=3,
            smooth=False, time_delay=t)
        t += 3.5
        cam_trent_walkback.set(group=MAIN, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=chair.name, angle=90, axis='Y_AXIS', duration=2,
            smooth=False, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_WALK_TRNS_270LV_XA_10, duration=25, time_scale=0.6,
            start_time=1.8, trans_time=1, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name, target_name=crystal.name, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS', duration=7, transition_duration=2, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=panel.name,
            target_name=self.get_automarker_name('mrk_panel_open'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=False, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=crystal.name,
            target_name=self.get_automarker_name('mrk_crystal_open'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=False, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=tome.name,
            target_name=self.get_automarker_name('mrk_tome_open'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=False, time_delay=t)
        t += 0.5
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-5, axis='Y_AXIS', duration=1,
            smooth=False, time_delay=t)
        t += 2.5
        LookAtEvent(root=self, group=MAIN, point=cam_flying_missile.name, focus=missile01.name, duration=70,
            target_type='ROOT', target_part='', up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_missile.name, parent_name=missile01.name, duration=25,
            target_part='HpExhaust', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', time_delay=t)
        t += 1
        cam_flying_missile.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=missile01.name,
            target_name=self.get_automarker_name('mrk_missile01_final_hp'), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=missile01.name,
            target_name=self.get_automarker_name('mrk_missile01_firepoint'), duration=18, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MotionEvent(root=self, group=MAIN, object_name=launcher01.name, anim='Sc_br_slugger_launcher', duration=1,
            time_delay=t)
        fx_missile.start(group=MAIN, duration=10, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=missile01.name, angle=3600, axis='Z_AXIS', duration=25,
            smooth=False, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=missile_travel.name, parent_name=missile01.name,
            duration=15, target_part='HpEngine01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            entity_relative=True, up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        missile_travel.start(group=MAIN, duration=15, loop=True, start_time=0, time_delay=t)
        missile_launch.start(group=MAIN, duration=5, loop=False, start_time=0, time_delay=t)
        missile_travel.change_attenuation(group=MAIN, duration=3, attenuation=-5, time_delay=t)
        t += 4
        MoveEvent(root=self, group=MAIN, object_name=missile02.name,
            target_name=self.get_automarker_name('mrk_missile02_start_pos'), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1
        LightAnimEvent(root=self, group=MAIN, object_name=light_room_backside.name, duration=0, smooth=False,
            on=False, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_room.name, duration=0, smooth=False, on=True,
            time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_before_touch'), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.25
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-35, axis='Y_AXIS', duration=0,
            smooth=False, time_delay=t)
        t += 0.75
        MoveEvent(root=self, group=MAIN, object_name=crystal.name,
            target_name=self.get_automarker_name('mrk_crystal_open2'), duration=0, smooth=True, adjust_pos=True,
            adjust_orient=False, time_delay=t)
        cam_trent_touch.move_focus(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        t += 1
        missile_travel.change_attenuation(group=MAIN, duration=5, attenuation=-100, time_delay=t)
        cam_trent_touch.set(group=MAIN, time_delay=t)
        cam_trent_touch.move_cam(group=MAIN, index=2, duration=10, smooth=True, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_SPCBODY_s027x_Trent_XA_STND_000DN_16, duration=8.5, time_scale=0.3,
            start_time=4, time_delay=t)
        t += 1
        AttachEvent(root=self, group=MAIN, target_name=fx_missile_alt.name, parent_name=missile02.name,
            duration=25, target_part='HpExhaust', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=missile02.name,
            target_name=self.get_automarker_name('mrk_missile02_final_pos'), duration=15, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        RotateAxisEvent(root=self, group=MAIN, object_name=missile02.name, angle=3600, axis='Z_AXIS', duration=25,
            smooth=False, time_delay=t)
        fx_missile_alt.start(group=MAIN, duration=25, time_delay=t)
        t += 0.5
        ConnectHardpointEvent(root=self, group=MAIN, target_name=crystal.name, parent_name=trent.name,
            duration=20, target_hardpoint='HpProp_Connect', parent_hardpoint='HpLeftConnect', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_crystal_touch.name, parent_name=crystal.name,
            duration=60, target_part='HpFX', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', offset_y=0.05, time_delay=t)
        fx_crystal_touch.start(group=MAIN, duration=30, time_delay=t)
        fx_crystal_touch_mega_effect.start(group=MAIN, duration=30, time_delay=t)
        transponder_activates.start(group=MAIN, duration=15, loop=False, start_time=0, time_delay=t)
        t += 4.5
        LightAnimEvent(root=self, group=MAIN, object_name=light_room_backside_nomad_light.name, duration=0,
            smooth=False, on=True, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_room_backside.name, duration=0, smooth=False,
            on=False, time_delay=t)
        LightAnimEvent(root=self, group=MAIN, object_name=light_room.name, duration=0, smooth=False, on=False,
            time_delay=t)
        fx_crystal_touch_mega_effect2.start(group=MAIN, duration=30, time_delay=t)
        cam_trent_missilewatch.set(group=MAIN, time_delay=t)
        cam_trent_missilewatch.change_fov(group=MAIN, duration=3, fov=4, smooth=True, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_player_transponding.name, parent_name=playership.name,
            duration=260, target_part='HpRoot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_player_transponding2.name, parent_name=playership.name,
            duration=260, target_part='HpRoot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_player_transponding3.name, parent_name=playership.name,
            duration=1, target_part='HpRoot', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        t += 4
        RotateAxisEvent(root=self, group=MAIN, object_name=cam_flying_missile_near.name, angle=5, axis='Y_AXIS',
            duration=0, smooth=False, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=fx_missile.name, parent_name=missile01.name, duration=25,
            target_part='HpExhaust', target_type='HARDPOINT', adjust_pos=True, adjust_orient=False, up='Y_AXIS',
            front='NEG_Z_AXIS', time_delay=t)
        t += 0.01
        RotateAxisEvent(root=self, group=MAIN, object_name=cam_flying_missile_near.name, angle=-3, axis='X_AXIS',
            duration=0, smooth=False, time_delay=t)
        t += 0.49
        MoveEvent(root=self, group=MAIN, object_name=missile01.name,
            target_name=self.get_automarker_name('mrk_missile01_fly2_start_pos'), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.5
        fx_player_transponding.start(group=MAIN, duration=235, time_delay=t)
        cam_flying_missile_near.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=cam_flying_missile_near.name,
            target_name=self.get_automarker_name('cam_flying_missile_near_pos2'), duration=10, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=missile01.name,
            target_name=self.get_automarker_name('mrk_missile01_fly2_final_pos'), duration=10, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        AttachEvent(root=self, group=MAIN, target_name=missile_travel2.name, parent_name=missile01.name,
            duration=60, target_part='HpEngine01', target_type='HARDPOINT', adjust_pos=True, adjust_orient=True,
            entity_relative=True, up='Y_AXIS', front='NEG_Z_AXIS', time_delay=t)
        missile_travel2.start(group=MAIN, duration=55, loop=True, start_time=0, time_delay=t)
        fx_missile.start(group=MAIN, duration=25, time_delay=t)
        t += 2
        fx_player_transponding2.start(group=MAIN, duration=2, time_delay=t)
        t += 1
        fx_player_transponding3.start(group=MAIN, duration=5, time_delay=t)
        t += 1
        cam_player_disappeared.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=playership.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 3
        missile_travel.change_attenuation(group=MAIN, duration=5, attenuation=-100, time_delay=t)
        t += 5
        music_background.change_attenuation(group=MAIN, duration=1, attenuation=-100, time_delay=t)
        line_sound = self.lookup_single_sound(60)
        SoundEvent(root=self, group=MAIN, sound_name=line_sound.get_nickname())
        main_group.append_time(45)
