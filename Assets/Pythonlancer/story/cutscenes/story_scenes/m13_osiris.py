from story.cutscenes.scene import Scene
from story.cutscenes.content import *
from story.cutscenes.anim import Male, Female, Trent

from story import actors


class EliteShip(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite2'


class Msn13OsirisScene(Scene):
    POINT_ROTATE_OVERRIDES = {
        'trent_walk': (0, 135, 0),
        'darcy_walk': (0, 135, 0),
        'trent_quest': (0, 135, 0),
        'darcy_quest': (0, 135, 0),
    }

    def action(self):
        main_group = self.get_group(MAIN)

        # CAMERAS

        cam_dbg = LookAtCamera(root=self, name='cam_dbg', fov=30)
        cam_start = LookAtCamera(root=self, name='cam_start', fov=24)
        cam_brief = LookAtCamera(root=self, name='cam_brief', fov=24)
        cam_quest = LookAtCamera(root=self, name='cam_quest', fov=18)
        cam_answer = LookAtCamera(root=self, name='cam_answer', fov=18)
        cam_brief_end = LookAtCamera(root=self, name='cam_brief_end', fov=20)
        cam_alaric = LookAtCamera(root=self, name='cam_alaric', fov=18)
        cam_final = LookAtCamera(root=self, name='cam_final', fov=20)

        # PROPS

        alarm = Music(root=self, name='alarm', sound='rtc_klaxon_loop_3', attenuation=-12)

        alarm.start(group=MAIN, duration=1030, loop=True)
        alarm.change_attenuation(group=MAIN, duration=2, attenuation=-20, time_delay=4)

        elite_ship = EliteShip(root=self, name='liberty_elite_ship', init_point='ship', light_group=3, rotate_y=-110,
                               loadout='rtc_m13_osiris_ship')


        start_diffuse = [0.2, 0, 0]
        end_diffuse = [1, 0.2, 0.2]
        start_diffuse2 = [0.2, 0, 0]
        end_diffuse2 = [1, 0, 0]
        light_anim_repeat = 100
        light_anim_repeat2 = 200

        set_ambi = Light(root=self, name='ambi_LtG09_Direct_Set_Amb', point_name=self.DEFAULT_POINT_NAME,
                         light_group=9, diffuse=[0, 0, 0], extra_name='', is_reference=True,
                         ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_DIRECT, range=2000, cutoff=150)
        ship_ambi = Light(root=self, name='ambi_LtG03_PShip_Orng_3oc_Spt', point_name=self.DEFAULT_POINT_NAME,
                          light_group=3, diffuse=[0, 0, 0], extra_name='', is_reference=True,
                          ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_DIRECT, range=2000, cutoff=150)

        char_ambi = Light(root=self, name='main_ambi_ltg01', point_name=self.DEFAULT_POINT_NAME,
                          light_group=1, diffuse=[0.22, 0.2, 0.15],
                          ambient=[0.15, 0.15, 0.15], direction=[0, 0, -1], light_type=L_DIRECT, range=2000, cutoff=150)

        spinner1 = Light(root=self, name='spinner1a', point_name='spinner1', light_group=9, diffuse=start_diffuse2,
                         ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_POINT, range=2000, cutoff=150)
        spinner2 = Light(root=self, name='spinner1b', point_name='spinner3', light_group=3, diffuse=start_diffuse,
                         ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_POINT, range=2000, cutoff=150)
        spinner3 = Light(root=self, name='spinner1c', point_name='spinner2', light_group=1, diffuse=start_diffuse,
                         ambient=[0, 0, 0], direction=[0, 0, 1], light_type=L_POINT, range=2000, cutoff=150)

        set_ambi.set_ambient(group=BG, duration=0.1, ambient=[0.25,0.25,0.25])
        ship_ambi.turn_off(group=BG)

        anim2_grp = 'anim2'
        anim3_grp = 'anim3'
        self.clone_group(anim2_grp, BG).append_time(0.2)
        self.clone_group(anim3_grp, BG).append_time(0.35)

        spinner1.animate_diffuse(BG, 'spinner1_anim1', start_diffuse=start_diffuse2, end_diffuse=end_diffuse2,
                                 duration=0.5, start_gap=0.5, end_gap=0.5, smooth=True, repeat=light_anim_repeat2)

        spinner2.animate_diffuse(anim2_grp, 'spinner1_anim2', start_diffuse=start_diffuse, end_diffuse=end_diffuse,
                                 duration=0.5, start_gap=0.5, end_gap=0.5, smooth=True, repeat=light_anim_repeat)

        spinner3.animate_diffuse(anim3_grp, 'spinner1_anim3', start_diffuse=start_diffuse, end_diffuse=end_diffuse,
                                 duration=0.5, start_gap=0.5, end_gap=0.5, smooth=True, repeat=light_anim_repeat2)


        # CHARACTERS

        trent = Character(root=self, actor=actors.Trent, light_group=1, init_point='trent_init', rotate_y=135)
        king = Character(root=self, actor=actors.King, light_group=1, init_point='king_init', rotate_y=-45)
        alaric = Character(root=self, actor=actors.Alaric, light_group=1, init_point='alaric_init', rotate_y=220)
        darcy = Character(root=self, actor=actors.Darcy, light_group=1, init_point='darcy_init', rotate_y=-45)

        male1 = Character(root=self, actor=actors.OsirisMaleElite1, light_group=1, init_point='male1', rotate_y=180)
        male2 = Character(root=self, actor=actors.OsirisMaleElite2, light_group=1, init_point='male2', rotate_y=125)
        male3 = Character(root=self, actor=actors.OsirisMaleElite3, light_group=1, init_point='male3', rotate_y=25)
        male4 = Character(root=self, actor=actors.OsirisMaleElite4, light_group=1, init_point='male4', rotate_y=85)
        major = Character(root=self, actor=actors.MajorScrew, light_group=1, init_point='major', rotate_y=60)

        female1 = Character(root=self, actor=actors.OsirisFemaleElite1, light_group=1, init_point='female1', rotate_y=135)
        female2 = Character(root=self, actor=actors.OsirisFemaleElite2, light_group=1, init_point='female2', rotate_y=25)
        female3 = Character(root=self, actor=actors.OsirisFemaleElite3, light_group=1, init_point='female3', rotate_y=230)
        female4 = Character(root=self, actor=actors.OsirisFemaleElite4, light_group=1, init_point='female4', rotate_y=170)

        chars = [
            trent, alaric, darcy, major,
            male1, male2, male3, male4,
            female1, female2, female3, female4,
        ]

        background_chars = [
            major,
            male1, male2, male3, male4,
            female1, female2, female3, female4,
        ]

        elite_ship.anim(group=BG, anim='Sc_force extend')

        # MARKERS

        mrk_king = trent.get_stand_marker('king_init')
        mrk_trent_quest = trent.get_stand_marker('trent_quest')
        mrk_alaric = trent.get_stand_marker('alaric_init')

        mrk_female4 = female4.get_stand_marker('female4')
        mrk_female1 = female1.get_stand_marker('female1')
        mrk_male2 = male3.get_stand_marker('male2')
        mrk_male1 = male1.get_stand_marker('male1')
        mrk_major = trent.get_stand_marker('major')

        mrk_trent_talk = self.get_automarker_name('mrk_trent_talk')
        mrk_trent_front = self.get_automarker_name('mrk_trent_front')
        mrk_darcy_talk = self.get_automarker_name('mrk_darcy_talk')
        mrk_darcy_front = self.get_automarker_name('mrk_darcy_front')


        # PREPARE

        for char in chars:
            char.move_head_ik(group=BG, target_name=mrk_king, immediately=True)
        female2.move_eye_ik(group=BG, target_name=mrk_king, immediately=True)

        king.move_head_ik(group=BG, target_name=mrk_female1, immediately=True)
        king.move_eye_ik(group=BG, target_name=mrk_female1, immediately=True)

        # ACTION!


        king.motion(group=MAIN, duration=30, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)

        trent.motion(group=MAIN, duration=12, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_WALK_TRNS_180LV_XA_02, time_delay=4)
        darcy.motion(group=MAIN, duration=11, loop=True, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, time_delay=6.475)
        RotateAxisEvent(root=self, group=MAIN, object_name=darcy.name, angle=5, duration=1, smooth=True, time_delay=6)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=-5, duration=10)

        cam_start.set(group=MAIN)
        cam_start.move_cam(group=MAIN, index=2, duration=6, smooth=True)
        cam_start.move_focus(group=MAIN, index=2, duration=6, smooth=True)

        main_group.append_time(4)
        darcy.facial(group=MAIN, index=10)

        main_group.append_time(1)

        MoveOffscreenEvent(root=self, group=MAIN, object_name=trent.name)
        MoveOffscreenEvent(root=self, group=MAIN, object_name=darcy.name)

        cam_brief.set(group=MAIN)
        cam_brief.move_cam(group=MAIN, index=2, duration=15, smooth=True)
        cam_brief.move_focus(group=MAIN, index=2, duration=15, smooth=True)
        cam_brief.move_cam(group=MAIN, index=3, duration=15, smooth=True, time_delay=17)
        cam_brief.move_focus(group=MAIN, index=3, duration=15, smooth=True, time_delay=17)
        cam_brief.move_cam(group=MAIN, index=4, duration=15, smooth=True, time_delay=33)
        cam_brief.move_focus(group=MAIN, index=4, duration=15, smooth=True, time_delay=33)

        arrive_trent = 'TRENT_ARRIVE'
        arrive_trent_group = self.clone_group(arrive_trent, MAIN)

        arrive_trent_group.append_time(8)

        MoveFastEvent(root=self, group=arrive_trent, object_name=trent.name, target_name=self.get_automarker_name('trent_walk'))
        trent.motion(group=arrive_trent, duration=1.3*1, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01)
        trent.motion(group=arrive_trent, duration=10, anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, time_delay=1.3*1)

        trent.motion(group=arrive_trent, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=4)
        trent.motion(group=arrive_trent, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=14)
        trent.motion(group=arrive_trent, duration=20, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=0.5, time_delay=18)
        trent.motion(group=arrive_trent, duration=20,  anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, time_scale=0.8, trans_time=1, time_delay=24)

        MoveFastEvent(root=self, group=arrive_trent, object_name=darcy.name, target_name=self.get_automarker_name('darcy_walk'))
        darcy.motion(group=arrive_trent, duration=2.65, loop=True, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01)
        darcy.motion(group=arrive_trent, duration=3, anim=Female.Sc_FMBODY_WALK_STND_TRNS_000LV_XA_01, time_delay=2.65)
        darcy.motion(group=arrive_trent, duration=3, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, time_delay=6)
        darcy.motion(group=arrive_trent, duration=3, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, time_delay=13)
        darcy.motion(group=arrive_trent, duration=3, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_delay=18)
        darcy.motion(group=arrive_trent, duration=5, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=28)

        arrive_trent_group.append_time(1)

        trent.start_head_ik(group=arrive_trent, duration=1000)
        trent.start_eye_ik(group=arrive_trent, duration=1000)
        darcy.start_head_ik(group=arrive_trent, duration=1000)
        darcy.start_eye_ik(group=arrive_trent, duration=1000)

        bg_chars = 'BG_CHARS'
        bg_chars_group = self.clone_group(bg_chars, MAIN)

        male1.motion(group=bg_chars, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        male2.motion(group=bg_chars, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        male3.motion(group=bg_chars, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        male4.motion(group=bg_chars, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        major.motion(group=bg_chars, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        alaric.motion(group=bg_chars, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)

        female1.motion(group=bg_chars, duration=10, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)
        female2.motion(group=bg_chars, duration=10, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)
        female3.motion(group=bg_chars, duration=10, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)
        female4.motion(group=bg_chars, duration=10, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)

        major.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=0.5, time_delay=2)
        major.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, trans_time=0.5, time_delay=7)
        # major.motion(group=bg_chars, duration=5, anim=Male.Sc_FMBODY_STND_IDLE_000LV_xa_05, trans_time=0.5, time_delay=11)
        major.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=12)
        major.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=0.5, time_delay=17)
        major.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, trans_time=0.5, time_delay=21)

        female1.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=1)
        female1.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=6)
        female1.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, trans_time=0.5, time_delay=10)
        female1.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, trans_time=0.5, time_delay=15)
        female1.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=20)
        female1.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=28)
        female1.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, trans_time=0.5, time_delay=32)

        female2.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=4)
        female2.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, trans_time=2, time_delay=15)
        female3.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=6)
        female3.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=12)
        female3.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_LEAN_LLEG_000LV_XA_01, trans_time=0.5, time_delay=17)
        female3.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, trans_time=1, time_delay=20)
        female3.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_LEAN_LLEG_000LV_XA_01, trans_time=0.5, time_delay=24)
        female3.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05, trans_time=1, time_delay=27)
        female4.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_02, trans_time=0.5, time_delay=1)
        female4.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_ATEASE_RLEASE_000LV_XA_02, trans_time=0.5, time_delay=12)
        female4.motion(group=bg_chars, duration=5, anim=Female.Sc_FMBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_02, trans_time=0.5, time_delay=18)

        male1.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, trans_time=0.5, time_delay=6)
        male2.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=4)
        male2.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=10)
        male2.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_LEAN_RLEG_000LV_XA_02, trans_time=0.5, time_delay=16)
        male2.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=1, time_delay=21)
        male3.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, trans_time=0.5, time_delay=6)
        male4.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, trans_time=0.5, time_delay=14)

        alaric.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_LEAN_LLEG_000LV_XA_02, trans_time=0.5, time_delay=3)
        alaric.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=2, time_delay=10)
        alaric.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_LEAN_RLEG_000LV_XA_02, trans_time=0.5, time_delay=15)
        alaric.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=2, time_delay=17)
        alaric.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, trans_time=2, time_delay=20)
        alaric.motion(group=bg_chars, duration=5, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, trans_time=2, time_delay=27)

        bg_chars_group.append_time(0.1)
        side_iks = []

        bg_ik_time = main_group.get_time()

        for char in background_chars:
            side_iks.append(
                char.start_head_ik(group=bg_chars, duration=1000)
            )
        side_iks.extend([
            female2.start_eye_ik(group=bg_chars, duration=1000),
            king.start_head_ik(group=MAIN, duration=1000),
            king.start_eye_ik(group=MAIN, duration=1000)
        ])

        alaric.start_head_ik(group=MAIN, duration=1000)
        alaric.start_eye_ik(group=MAIN, duration=1000)



        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, time_scale=0.5, time_delay=2)

        # main_group.append_time(1000)
        main_group.append_time(1)

        king.move_head_ik(group=MAIN, target_name=mrk_female4, duration=2.3, time_delay=-1)
        king.move_eye_ik(group=MAIN, target_name=mrk_female4, duration=0.8, time_delay=-1)

        king.move_head_ik(group=MAIN, target_name=mrk_female1, duration=2.3, time_delay=2)
        king.move_eye_ik(group=MAIN, target_name=mrk_female1, duration=0.8, time_delay=2)

        king.move_head_ik(group=MAIN, target_name=mrk_male2, duration=2.3, time_delay=5)
        king.move_eye_ik(group=MAIN, target_name=mrk_male2, duration=0.8, time_delay=5)

        king.move_head_ik(group=MAIN, target_name=mrk_female1, duration=3, time_delay=8)
        king.move_eye_ik(group=MAIN, target_name=mrk_female1, duration=1.2, time_delay=8)

        king.move_head_ik(group=MAIN, target_name=mrk_major, duration=2.3, time_delay=11)
        king.move_eye_ik(group=MAIN, target_name=mrk_major, duration=0.8, time_delay=11)

        king.move_head_ik(group=MAIN, target_name=mrk_male2, duration=2.3, time_delay=15)
        king.move_eye_ik(group=MAIN, target_name=mrk_male2, duration=0.8, time_delay=15)

        king.move_head_ik(group=MAIN, target_name=mrk_female4, duration=3.2, time_delay=18)
        king.move_eye_ik(group=MAIN, target_name=mrk_female4, duration=1.5, time_delay=18)

        king.move_head_ik(group=MAIN, target_name=mrk_male1, duration=2.3, time_delay=21)
        king.move_eye_ik(group=MAIN, target_name=mrk_male1, duration=0.8, time_delay=21)

        king.move_head_ik(group=MAIN, target_name=mrk_female1, duration=2.3, time_delay=24)
        king.move_eye_ik(group=MAIN, target_name=mrk_female1, duration=0.8, time_delay=24)

        king.move_head_ik(group=MAIN, target_name=mrk_major, duration=3.2, time_delay=27)
        king.move_eye_ik(group=MAIN, target_name=mrk_major, duration=1.5, time_delay=27)

        king.move_head_ik(group=MAIN, target_name=mrk_male2, duration=2.3, time_delay=30)
        king.move_eye_ik(group=MAIN, target_name=mrk_male2, duration=0.8, time_delay=30)


        king.move_head_ik(group=MAIN, target_name=mrk_female4, duration=2.3, time_delay=33)
        king.move_eye_ik(group=MAIN, target_name=mrk_female4, duration=0.8, time_delay=33)

        king.move_head_ik(group=MAIN, target_name=mrk_female1, duration=2.3, time_delay=36)
        king.move_eye_ik(group=MAIN, target_name=mrk_female1, duration=0.8, time_delay=36)

        king.move_head_ik(group=MAIN, target_name=mrk_male2, duration=2.3, time_delay=39)
        king.move_eye_ik(group=MAIN, target_name=mrk_male2, duration=0.8, time_delay=39)

        king.move_head_ik(group=MAIN, target_name=mrk_female1, duration=3, time_delay=42)
        king.move_eye_ik(group=MAIN, target_name=mrk_female1, duration=1.2, time_delay=42)

        king.move_head_ik(group=MAIN, target_name=mrk_major, duration=2.3, time_delay=45)
        king.move_eye_ik(group=MAIN, target_name=mrk_major, duration=0.8, time_delay=45)

        king.move_head_ik(group=MAIN, target_name=mrk_male2, duration=2.3, time_delay=48)
        king.move_eye_ik(group=MAIN, target_name=mrk_male2, duration=0.8, time_delay=48)




        king.facial(group=MAIN, index=20)
        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, time_scale=0.5, time_delay=4)
        king.facial(group=MAIN, index=30)

        king.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xa_04, start_time=2, trans_time=1, time_delay=2, time_scale=0.8)
        king.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, start_time=0, time_delay=2.5, trans_time=0.2)
        king.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTL_CASL_000LV_00, start_time=0, time_delay=2.5, trans_time=0.2)

        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, trans_time=1, time_delay=12, time_scale=0.8)
        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_LEFT_000LV_00, start_time=0, time_delay=12, trans_time=0.2)
        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_RGHT_000LV_00, start_time=0, time_delay=12, trans_time=0.2)

        king.facial(group=MAIN, index=50)
        king.facial(group=MAIN, index=60)

        king.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, trans_time=1, time_delay=0, time_scale=0.8)
        king.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, start_time=1, trans_time=0.2)

        king.facial(group=MAIN, index=70)


        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, trans_time=1, time_delay=0, time_scale=0.8)
        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_LEFT_000LV_00, start_time=0, time_delay=0, trans_time=0.2)
        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_RGHT_000LV_00, start_time=0, time_delay=0, trans_time=0.2)

        king.facial(group=MAIN, index=80)

        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_ATEASE_HSEC_RLEASE_000LV_XA_03, time_scale=0.5, time_delay=-2)

        king.facial(group=MAIN, index=90)


        cam_quest.set(group=MAIN)


        male2.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_LEAN_RLEG_000LV_XA_02, trans_time=0.5, time_delay=-0.5)
        male2.motion(group=MAIN, duration=5, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=1, time_delay=2)
        female1.motion(group=MAIN, duration=5, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, time_scale=0.5, trans_time=0.5, time_delay=0.5)

        trent.facial(group=MAIN, index=100)

        cam_answer.set(group=MAIN)
        cam_answer.move_cam(group=MAIN, index=2, duration=15, smooth=True)
        cam_answer.move_focus(group=MAIN, index=2, duration=15, smooth=True)

        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, time_scale=0.6, time_delay=1)

        king.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, trans_time=1, time_delay=2, time_scale=0.8)
        king.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, start_time=1, trans_time=0.2)

        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, trans_time=1, time_delay=7, time_scale=0.8)
        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_LEFT_000LV_00, start_time=0, time_delay=7, trans_time=0.2)
        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_RGHT_000LV_00, start_time=0, time_delay=7, trans_time=0.2)

        female2.motion(group=MAIN, duration=8, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, time_scale=0.7, trans_time=1, time_delay=1)

        female2.move_head_ik(group=MAIN, target_name=mrk_trent_quest, duration=2.3, time_delay=0)
        female2.move_eye_ik(group=MAIN, target_name=mrk_trent_quest, duration=0.8, time_delay=0)
        female2.move_head_ik(group=MAIN, target_name=mrk_king, duration=2.7, time_delay=4.5)
        female2.move_eye_ik(group=MAIN, target_name=mrk_king, duration=1, time_delay=4.5)

        king.move_head_ik(group=MAIN, target_name=mrk_trent_quest, duration=2.3, time_delay=0)
        king.move_eye_ik(group=MAIN, target_name=mrk_trent_quest, duration=0.8, time_delay=0)

        king.move_head_ik(group=MAIN, target_name=mrk_male2, duration=2.3, time_delay=3)
        king.move_eye_ik(group=MAIN, target_name=mrk_male2, duration=0.8, time_delay=3)

        king.move_head_ik(group=MAIN, target_name=mrk_female1, duration=2.3, time_delay=6)
        king.move_eye_ik(group=MAIN, target_name=mrk_female1, duration=0.8, time_delay=6)

        king.facial(group=MAIN, index=110)

        king.move_head_ik(group=MAIN, target_name=mrk_female4, duration=1.3, time_delay=0)
        king.move_eye_ik(group=MAIN, target_name=mrk_female4, duration=0.8, time_delay=0)

        king.move_head_ik(group=MAIN, target_name=mrk_female1, duration=1.3, time_delay=2)
        king.move_eye_ik(group=MAIN, target_name=mrk_female1, duration=0.8, time_delay=2)

        king.facial(group=MAIN, index=120)

        end_time = main_group.get_time() - bg_ik_time
        for ik in side_iks:
            ik.set_duration(end_time)

        king.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_WALK_TRNS_270LV_XA_02,  trans_time=0.5)
        female2.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_WALK_TRNS_180LV_XA_02,  trans_time=0.5, time_delay=-0.1)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, time_scale=1)

        #
        # main_group.append_time(1000)
        #
        # self.set_start_time(main_group.get_time())


        # trent.start_head_ik(group=MAIN, duration=1000)
        # trent.start_eye_ik(group=MAIN, duration=1000)
        # darcy.start_head_ik(group=MAIN, duration=1000)
        # darcy.start_eye_ik(group=MAIN, duration=1000)
        # alaric.start_head_ik(group=MAIN, duration=1000)
        # alaric.start_eye_ik(group=MAIN, duration=1000)

        main_group.append_time(1)

        cam_brief_end.set(group=MAIN)
        cam_brief_end.move_cam(group=MAIN, index=2, duration=15, smooth=True)
        cam_brief_end.move_focus(group=MAIN, index=2, duration=15, smooth=True)
        cam_brief_end.move_cam(group=MAIN, index=3, duration=10, smooth=True, time_delay=15)
        cam_brief_end.move_focus(group=MAIN, index=3, duration=10, smooth=True, time_delay=15)

        MoveOffscreenEvent(root=self, group=MAIN, object_name=king.name)
        MoveOffscreenEvent(root=self, group=MAIN, object_name=female2.name)
        MoveOffscreenEvent(root=self, group=MAIN, object_name=female3.name)
        MoveOffscreenEvent(root=self, group=MAIN, object_name=elite_ship.name)

        MoveFastEvent(root=self, group=MAIN, object_name=trent.name, target_name=self.get_automarker_name('trent_quest'))
        MoveFastEvent(root=self, group=MAIN, object_name=darcy.name, target_name=self.get_automarker_name('darcy_quest'))


        male1.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        male1.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_WALK_TRNS_180LV_XA_02, time_delay=0.3)
        male1.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, time_delay=3)
        RotateAxisEvent(root=self, group=MAIN, object_name=male1.name, angle=30, duration=1, smooth=True, time_delay=1)
        RotateAxisEvent(root=self, group=MAIN, object_name=male1.name, angle=-70, duration=1, smooth=True, time_delay=2.9)

        male2.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_WALK_TRNS_000LV_XA_01)
        male2.motion(group=MAIN, duration=20, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, time_delay=1.06)
        RotateAxisEvent(root=self, group=MAIN, object_name=male2.name, angle=-40, duration=4, smooth=True, time_delay=0.3)

        male3.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)
        male4.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_FSTHIPB_HOLD_000LV_XA_02)
        male4.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02, trans_time=1, time_delay=1)
        major.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_WALK_TRNS_090LV_XA_02)
        major.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, time_delay=2.475)
        alaric.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04)

        darcy.motion(group=MAIN, duration=10, loop=True, anim=Female.Sc_FMBODY_STND_IDLE_000LV_xa_05)
        female1.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_WALK_TRNS_180LV_XA_02)
        female1.motion(group=MAIN, duration=50, loop=True, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, time_delay=2.475)
        RotateAxisEvent(root=self, group=MAIN, object_name=female1.name, angle=-40, duration=1, smooth=True, time_delay=0.3)
        RotateAxisEvent(root=self, group=MAIN, object_name=female1.name, angle=40, duration=1, smooth=True, time_delay=1.4)

        female4.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_WALK_TRNS_000LV_XA_01)
        female4.motion(group=MAIN, duration=10, loop=True, anim=Female.Sc_FMBODY_WLKG_000LV_XA_01, time_delay=1.46)
        RotateAxisEvent(root=self, group=MAIN, object_name=female4.name, angle=-60, duration=3, smooth=True, time_delay=0.3)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_2STEP_FRWD_TRNS_000LV_XA_02, trans_time=0.25, time_delay=1)
        RotateAxisEvent(root=self, group=MAIN, object_name=trent.name, angle=60, duration=2, smooth=True, time_delay=1)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=0.25, time_delay=4)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_1STEP_SIDWYSL_000LV_XA_02, time_delay=1.4)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, trans_time=0.5, time_delay=3.6)

        alaric.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_TURN_045LV_XA_04, trans_time=0.25, time_delay=1)
        RotateAxisEvent(root=self, group=MAIN, object_name=alaric.name, angle=20, duration=1, smooth=True, time_delay=1)

        trent.move_head_ik(group=MAIN, target_name=mrk_alaric, duration=2.3, time_delay=0)
        trent.move_eye_ik(group=MAIN, target_name=mrk_alaric, duration=0.8, time_delay=0)
        darcy.move_head_ik(group=MAIN, target_name=mrk_alaric, duration=2.3, time_delay=1)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_alaric, duration=0.8, time_delay=1)
        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=2.3, time_delay=1)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.8, time_delay=1)



        main_group.append_time(1.6)

        trent.facial(group=MAIN, index=200)




        alaric.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, trans_time=0.25, time_delay=0.15)
        alaric.facial(group=MAIN, index=210)

        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_CONV_RHND_CASL_000LV_xa_01, trans_time=1, time_delay=0, time_scale=0.8)
        trent.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, start_time=1, trans_time=0.2)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2.3, time_delay=-2)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.8, time_delay=-2)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, trans_time=0.5, time_delay=2)

        trent.facial(group=MAIN, index=220)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CONV_RHNDDN_TRNS_000LV_XA_02, trans_time=1, time_delay=-2, time_scale=0.8)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_LEFT_000LV_00, start_time=0, time_delay=-2, trans_time=0.2)
        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_RGHT_000LV_00, start_time=0, time_delay=-2, trans_time=0.2)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CROSS_ARMS_000LV_xa_06, trans_time=1, time_delay=1, time_scale=0.8)

        darcy.move_head_ik(group=MAIN, target_name=mrk_alaric, duration=2.3, time_delay=1)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_alaric, duration=0.8, time_delay=1)

        alaric.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, trans_time=0.25, time_delay=0.15)
        alaric.motion(group=MAIN, duration=30, loop=True, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, trans_time=0.25, time_delay=4)

        alaric.facial(group=MAIN, index=230)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2.3, time_delay=-0.2)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.8, time_delay=-0.2)

        darcy.move_head_ik(group=MAIN, target_name=mrk_alaric, duration=2.3, time_delay=7)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_alaric, duration=0.8, time_delay=7)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2.3, time_delay=9)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.8, time_delay=9)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_FSTHIPB_HSEC_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=0)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_FSTHIPB_RLEASE_000LV_XA_01, trans_time=0.5, time_delay=6)
        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_CROSS_ARMS_000LV_xa_03, trans_time=0.5, time_delay=10)


        trent.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=2.3, time_delay=-0.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=0.8, time_delay=-0.5)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_UNCRSS_ARMS_000LV_XA_02, trans_time=1, time_delay=3, time_scale=0.8)

        RotateAxisEvent(root=self, group=MAIN, object_name=female1.name, angle=-135, duration=4, smooth=True, time_delay=-3)

        alaric.move_head_ik(group=MAIN, target_name=mrk_darcy_talk, duration=2.3, time_delay=1)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=0.8, time_delay=1)

        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=2.3, time_delay=5)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.8, time_delay=5)

        darcy.facial(group=MAIN, index=240)

        trent.move_head_ik(group=MAIN, target_name=mrk_alaric, duration=2.3, time_delay=1)
        trent.move_eye_ik(group=MAIN, target_name=mrk_alaric, duration=0.8, time_delay=1)

        trent.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=2.3, time_delay=3.5)
        trent.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=0.8, time_delay=3.5)

        trent.move_head_ik(group=MAIN, target_name=mrk_alaric, duration=2.3, time_delay=6)
        trent.move_eye_ik(group=MAIN, target_name=mrk_alaric, duration=0.8, time_delay=6)

        trent.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_SHRG_SHLDRS_SMALL_000LV_XA_01, time_scale=0.8, trans_time=0.5, time_delay=2)

        trent.facial(group=MAIN, index=250)

        MoveOffscreenEvent(root=self, group=MAIN, object_name=female1.name)
        MoveOffscreenEvent(root=self, group=MAIN, object_name=male1.name)


        cam_alaric.set(group=MAIN)

        alaric.move_head_ik(group=MAIN, target_name=mrk_darcy_talk, duration=2.3, time_delay=1)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=0.8, time_delay=1)

        alaric.move_head_ik(group=MAIN, target_name=mrk_trent_talk, duration=2.3, time_delay=3.5)
        alaric.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.8, time_delay=3.5)

        alaric.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLBODY_STND_CONV_HNDS_CASL_000LV_xa_04, start_time=2, trans_time=1, time_delay=0, time_scale=0.8)
        alaric.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTR_CASL_000LV_00, start_time=0, time_delay=0.5, trans_time=0.2)
        alaric.motion(group=MAIN, duration=10, loop=True, anim=Male.Sc_MLHAND_HNEUT_GESTL_CASL_000LV_00, start_time=0, time_delay=0.5, trans_time=0.2)

        alaric.motion(group=MAIN, duration=10, anim=Male.Sc_MLBODY_STND_CONV_HNDSDN_TRNS_000LV_XA_01, trans_time=1, time_delay=4, time_scale=0.8)
        alaric.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_LEFT_000LV_00, start_time=0, time_delay=4, trans_time=0.2)
        alaric.motion(group=MAIN, duration=10, anim=Male.Sc_MLHAND_HNEUT_EDGE_RGHT_000LV_00, start_time=0, time_delay=4, trans_time=0.2)

        alaric.facial(group=MAIN, index=260)


        cam_final.set(group=MAIN)
        cam_final.move_cam(group=MAIN, index=2, duration=6, smooth=True)
        cam_final.move_focus(group=MAIN, index=2, duration=6, smooth=True)

        darcy.move_head_ik(group=MAIN, target_name=mrk_alaric, duration=2.3, time_delay=-2)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_alaric, duration=0.8, time_delay=-2)

        darcy.move_head_ik(group=MAIN, target_name=mrk_trent_front, duration=2.3, time_delay=2)
        darcy.move_eye_ik(group=MAIN, target_name=mrk_trent_talk, duration=0.8, time_delay=2)

        darcy.motion(group=MAIN, duration=10, anim=Female.Sc_FMBODY_STND_UNCRSS_ARMS_000LV_XA_03, trans_time=0.5, time_delay=1)


        trent.move_head_ik(group=MAIN, target_name=mrk_darcy_front, duration=2.3, time_delay=1)
        trent.move_eye_ik(group=MAIN, target_name=mrk_darcy_talk, duration=0.8, time_delay=1)

        trent.move_head_ik(group=MAIN, target_name=mrk_alaric, duration=2.3, time_delay=4)
        trent.move_eye_ik(group=MAIN, target_name=mrk_alaric, duration=0.8, time_delay=4)

        darcy.facial(group=MAIN, index=270)

        trent.facial(group=MAIN, index=280)

        main_group.append_time(1)
