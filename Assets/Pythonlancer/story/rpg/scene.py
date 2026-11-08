"""One spoken fragment using mission 14+ Autoplay and generic facial timing.

The conversation session owns actor binding, placement and both cameras.
No room, costume, light, ship, or Blender scene is loaded here.
"""
import copy
import json

from audio.sound import CutsceneSound
from story.cutscenes.scene import Scene
from story.cutscenes.content import MAIN, BG, BG_GROUP, Character, Autoplay, SetCameraEvent, SoundEvent, MotionEvent
from story.cutscenes import sequence

CAMERAS = {'vendor': 'RpgCamera_vendor', 'player': 'RpgCamera_player'}
GESTURE_SEQUENCE = 'SEQUENCE_MALE_STAND_RHAND_ALT2'
GESTURE_COUNT = 8


class FragmentSound(CutsceneSound):
    def get_duration(self, russian=True):
        return self.seconds

    def get_nickname(self):
        return self.nickname


class BoundCharacter(Character):
    def __init__(self, root, actor, binding, anim_sequence=None):
        self.root, self.actor = root, actor
        self.name = f'Char_{actor.NAME}'
        self.binding = binding
        self.camera = self
        self.sequence_step = 0
        self.facial_indexes = 1
        # Autoplay consumes override_duration; never mutate the shared library.
        self.anim_sequence = copy.deepcopy(anim_sequence) if anim_sequence else [[]]
        self.sequence_len = len(self.anim_sequence)
        root.add_entity(self)

    def set(self, group):
        SetCameraEvent(root=self.root, group=group, camera_name=self.root.camera_name)

    def get_thorn(self):
        return ('{entity_name=' + json.dumps(self.name) + ',type=DEFORMABLE,'
                'template_name="",flags=LIT_DYNAMIC,lt_grp=0,srt_grp=0,'
                'userprops={Actor=' + json.dumps(self.binding) + ',category="Character"}}')


class FragmentScene(Scene):
    def __init__(self, templates, script, fragment, sound, language, seconds, nickname, anim_sequence=None):
        self.tpl_manager = templates
        self.russian = language == 'ru'
        self.start_time = 0
        self.entities, self.events, self.groups = {}, [], {}
        self.add_group(BG, group_type=BG_GROUP)
        self.add_group(MAIN)
        self.camera_name = CAMERAS[fragment['role']]
        self.sound = FragmentSound(sound.line, sound.name, script)
        self.sound.seconds, self.sound.nickname = seconds, nickname
        binding = script.data['binding'][fragment['role']]
        BoundCharacter(self, sound.line.actor, binding, anim_sequence)
        self.get_group(MAIN).append_time(.15)
        Autoplay(self, group=MAIN)
        for _, event in self.events:
            if isinstance(event, SoundEvent):
                event.duration = seconds
        # Keep the existing auto facial tail; Character.facial is inherited unchanged.
        self.get_group(MAIN).append_time(1)
        self.duration = self.get_group(MAIN).get_time()

    def lookup_multiple_sounds(self, start, end):
        return [self.sound]

    def lookup_single_sound(self, index):
        return self.sound

    def get_content(self):
        # Reference cameras are supplied once by the conversation session.
        # No origin camera fallback or per-fragment player placement.
        camera = ('{entity_name=' + json.dumps(self.camera_name) + ',type=CAMERA,'
                  'template_name="",flags=REFERENCE,'
                  'cameraprops={fovh=30,hvaspect=1.333333,nearplane=.1,farplane=10000}}')
        entities = ['{entity_name="Monitor_1",type=MONITOR,template_name=""}', camera]
        entities += [entity.get_thorn() for entity in self.entities.values()]
        entities.append(self.sound.get_thorn())
        events = [event.get_thorn(time) for time, event in sorted(self.events, key=lambda item: item[0])]
        return ('-- RPG fragment: requires bound actors and session cameras; see manifest.json\n'
                f'duration={self.duration:.6f}\nentities={{\n' + ',\n'.join(entities) +
                '\n}\nevents={\n' + ',\n'.join(events) + '\n}\n')


class GestureScene(FragmentScene):
    """One complete authored sequence step, owned by the conversation, not a voice."""
    def __init__(self, templates, script, fragment, sound, language, seconds, nickname, step):
        # Seated commandants keep the chair pose throughout their gesture track.
        if fragment['role'] == 'vendor' and script.data.get('vendor_posture') == 'sit':
            seated = ['Sc_MLBODY_CHRB_SHRG_SHLDRS_SMALL_000LV_XA_03',
                      'Sc_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07',
                      'Sc_MLBODY_CHRB_IDLE_MED_000LV_XA_07',
                      'Sc_MLBODY_CHRB_IDLE_000LV_XA_05']
            authored = [[{'anim': seated[i % len(seated)], 'time_scale': .6, 'trans_time': .8}]
                        for i in range(GESTURE_COUNT)]
        else:
            authored = getattr(sequence, GESTURE_SEQUENCE)
        if len(authored) != GESTURE_COUNT:
            raise ValueError('Gesture sequence length changed; update the client sequence contract')
        super().__init__(templates, script, fragment, sound, language, seconds, nickname,
                         anim_sequence=[authored[step]])
        # Autoplay generates the complete step. Only its body track lives separately;
        # facial, sound and camera events remain in the spoken fragment.
        self.events = [(time, event) for time, event in self.events if isinstance(event, MotionEvent)]
        self.duration = max(time + event.duration for time, event in self.events)

    def get_content(self):
        entities = ',\n'.join(entity.get_thorn() for entity in self.entities.values())
        events = ',\n'.join(event.get_thorn(time) for time, event in sorted(self.events, key=lambda item: item[0]))
        return f'-- Complete authored gesture step; independent of speech fragments.\nduration={self.duration:.6f}\nentities={{\n{entities}\n}}\nevents={{\n{events}\n}}\n'
