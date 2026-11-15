"""m06_order_deck: постановка для ручного редактирования.

Точки: SCENES/m06_order_deck.blend → DUMPS/m06_order_deck.json.
Создание объектов — в начале action(); далее вход, реплики и выход.
t — смещение внутри текущего блока; facial()/append_time() двигают часы.
Исходные события и их номера сохранены в отчёте декомпиляции.
"""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character,
    EyeIkEvent,
    LookAtCamera,
    MAIN,
    MotionEvent,
    MotionPath,
    MoveEvent,
    NeckIkEvent,
    PlayerShip,
    Ship,
    Sound,
    SoundEvent,
    StaticCamera,
)
from story.cutscenes.anim import (
    Male,
    Trent,
)
from story.cutscenes.source_extensions import (
    SourcePathEvent,
    preserve_entity,
)
from story import actors


class PropPlayership(Ship):
    COMPOUND_TEMPLATE_NAME = 'PlayerShip'
    SRT_GRP = 0
    USR_FLG = 0


class PropPrisonersShip02(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'
    SRT_GRP = 0
    USR_FLG = 0


class PropPrisonersShip03(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'
    SRT_GRP = 0
    USR_FLG = 0


class PropTestVehicle(Ship):
    COMPOUND_TEMPLATE_NAME = 'li_elite'
    SRT_GRP = 0
    USR_FLG = 0


class ExtraCharPrisoner1(actors.Actor):
    NAME = 'prisoner1'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner01'
    GAME_ACTOR = 'Prisoner1'


class ExtraCharPrisoner2(actors.Actor):
    NAME = 'prisoner2'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner02'
    GAME_ACTOR = 'Prisoner2'


class ExtraCharPrisoner3(actors.Actor):
    NAME = 'prisoner3'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner03'
    GAME_ACTOR = 'Prisoner3'


class ExtraCharPrisoner4(actors.Actor):
    NAME = 'prisoner4'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_asf_prisoner04'
    GAME_ACTOR = 'Prisoner4'


class ExtraCharCommander(actors.Actor):
    NAME = 'commander'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_gunner_leader'
    GAME_ACTOR = 'Gunner_commander'


class ExtraCharGunner01(actors.Actor):
    NAME = 'gunner01'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_gunner_sides1'
    GAME_ACTOR = 'Gunner2'


class ExtraCharGunner02(actors.Actor):
    NAME = 'gunner02'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_gunner_sides2'
    GAME_ACTOR = 'Gunner3'


class ExtraCharGunner03(actors.Actor):
    NAME = 'gunner03'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_gunner_back1'
    GAME_ACTOR = 'Gunner4'


class ExtraCharGunner04(actors.Actor):
    NAME = 'gunner04'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_gunner_back2'
    GAME_ACTOR = 'Gunner5'


class ExtraCharSydGuard(actors.Actor):
    NAME = 'syd_guard'
    TYPE = 'male'
    CUTSCENE_APPEARANCE = 'm06_gunner_syd'
    GAME_ACTOR = 'GunnerSyd'



class M06OrderDeckScene(Scene):
    DUMP_FILE = 'm06_order_deck'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Объекты: параметры камеры, света, персонажей и реквизита правятся здесь.
        music_main = Sound(root=self, name='music_main', sound='music_discordant_psychosis', attenuation=0, dmin=50,
            dmax=300, priority='Story_Sound_1')
        preserve_entity(music_main, userprops={'category': 'Audio', 'Priority': 'Story_Sound_1'})
        PlayerShip = PropPlayership(root=self, name='PlayerShip', light_group=3, init_point='PlayerShip',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(PlayerShip, userprops={'category': 'Spaceship'})
        prisoners_ship02 = PropPrisonersShip02(root=self, name='prisoners_ship02', light_group=3,
            init_point='prisoners_ship02', rotate_from_quat=True, use_ambient=False)
        preserve_entity(prisoners_ship02, userprops={'category': 'Spaceship', 'loadout': 'level_li_elite_loadout04'})
        prisoners_ship03 = PropPrisonersShip03(root=self, name='prisoners_ship03', light_group=3,
            init_point='prisoners_ship03', rotate_from_quat=True, use_ambient=False)
        preserve_entity(prisoners_ship03, userprops={'category': 'Spaceship', 'loadout': 'level_li_elite_loadout04'})
        test_vehicle = PropTestVehicle(root=self, name='test_vehicle', light_group=3, init_point='test_vehicle',
            rotate_from_quat=True, use_ambient=False)
        preserve_entity(test_vehicle, userprops={'category': 'Spaceship', 'loadout': 'level_li_elite_loadout04'})
        trent = Character(root=self, actor=actors.Trent, light_group=3, init_point='Char_trent', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(trent, template_name='trent', userprops={'actor': 'Player', 'category': 'Character'})
        prisoner1 = Character(root=self, actor=ExtraCharPrisoner1, light_group=3, init_point='Char_prisoner1',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner1, template_name='m06_asf_prisoner01',
            userprops={'actor': 'Prisoner1', 'category': 'Character'})
        prisoner2 = Character(root=self, actor=ExtraCharPrisoner2, light_group=3, init_point='Char_prisoner2',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner2, template_name='m06_asf_prisoner02',
            userprops={'actor': 'Prisoner2', 'category': 'Character'})
        prisoner3 = Character(root=self, actor=ExtraCharPrisoner3, light_group=3, init_point='Char_prisoner3',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner3, template_name='m06_asf_prisoner03',
            userprops={'actor': 'Prisoner3', 'category': 'Character'})
        prisoner4 = Character(root=self, actor=ExtraCharPrisoner4, light_group=3, init_point='Char_prisoner4',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(prisoner4, template_name='m06_asf_prisoner04',
            userprops={'actor': 'Prisoner4', 'category': 'Character'})
        commander = Character(root=self, actor=ExtraCharCommander, light_group=3, init_point='Char_commander',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(commander, template_name='m06_gunner_leader',
            userprops={'actor': 'Gunner_commander', 'category': 'Character'})
        gunner01 = Character(root=self, actor=ExtraCharGunner01, light_group=3, init_point='Char_gunner01',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(gunner01, template_name='m06_gunner_sides1', userprops={'actor': 'Gunner2', 'category': 'Character'})
        gunner02 = Character(root=self, actor=ExtraCharGunner02, light_group=3, init_point='Char_gunner02',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(gunner02, template_name='m06_gunner_sides2', userprops={'actor': 'Gunner3', 'category': 'Character'})
        gunner03 = Character(root=self, actor=ExtraCharGunner03, light_group=3, init_point='Char_gunner03',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(gunner03, template_name='m06_gunner_back1', userprops={'actor': 'Gunner4', 'category': 'Character'})
        gunner04 = Character(root=self, actor=ExtraCharGunner04, light_group=3, init_point='Char_gunner04',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(gunner04, template_name='m06_gunner_back2', userprops={'actor': 'Gunner5', 'category': 'Character'})
        syd = Character(root=self, actor=actors.Ceed, light_group=3, init_point='Char_syd', rotate_from_quat=True,
            use_ambient=False, floor_height=0)
        preserve_entity(syd, template_name='syd', userprops={'actor': 'Syd', 'category': 'Character'})
        syd_guard = Character(root=self, actor=ExtraCharSydGuard, light_group=3, init_point='Char_syd_guard',
            rotate_from_quat=True, use_ambient=False, floor_height=0)
        preserve_entity(syd_guard, template_name='m06_gunner_syd', userprops={'actor': 'GunnerSyd', 'category': 'Character'})
        cam_entry = StaticCamera(root=self, name='cam_entry', fov=25, farplane=5000)
        preserve_entity(cam_entry)
        Path_cam_entry = MotionPath(root=self, name='Path_cam_entry', point_name='Path_cam_entry',
            path_data='{-15, 11, -25}, {0.5,0,-0.5,0},   {-10, 5, -10}, {0.8,0,-0.2,0},   {0, 4, 5}, {0.6,0,0.4,0},  {10, 1, 6}, {0.3,0,0.7,0}')
        preserve_entity(Path_cam_entry)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=20, farplane=5000, look_duration=150)
        preserve_entity(cam_trent)
        cam_syd = LookAtCamera(root=self, name='cam_syd', fov=18, farplane=5000, look_duration=150)
        preserve_entity(cam_syd)

        # Вход / начальная постановка.
        t = 0
        trent.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=50, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner1',
            anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner2',
            anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner3',
            anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_prisoner4',
            anim=Male.Sc_MLBODY_STND_IDLE_000LV_xa_04, duration=10)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_gunner01',
            anim=Male.Sc_MLBODY_STND_AIM_GUN_FRWD_000LV_XA_02, duration=2, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_gunner02',
            anim=Male.Sc_SPCBODY_s019b_Drake_XA_STND_000LV_13, duration=2, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_gunner03',
            anim=Male.Sc_SPCBODY_s019b_Drake_XA_STND_000LV_13, duration=2, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_gunner04',
            anim=Male.Sc_MLBODY_STND_AIM_GUN_FRWD_000LV_XA_02, duration=2, loop=True)
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_HOLD_000LV_XA_01, duration=1, loop=True)
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_syd_guard',
            anim=Male.Sc_MLBODY_STND_HOLD_RIFLE_MILI_000LV_XA_05, duration=555, loop=True)
        cam_entry.set(group=MAIN, time_delay=t)
        SourcePathEvent(root=self, group=MAIN, time_delay=t, targets=['cam_entry', 'Path_cam_entry'], duration=25,
            start_percent=0, stop_percent=1, offset=[0, 0, 0], up='Y_AXIS', front='NEG_Z_AXIS',
            flags='POSITION+ORIENTATION', param_curve={'CLSID': 'FreeFormPCurve', 'points': [[0, 0, 0, 0], [1, 1, 0, 0]]},
            pcurve_period=-1000)
        music_main.start(group=MAIN, time_delay=t, duration=47, loop=True)
        t += 22.9
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_commander',
            target_name='automarker_point_commander_start', duration=0.001, smooth=False)
        t += 0.1
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_commander', anim=Male.Sc_MLBODY_WLKG_000LV_XA_01,
            duration=7, loop=True)
        t += 5
        cam_trent.set(group=MAIN, time_delay=t)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_trent',
            target_name='automarker_trent_lookpoint_commander', duration=25, transition_duration=2, target_type='ROOT',
            target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1
        trent.motion(group=MAIN, time_delay=t, anim=Trent.Sc_MLHEAD_CONCNTRTE_TRENT_000LV_XA_, duration=5, trans_time=0.25)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='Char_commander',
            target_name='automarker_point_commander_around_syd', duration=0.001, smooth=False)
        NeckIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_syd', target_name='automarker_syd_head_ik',
            duration=55, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        EyeIkEvent(root=self, group=MAIN, time_delay=t, char_name='Char_syd', target_name='automarker_syd_eye_ik',
            duration=55, transition_duration=1, target_type='ROOT', target_part='', up='NEG_Y_AXIS', front='Z_AXIS')
        t += 1
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_commander',
            anim=Male.Sc_MLBODY_WALK_STND_TRNS_000LV_XA_02, duration=15)
        cam_syd.set(group=MAIN, time_delay=t)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='cam_syd', target_name='automarker_cam_syd_pos2',
            duration=10, smooth=True)
        music_main.change_attenuation(group=MAIN, time_delay=t, duration=5, attenuation=-15)
        main_group.append_time(35)


        # Реплика 10 · orderpilot · исходное время 35 с
        # Капитан Сид, мы обнаружили артефакты на борту этого фриленсера.
        # Исходное окно facial: 0 с.
        t = 0
        voice_sound = self.lookup_single_sound(10)
        SoundEvent(root=self, group=MAIN, sound_name=voice_sound.get_nickname())
        t = 0
        MotionEvent(root=self, group=MAIN, time_delay=t, object_name='Char_commander',
            anim=Male.Sc_MLBODY_STND_SALUT_000LV_XA_03, duration=5, time_scale=0.8, trans_time=1)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_lookpoint_syd_at_commander', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_lookpoint_syd_at_commander', duration=1.5, smooth=True)
        main_group.append_time(4)


        # Реплика 20 · syd · исходное время 39 с
        # Отлично. Спасибо за работу, ребята. Артефакты – на склад, пленных – в кают-компанию.
        # Исходное окно facial: 19 с.
        t = 0
        t += 0.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_lookpoint_syd_forward', duration=2, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_lookpoint_syd_forward', duration=1.5, smooth=True)
        t += 3.5
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_lookpoint_syd_at_commander', duration=1.5, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_lookpoint_syd_at_commander', duration=1.1, smooth=True)
        t += 3
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_head_ik',
            target_name='automarker_lookpoint_syd_forward', duration=3, smooth=True)
        MoveEvent(root=self, group=MAIN, time_delay=t, object_name='automarker_syd_eye_ik',
            target_name='automarker_lookpoint_syd_forward', duration=2, smooth=True)
        t += 0.5
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLBODY_STND_ATEASE_RLEASE_000LV_XA_01, duration=15,
            time_scale=0.5, trans_time=1)
        t += 0.5
        syd.motion(group=MAIN, time_delay=t, anim=Male.Sc_MLHEAD_BASEPOSE_000LV_02_01, duration=15, time_scale=0.7,
            trans_time=0.5)
        syd.facial(group=MAIN, index=20, append=True, auto_lip=True, extra_delay=0)
        # Перекрытие исходных facial-окон; менять отдельно от паузы после реплики.
        main_group.append_time(-8.0)


# Совместимость с уже подключёнными THORN_CLASS.
ReconstructedScene = M06OrderDeckScene
