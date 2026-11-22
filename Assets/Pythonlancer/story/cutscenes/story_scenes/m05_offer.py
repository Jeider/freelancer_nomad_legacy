"""m05_offer: полная постановка из master; точки в m05_offer.blend."""
from story.cutscenes.scene import Scene
from story.cutscenes.content import (
    Character, ConnectHardpointEvent, EyeIkEvent, Female, Light, LookAtCamera, MAIN, Male, MoveEvent, NeckIkEvent, Prop,
)
from story.cutscenes.anim import (
    Female, Male,
)
from story import actors


class HatcherBottleProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'bottle_wine_3'

class HatcherGlassProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass'

class TrentGlassProp(Prop):
    COMPOUND_TEMPLATE_NAME = 'glass'


class M05OfferScene(Scene):
    DUMP_FILE = 'm05_offer'
    SCENE_AMBIENT = [128, 128, 128]

    def action(self):
        main_group = self.get_group(MAIN)

        # Персонажи, камеры, реквизит и звук.
        ambi_ltg00_tbl_rtable4_01 = Light(root=self, name='ambi_LtG00_Tbl_rTable4/01',
            point_name='ambi_LtG00_Tbl_rTable4/01', extra_name='', light_group=5, hidden=False,
            rotate_from_quat=True, diffuse=[1, 1, 1], ambient=[0.141176, 0.141176, 0.141176], direction=[0, 0, 1],
            light_type='L_POINT', range=451, cutoff=180, theta=180, color=[214, 187, 133],
            attenuation=[0.0099999998, 0, 5.1500000954], on=True)
        ambi_ltg00_bar_ovrhd01a = Light(root=self, name='ambi_LtG00_Bar_Ovrhd01A',
            point_name='ambi_LtG00_Bar_Ovrhd01A', extra_name='', light_group=5, hidden=False,
            rotate_from_quat=True, diffuse=[0.596078, 0.572549, 0.403922], ambient=[0.223529, 0.2, 0.192157],
            direction=[0, 0, 1], light_type='L_POINT', range=15, cutoff=18, theta=15, color=[233, 208, 150],
            attenuation=[0.8999999762, 0, 0.0060000001], on=True)
        hatcher_bottle = HatcherBottleProp(root=self, name='hatcher_bottle', light_group=0,
            init_point='hatcher_bottle', rotate_from_quat=True)
        hatcher_glass = HatcherGlassProp(root=self, name='hatcher_glass', light_group=0,
            init_point='hatcher_glass', rotate_from_quat=True)
        trent_glass = TrentGlassProp(root=self, name='trent_glass', light_group=0, init_point='trent_glass',
            rotate_from_quat=True)
        hatcher = Character(root=self, actor=actors.Hatcher, name='Char_hatcher', light_group=5,
            init_point='Char_hatcher', rotate_from_quat=True, appearance='hatcher', actor_name='Hatcher')
        trent = Character(root=self, actor=actors.Trent, name='Char_trent', light_group=0,
            init_point='Char_trent', rotate_from_quat=True, appearance='trent', actor_name='Player')
        cam_start = LookAtCamera(root=self, name='cam_start', fov=25, look_duration=300)
        cam_hatcher = LookAtCamera(root=self, name='cam_hatcher', fov=22, look_duration=300)
        cam_trent = LookAtCamera(root=self, name='cam_trent', fov=25, look_duration=300)
        cam_hatcher_top = LookAtCamera(root=self, name='cam_hatcher_top', fov=20, look_duration=300)
        cam_trent_top = LookAtCamera(root=self, name='cam_trent_top', fov=22, look_duration=300)
        cam_hatcher_table = LookAtCamera(root=self, name='cam_hatcher_table', fov=25, look_duration=300)
        cam_table = LookAtCamera(root=self, name='cam_table', fov=22, look_duration=300)
        cam_hatcher_reward = LookAtCamera(root=self, name='cam_hatcher_reward', fov=20, look_duration=300)

        # Исходные точки взгляда.

        # Вход.
        t = 0
        cam_start.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_WLKG_000LV_XA_01, duration=8, time_scale=0.7, loop=True,
            time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=15, loop=True,
            time_delay=t)
        cam_start.move_cam(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        cam_start.move_focus(group=MAIN, index=2, duration=7, smooth=True, time_delay=t)
        t += 3
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=5, transition_duration=1, time_delay=t)
        t += 2
        NeckIkEvent(root=self, group=MAIN, char_name=hatcher.name,
            target_name=self.get_automarker_name('hatcher_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=200, transition_duration=1, time_delay=t)
        t += 2
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('hatcher_head_ik'),
            target_name=self.get_automarker_name('head_trent_sit'), duration=2, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        cam_hatcher.set(group=MAIN, time_delay=t)
        main_group.append_time(7.5)

        # m05_offer 10: Hatcher.
        # Как вы мистер Трент? Все в порядке?
        t = 0.6
        MoveEvent(root=self, group=MAIN, object_name=trent.name,
            target_name=self.get_automarker_name('point_trent_sit'), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 0.1
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=1, time_delay=t)
        t += 1.8
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=29, transition_duration=1, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_TALK_000LV_A_16, duration=10, time_delay=t)
        t += 0.25
        cam_trent_top.set(group=MAIN, time_delay=t)
        hatcher.facial(group=MAIN, index=10, auto_lip=True, extra_delay=0)

        # m05_offer 20: Trent.
        # Все отлично мисс Хетчер. Только вот, знаете, вчера ногу натер, а сегодня утром из душа выходил - так
        # в пояснице кольнуло.
        t = 7
        ConnectHardpointEvent(root=self, group=MAIN, target_name=hatcher_bottle.name, parent_name=hatcher.name,
            duration=7, target_hardpoint='HpRightConnect_prop_bottle_wine_1', parent_hardpoint='HpRightConnect',
            time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=hatcher_glass.name, parent_name=hatcher.name,
            duration=7, target_hardpoint='hpleftconnect_prop_glass_green', parent_hardpoint='hpleftconnect',
            time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_HOLDD_LEFT_000LV_00, duration=0.2, time_scale=10,
            trans_time=0.25, time_delay=t)
        cam_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_GRABR_PRDRNK_TABL_000LV_XA_09, duration=8,
            time_scale=0.3, start_time=0.9, time_delay=t)
        trent.facial(group=MAIN, index=20, auto_lip=True, extra_delay=0)

        # m05_offer 30: Hatcher.
        # Мистер Трент, давайте не будем превращать традиционный обмен любезностями в цирк.
        hatcher.facial(group=MAIN, index=30, auto_lip=True, extra_delay=0)

        # m05_offer 40: Trent.
        # Так может обойдемся без обмена любезностями и перейдем сразу к делу?
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=6, time_delay=t)
        t += 2.5
        MoveEvent(root=self, group=MAIN, object_name=hatcher_bottle.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=hatcher_glass.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=40, auto_lip=True, extra_delay=0)

        # m05_offer 50: Hatcher.
        # А с вами будет непросто...
        t = 0
        cam_hatcher_top.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=6, time_delay=t)
        hatcher.facial(group=MAIN, index=50, auto_lip=True, extra_delay=0)

        # m05_offer 60: Hatcher.
        # Мы проанализировали привезенные вами документы, они безусловно представляют огромную ценность для
        # нас, но есть одна проблема.
        t = 0.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_PUSH_DRINK_TABL_000LV_XA_05, duration=9,
            time_scale=0.7, trans_time=0.5, time_delay=t)
        t += 7.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=5, time_delay=t)
        cam_trent.set(group=MAIN, time_delay=t)
        hatcher.facial(group=MAIN, index=60, auto_lip=True, extra_delay=0)

        # m05_offer 70: Trent.
        # Всегда есть проблема
        t = 0
        ConnectHardpointEvent(root=self, group=MAIN, target_name=trent_glass.name, parent_name=trent.name,
            duration=10, target_hardpoint='hpleftconnect_prop_glass_green', parent_hardpoint='hpleftconnect',
            time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, duration=0.2, time_scale=10,
            trans_time=0.25, time_delay=t)
        t += 1.5
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_DRINK_LHND_SIP_000LV_XA_04, duration=7, trans_time=1,
            time_delay=t)
        t += 1
        trent.motion(group=MAIN, anim=Male.Sc_MLHEAD_NEUT_BLINK_EYES_000LV_A_00, duration=2, time_scale=0.2,
            trans_time=0.25, time_delay=t)
        t += 1.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=0.8, time_delay=t)
        trent.facial(group=MAIN, index=70, auto_lip=True, extra_delay=0)

        # m05_offer 80: Hatcher.
        # Слишком много научных выкладок, причем настолько передовых, что у нас головастики драку устроили, не
        # сойдясь в трактовках данных.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        t += 0.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CONV_LHNDUP_TRNS_000LV_XA_01, duration=2,
            time_scale=0.5, trans_time=1, time_delay=t)
        t += 1
        hatcher.motion(group=MAIN, anim=Female.Sc_FMHAND_HNEUT_GESTL_CASL_000LV_00, duration=10, time_scale=0.7,
            trans_time=0.25, time_delay=t)
        t += 0.8
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CONV_LHND_CASL_000LV_xa_03, duration=3,
            time_scale=0.5, trans_time=1, loop=True, time_delay=t)
        t += 0.2
        NeckIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_head_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=500, transition_duration=1, time_delay=t)
        t += 2.8
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CONV_LHNDDN_TRNS_000LV_XA_01, duration=3,
            time_scale=0.5, trans_time=1.5, time_delay=t)
        t += 0.2
        MoveEvent(root=self, group=MAIN, object_name=trent_glass.name,
            target_name=self.get_automarker_name(self.OFFSCREEN_POINT_NAME), duration=0.001, smooth=False,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        t += 1.8
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=5, time_scale=0.7,
            trans_time=1, time_delay=t)
        hatcher.facial(group=MAIN, index=80, auto_lip=True, extra_delay=0)

        # m05_offer 90: Hatcher.
        # Знаете, мистер Трент, драка между учеными выглядит со стороны весьма забавно.
        t = 3
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_IDLE_000LV_XA_05, duration=0.1, time_delay=t)
        t += 1.5
        cam_trent_top.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_PUTDNL_DRINK_TABL_000LV_XA_06, duration=15,
            time_scale=0.7, time_delay=t)
        ConnectHardpointEvent(root=self, group=MAIN, target_name=trent_glass.name, parent_name=trent.name,
            duration=3, target_hardpoint='hpleftconnect_prop_glass_green', parent_hardpoint='hpleftconnect',
            time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_HNEUT_HOLDD_LEFT_000LV_00, duration=0.2, time_scale=10,
            trans_time=0.25, time_delay=t)
        hatcher.facial(group=MAIN, index=90, auto_lip=True, extra_delay=0)

        # m05_offer 100: Trent.
        # Жаль не видел. В чем моя роль? Не ученых же ваших разнимать?
        t = 2.7
        trent.motion(group=MAIN, anim=Male.Sc_MLHAND_NEUT_LEFT_000LV_A_00, duration=6, time_scale=0.01,
            trans_time=0.25, time_delay=t)
        trent.facial(group=MAIN, index=100, auto_lip=True, extra_delay=0)

        # m05_offer 110: Hatcher.
        # Нам нужно мнение не просто ученого, а гения, светилы в своей области, человека который мог бы дать
        # однозначную трактовку этим данным.
        t = 0
        cam_hatcher_table.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CONV_LHNDUP_TRNS_000LV_XA_02, duration=2.6,
            time_scale=0.6, time_delay=t)
        t += 2.6
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CONV_LHNDDN_TRNS_000LV_XA_02, duration=3,
            time_scale=0.6, trans_time=1, time_delay=t)
        t += 3
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_IDLE_000LV_XA_05, duration=3, time_scale=0.6,
            trans_time=1, time_delay=t)
        hatcher.facial(group=MAIN, index=110, auto_lip=True, extra_delay=0)

        # m05_offer 120: Hatcher.
        # Я знаю такого человека, я с ним лично знакома. Это профессор Мандрейк. Он сможет во всем
        # разобраться.
        t = 0.5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_CHRB_TRNS_000LV_XA_02, duration=5, time_scale=0.6,
            trans_time=1, time_delay=t)
        t += 6
        cam_trent.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_LSTN_000UP_A_18, duration=6, time_scale=0.7,
            time_delay=t)
        hatcher.facial(group=MAIN, index=120, auto_lip=True, extra_delay=0)

        # m05_offer 130: Trent.
        # Но вы не можете просто позвонить ему и попросить вам помочь потому что...
        trent.facial(group=MAIN, index=130, auto_lip=True, extra_delay=0)

        # m05_offer 140: Hatcher.
        # Потому что он работает в ДипСпейсИнжиниринг и в данный момент отправился в исследовательскую
        # экспедицию, судя по всему очень важную, потому что их служба противодействия промышленному шпионажу
        # буквально на ушах стоит.
        t = 0
        cam_hatcher_top.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRF_TALK_EMPH_000UP_A_10, duration=15, time_scale=0.6,
            time_delay=t)
        hatcher.facial(group=MAIN, index=140, auto_lip=True, extra_delay=0)
        # Действие после исходного окна реплики.
        t = 0.5
        cam_trent_top.set(group=MAIN, time_delay=t)
        trent.motion(group=MAIN, anim=Male.Sc_MLBODY_CHRB_LSTN_000UP_A_18, duration=55, time_scale=0.7, loop=True,
            time_delay=t)
        main_group.append_time(1)

        # m05_offer 150: Trent.
        # И мое задание будет состоять в...
        trent.facial(group=MAIN, index=150, auto_lip=True, extra_delay=0)

        # m05_offer 160: Hatcher.
        # В полете... Мистер Трент, перестаньте. Вам нужно будет вылететь на станцию Детройт - в штаб квартиру
        # ДипСпейс, узнать там местонахождение профессора Мандрейка, забрать его и привезти ко мне.
        t = 0
        cam_hatcher.set(group=MAIN, time_delay=t)
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_TALK_000LV_A_08, duration=10, time_scale=0.6,
            trans_time=1, time_delay=t)
        t += 10
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_TALK_000UP_A_14, duration=15, time_scale=0.6,
            trans_time=1, time_delay=t)
        hatcher.facial(group=MAIN, index=160, auto_lip=True, extra_delay=0)

        # m05_offer 170: Hatcher.
        # Я дам вам свою визитку на случай проблем со службой безопасности ДипСпейс, скажете что действуете от
        # моего имени.
        t = 0
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_PUSH_DRINK_TABL_000LV_XA_05, duration=15,
            start_time=1, trans_time=1, time_delay=t)
        t += 5
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_IDLE_000LV_XA_06, duration=10, trans_time=1,
            time_delay=t)
        EyeIkEvent(root=self, group=MAIN, char_name=trent.name,
            target_name=self.get_automarker_name('trent_eye_ik'), target_type='ROOT', target_part='',
            up='NEG_Y_AXIS', front='Z_AXIS', duration=25, transition_duration=1, time_delay=t)
        t += 1
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('marker_card'), duration=3, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('marker_card'), duration=1.5, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        hatcher.facial(group=MAIN, index=170, auto_lip=True, extra_delay=0)

        # m05_offer 180: Trent.
        # Служба безопасности Альянса? Никогда не слышал о такой.
        t = 0
        cam_trent.set(group=MAIN, time_delay=t)
        t += 3
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_head_ik'),
            target_name=self.get_automarker_name('head_hatcher'), duration=1, smooth=True, adjust_pos=True,
            adjust_orient=True, time_delay=t)
        MoveEvent(root=self, group=MAIN, object_name=self.get_automarker_name('trent_eye_ik'),
            target_name=self.get_automarker_name('head_hatcher_lower'), duration=0.5, smooth=True,
            adjust_pos=True, adjust_orient=True, time_delay=t)
        trent.facial(group=MAIN, index=180, auto_lip=True, extra_delay=0)

        # m05_offer 190: Hatcher.
        # Это не имеет значения, мистер Трент. Гонорар за выполнение задания будет очень приятным.
        t = 0
        hatcher.motion(group=MAIN, anim=Female.Sc_FMBODY_CHRB_CHRF_TRNS_000LV_XA_02, duration=5, time_scale=0.7,
            trans_time=1, time_delay=t)
        cam_hatcher_reward.set(group=MAIN, time_delay=t)
        hatcher.facial(group=MAIN, index=190, auto_lip=True, extra_delay=0)
