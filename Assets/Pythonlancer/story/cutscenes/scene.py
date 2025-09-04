import json
import pathlib

from story.cutscenes.meta import LipSyncManager
from story.cutscenes.content import (Point, Marker, Event, Group, MAIN, BG, FloorHeightEvent,
                                     SOURCE_BLENDER, SOURCE_PYTHONLANCER, DEFAULT_GROUP, BG_GROUP)
from tools.data_folder import DataFolder
from text.dividers import STRING_DIVIDER


DUMPS_PATH = pathlib.Path().resolve().parent / 'SCENES' / 'DUMPS'
ROOT_TEMPLATE = 'cutscenes/misc/scene_root.lua'


def automarker_name(name):
    return f'automarker_{name}'


class Scene:
    SCENE_AMBIENT = [0, 0, 0]
    MIN_DURATION = 1
    POINT_ROTATE_OVERRIDES = {}
    DEFAULT_POINT_NAME = 'default_point'
    OFFSCREEN_POINT_NAME = 'offscreen_point'

    def __init__(self, tpl_manager, props, extra_name=''):
        self.tpl_manager = tpl_manager
        self.meta_manager = LipSyncManager(tpl_manager=self.tpl_manager)
        self.extra_name = extra_name
        self.props = props
        self.entities = {}
        self.events = []
        self.points = {}
        self.groups = {}
        self.add_group(BG, group_type=BG_GROUP)
        self.add_group(MAIN)
        self.start_time = 0
        self.duration = None

        self.load_default_point()
        self.load_points_dump()
        self.action()
        # self.load_base_entities()

    def set_start_time(self, start_time):
        self.start_time = start_time

    def add_group(self, name, time=0, group_type=DEFAULT_GROUP):
        self.groups[name] = Group(self, time=time, name=name, group_type=group_type)

    def clone_group(self, name, original):
        from_group = self.groups[original]
        new_group = Group(self, time=from_group.get_time(), name=name, group_type=from_group.get_type())
        if name in self.groups:
            raise Exception(f'Group {name} is already used')
        self.groups[name] = new_group
        return new_group

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
        if self.duration is not None:
            return self.duration
        main_time = self.get_group(MAIN).get_time()
        if main_time > self.MIN_DURATION:
            return main_time
        return self.MIN_DURATION

    def set_duration(self, duration):
        self.duration = duration

    def get_scene_base_name(self):
        return self.props.get_scene_name()

    def get_scene_name(self):
        extended_name = (
            f'_{self.extra_name}'
            if self.extra_name != ''
            else ''
        )
        return f'{self.props.get_scene_name()}{extended_name}'

    def get_scene_ambient(self):
        return self.SCENE_AMBIENT

    def load_default_point(self):
        self.add_point(name=self.DEFAULT_POINT_NAME, position=[0, 0, 0], source=SOURCE_PYTHONLANCER)

        Marker(
            root=self,
            name=automarker_name(self.DEFAULT_POINT_NAME),
            point_name=self.DEFAULT_POINT_NAME
        )

        self.add_point(name=self.OFFSCREEN_POINT_NAME, position=[0, -10000, 0], source=SOURCE_PYTHONLANCER)

        Marker(
            root=self,
            name=automarker_name(self.OFFSCREEN_POINT_NAME),
            point_name=self.OFFSCREEN_POINT_NAME
        )

    def load_points_dump(self):
        points_file = DUMPS_PATH / f'{self.get_scene_base_name()}.json'
        if not points_file.exists():
            raise Exception(f'Scene {self} have no dump file')

        try:
            with open(points_file) as points_data:
                data = json.load(points_data)

        except json.JSONDecodeError as e:
            raise Exception(f'Could not previous cutscene metadata. Reason: {e}')

        for key, value in data.items():
            self.add_point(
                name=key,
                position=value['position'],
                orientation=value['orientation'],
                source=SOURCE_BLENDER
            )

            Marker(
                root=self,
                name=automarker_name(key),
                point_name=key
            )

    def get_automarker(self, point_name):
        if point_name not in self.points:
            raise Exception(f'Unknown point {point_name}')

        return self.entities[automarker_name(point_name)]

    def get_automarker_name(self, point_name):
        return self.get_automarker(point_name).name

    def get_entity(self, entity_name):
        return self.entities[entity_name]

    def add_point(self, name, position, source, rotate=None, orientation=None):
        point = Point(
            name=name,
            position=position,
            orientation=orientation,
            rotate=rotate if rotate else self.POINT_ROTATE_OVERRIDES.get(name),
            source=source,
        )
        if name in self.points:
            raise Exception(f'Point {name} is already defined')
        self.points[name] = point

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
        thorn = []

        for time, e in self.events:
            event_time = time
            if e.group.is_default():
                event_time -= self.start_time
                skip_event = True
                if event_time < 0:
                    if e.__class__ == FloorHeightEvent:
                        e.make_immediately()
                        event_time = 0
                        skip_event = False

                    if skip_event:
                        continue

            thorn.append(e.get_thorn(event_time))

        return STRING_DIVIDER.join(thorn)

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
        return self.tpl_manager.get_result(ROOT_TEMPLATE, self.get_root_params())

    def sync_content(self):
        DataFolder.sync_scene(self.get_scene_name(), self.get_content())
