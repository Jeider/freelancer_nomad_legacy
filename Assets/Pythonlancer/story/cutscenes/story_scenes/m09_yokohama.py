from story.cutscenes.scene import Scene
from story.cutscenes.content import StaticCamera, LookAtCamera


class Msn9YokohamaCutsceneThorn(Scene):

    def get_base_entities(self):
        return [
            # StaticCamera(self, 'cam_fix', fov=40),
            LookAtCamera(self, 'cam_dbg', fov=40)
        ]
