class Event(object):
    PARENT = None

    def process(self):
        raise Exception('Event %s cannot be processed' % self.__class__.__name__)


class SetCam(Event):
    def __init__(self, cam_name):
        self.cam_name = cam_name


class AnimateCam(Event):
    def __init__(self, cam_name, new_index=2):
        self.cam_name = cam_name
        self.new_index = new_index


class StartIK(Event):

    def __init__(self, character):
        self.character = character
