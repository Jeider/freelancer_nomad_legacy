import json
import pathlib

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
        self.props = props
        self.entities = {}
        self.events = []
        self.points = {}
        self.groups = {
            BG: Group(self),
            MAIN: Group(self),
        }

        self.load_points_dump()
        self.load_base_entities()

    def get_group(self, group_name):
        return self.groups[group_name]

    def get_duration(self):
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
                orientation=value['orientation']
            )
            self.points[key] = point

            self.add_entity(
                Marker(
                    self,
                    name=automarker_name(key),
                    point_name=key
                )
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

    def get_root_params(self):
        return {
            'scene_name': self.get_scene_name(),
            'scene_duration': self.get_duration(),
            'scene_ambient': self.get_scene_ambient(),
            'entities': self.get_entities_content(),
            'events': self.get_events_content(),
        }

    def get_content(self):
        data = self.tpl_manager.get_result(ROOT_TEMPLATE, self.get_root_params())
        DataFolder.sync_scene(self.get_scene_name(), data)
