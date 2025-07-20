import json
import pathlib

from story.cutscenes.meta import MetaManager
from story.cutscenes.content import Point, Marker, Event, Group, MAIN, BG
from tools.data_folder import DataFolder
from text.dividers import STRING_DIVIDER


DUMPS_PATH = pathlib.Path().resolve().parent / 'SCENES' / 'DUMPS'
ROOT_TEMPLATE = 'cutscenes/misc/scene_root.lua'


def automarker_name(name):
    return f'automarker_{name}'


class Scene:
    SCENE_AMBIENT = [0, 0, 0]
    MIN_DURATION = 30

    def __init__(self, tpl_manager, props):
        self.tpl_manager = tpl_manager
        self.meta_manager = MetaManager(tpl_manager=self.tpl_manager)
        self.props = props
        self.entities = {}
        self.events = []
        self.points = {}
        self.groups = {}
        self.add_group(BG)
        self.add_group(MAIN)

        self.load_points_dump()
        self.action()
        # self.load_base_entities()

    def add_group(self, name, time=0):
        self.groups[name] = Group(self, time=time)

    def clone_group(self, name, original):
        from_group = self.groups[original]
        self.groups[name] = Group(self, time=from_group.get_time())

    def lookup_single_sound(self, index):
        for sound in self.props.get_sounds():
            if sound.line.index == index:
                return sound

        raise Exception(f'Scene {self}. Dialog with index {index} not found')

    def lookup_sound_meta(self, sound):
        return self.meta_manager.get_line_meta(sound)

    def action(self):
        raise NotImplementedError

    def get_group(self, group_name):
        return self.groups[group_name]

    def get_duration(self):
        main_time = self.get_group(MAIN).get_time()
        if main_time > self.MIN_DURATION:
            return main_time
        return self.MIN_DURATION

    def get_scene_name(self):
        return self.props.get_scene_name()

    def get_scene_ambient(self):
        return self.SCENE_AMBIENT

    def load_points_dump(self):
        points_file = DUMPS_PATH / f'{self.get_scene_name()}.json'
        if not points_file.exists():
            raise Exception(f'Scene {self} have no dump file')

        try:
            with open(points_file) as points_data:
                data = json.load(points_data)

        except json.JSONDecodeError as e:
            raise Exception(f'Could not previous cutscene metadata. Reason: {e}')

        for key, value in data.items():
            point = Point(
                name=key,
                position=value['position'],
                orientation=value['orientation'],
                rotate=value['rotate']
            )
            self.points[key] = point

            Marker(
                root=self,
                name=automarker_name(key),
                point_name=key
            )

    def get_automarker(self, point_name):
        if point_name not in self.points:
            raise Exception(f'Unknown point {point_name}')

        return self.entities[automarker_name(point_name)]

    def get_point(self, point_name):
        return self.points[point_name]

    def get_base_entities(self):
        raise Exception(f'Scene {self} have no base entities')

    def load_base_entities(self):
        for entity in self.get_base_entities():
            self.add_entity(entity)

    def add_entity(self, entity):
        if entity.name in self.entities:
            raise Exception(f'Entity {entity.name} already defined')
        self.entities[entity.name] = entity

    def add_event(self, time, event):
        self.events.append(
            (time, event),
        )

    def get_entities_content(self):
        return STRING_DIVIDER.join([e.get_thorn() for e in self.entities.values()])

    def get_events_content(self):
        return STRING_DIVIDER.join([e.get_thorn(time) for time, e in self.events])

    def get_script_sounds(self):
        return STRING_DIVIDER.join([s.get_thorn() for s in self.props.get_sounds()])

    def get_root_params(self):
        return {
            'scene_name': self.get_scene_name(),
            'scene_duration': self.get_duration(),
            'scene_ambient': self.get_scene_ambient(),
            'entities': self.get_entities_content(),
            'events': self.get_events_content(),
            'script_sounds': self.get_script_sounds(),
        }

    def get_content(self):
        data = self.tpl_manager.get_result(ROOT_TEMPLATE, self.get_root_params())
        DataFolder.sync_scene(self.get_scene_name(), data)
