import json
import pathlib

from tools.data_folder import DataFolder
from story.actors import ACTOR_TRENT, ACTOR_MALE, ACTOR_FEMALE

CAMERA_PER_TYPE = {
    ACTOR_TRENT: 'cam_dbg_trent',
    ACTOR_MALE: 'cam_dbg_trent',
    ACTOR_FEMALE: 'cam_hatcher',
}

DEFAULT_ANIM_PER_TYPE = {
    ACTOR_TRENT: 'Sc_dx_s045b_1801_trent',
    ACTOR_MALE: 'Sc_dx_s068x_0201_walker',
    ACTOR_FEMALE: 'Sc_dx_s070x_0801_Jacobi',
}

STAND_ANIM_PER_TYPE = {
    ACTOR_TRENT: 'Sc_MLBODY_STND_IDLE_000LV_xa_04',
    ACTOR_MALE: 'Sc_MLBODY_STND_IDLE_000LV_xa_04',
    ACTOR_FEMALE: 'Sc_FMBODY_STND_IDLE_000LV_xa_05',
}


class ExitInteractionException(Exception):
    pass


class MetaDatabase:

    @staticmethod
    def get_database_file_location():
        current_path = pathlib.Path().resolve()
        return current_path / 'story' / 'cutscenes' / 'db' / 'audio_meta.json'

    def __init__(self):
        db_file_loc = self.get_database_file_location()
        if not db_file_loc.exists():
            raise Exception('cutscene meta database file is not exist')

        try:
            with open(db_file_loc) as db_file:
                self.db = json.load(db_file)

        except json.JSONDecodeError as e:
            raise Exception(f'Could not previous cutscene metadata. Reason: {e}')

    def save_db(self):
        with open(self.get_database_file_location(), 'w') as db_file:
            json.dump(self.db, db_file)

    def set_meta(self, line, meta):
        self.db[line] = meta
        self.save_db()

    def record_exist(self, line):
        return self.db.get(line, None) is not None

    def get_record(self, line):
        return self.db[line]


class Lip:
    def __init__(self, props='', delay=0, delay_factor=0):
        self.delay_factor: float = delay_factor
        self.delay: float = delay
        self.props = props

    def set_delay(self, delay):
        self.delay = delay

    def set_props(self, props):
        self.props = props

    def get_meta(self):
        return {
            'delay': self.delay + self.delay_factor,
            'props': self.props,
        }

    def get_delay(self):
        return self.delay

    def get_props(self):
        return self.props


class LipsParser:
    '''
    EXTRACTS STRING
{
    -- LIP
    0,
    START_MOTION,
    {"Char_the"},
    {animation="Sc_dx_s045b_1801_trent", duration=10, time_scale=1, trans_time=0.25,  weight=1, heading=-1}
},
    '''

    LIP_IDENTIFIER = '-- LIP'

    def __init__(self, delay_factor=0):
        self.delay_factor = delay_factor
        self.data = DataFolder.get_facial()

    def get_lips(self):
        lips = []

        lip_index = 1
        for line in self.data:
            clean_line = line.strip()
            if clean_line == self.LIP_IDENTIFIER:
                lips.append(Lip())
                lip_index = 1

            if len(lips) == 0:
                continue  # no current lip, skip

            elif lip_index == 2:
                lips[-1].set_delay(float(clean_line[:-1]))

            elif lip_index == 3 and clean_line[:-1] != 'START_MOTION':
                raise Exception(f'Invalid action: {clean_line[:-1]}')

            elif lip_index == 5:
                lips[-1].set_props(clean_line)  # props have no ending comma

            lip_index += 1

        return lips


class LipSyncManager:
    FACIAL_TEMPLATE = 'cutscenes/demo/facial.lua'

    def __init__(self, tpl_manager):
        self.meta_db = MetaDatabase()
        self.tpl_manager = tpl_manager

    def prepare_facial_workspace(self, sound, new=True):
        actor_type = sound.line.actor.TYPE
        context = {
            'sound': sound,
            'anim': DEFAULT_ANIM_PER_TYPE[actor_type],
            'camera': CAMERA_PER_TYPE[actor_type],
            'stand_anim': STAND_ANIM_PER_TYPE[actor_type],
            'new': new,
            'exist_meta': [] if new else self.get_line_meta(sound)
        }
        data = self.tpl_manager.get_result(self.FACIAL_TEMPLATE, context)
        DataFolder.sync_facial(data)

    def get_lips_from_workspace(self):
        return LipsParser().get_lips()

    def save_line_meta(self, sound, lips):
        self.meta_db.set_meta(
            sound.get_nickname(),
            [x.get_meta() for x in lips]
        )

    def get_line_meta(self, sound):
        record = self.meta_db.get_record(sound.get_nickname())
        results = []
        for item in record:
            results.append(
                Lip(
                    delay=item['delay'],
                    props=item['props']
                )
            )
        return results

    def sound_meta_is_exist(self, sound):
        return self.meta_db.record_exist(sound.get_nickname())

    def edit_sound_interactive(self, sound, new=True):
        self.prepare_facial_workspace(sound, new)

        nickname = sound.get_nickname()

        action = input(f'Edit {nickname}. Enter A to apply')

        if action.lower() != 'a':
            raise ExitInteractionException('Skip. Unknown error')

        lips = self.get_lips_from_workspace()
        self.save_line_meta(sound, lips)

    def edit_cutscene_interactive(self, cutscene, skip_exist=True):
        for sound in cutscene.get_sounds():
            if skip_exist and self.sound_meta_is_exist(sound):
                continue

            try:
                self.edit_sound_interactive(sound)
            except ExitInteractionException:
                raise Exception('Operation aborted')

    def edit_mission_interactive(self, script_mission):
        raise NotImplementedError

    def get_single_sound_from_scene(self, scene, index):
        for sound in scene.get_sounds():
            if sound.line.index == index:
                return sound
        raise Exception(f'index {index} not found in scene {scene}')

    def test_edit(self, script_mission):
        scenes = script_mission.get_cutscenes()
        scene = scenes[0]

        # self.edit_cutscene_interactive(scene)

        sound = self.get_single_sound_from_scene(scene, 100)
        self.edit_sound_interactive(sound, new=False)



        # sound = scenes[0].get_sounds()[0]
        #
        # self.edit_sound_interactive(sound)

        #
        # self.prepare_facial_workspace(sound)
        # lips = self.get_lips_from_workspace()
        # self.save_line_meta(sound, lips)

        print('1')


