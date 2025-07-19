import json
import pathlib

from story.cutscenes.content import Point, Marker
from tools.data_folder import DataFolder
from text.dividers import STRING_DIVIDER


DUMPS_PATH = pathlib.Path().resolve().parent / 'SCENES' / 'DUMPS'
ROOT_TEMPLATE = 'cutscenes/misc/scene_root.lua'


class Scene:
    SCENE_AMBIENT = [0, 0, 0]
    MIN_DURATION = 30

    def __init__(self, tpl_manager, props):
        self.tpl_manager = tpl_manager
        self.props = props
        self.entities = {}
        self.events = {}
        self.points = {}

        self.load_points_dump()

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
                    name=f'automarker_{key}',
                    point=point
                )
            )

    def add_entity(self, entity):
        if entity.name in self.entities:
            raise Exception(f'Entity {entity.name} already defined')
        self.entities[entity.name] = entity

    def get_entites_content(self):
        return STRING_DIVIDER.join([e.get_thorn() for e in self.entities.values()])

    def get_events_content(self):
        return STRING_DIVIDER.join([e.get_thorn() for e in self.events.values()])

    def get_root_params(self):
        return {
            'scene_name': self.get_scene_name(),
            'scene_duration': self.get_duration(),
            'scene_ambient': self.get_scene_ambient(),
            'entities': self.get_entites_content(),
            'events': self.get_events_content(),
        }

    def get_content(self):
        data = self.tpl_manager.get_result(ROOT_TEMPLATE, self.get_root_params())
        DataFolder.sync_scene(self.get_scene_name(), data)

