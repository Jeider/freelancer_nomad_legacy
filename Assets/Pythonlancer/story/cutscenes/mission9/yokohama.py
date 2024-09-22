from story.scripts.mission9 import Msn9YokohamaCutscene as Msn9YokohamaCutsceneProps
from story.thorn import cutscene
from story.thorn import entity as et
from story.thorn import event as ev

from text.dividers import DIVIDER

class Yo(object):
    pass


class Trent():
    pass





DBG1 = 'nextpoint'

#
# class Debug(cutscene.Section):
#
#     def get_actions(self):
#         return [
#             ev.SetCam('dbg', i=1),
#             ev.StartIK(Trent, after=1),
#
#             ev.Index(after=1, i=2),
#             ev.LookHead(Trent, p=DBG1, d=2, after=2),
#             ev.LookEye(Trent, p=DBG1, d=1, after=2),
#
#             ev.Talk(Trent, voice=10, after=2, i=3),
#
#             ev.SetCam('altercam', after=3, i=4),
#             ev.AnimateCam('altercam', n=2, d=10),
#         ]



class CutsceneThorn(object):
    OFFSCREEN = 'offscreen'
    SCENE_NAME = 'm08_yokohama'
    SCENE_AMBIENT = [0, 0, 0]
    OFFSCREEN_POS = -1000000, -10000, 0
    SCENARIO_CLASS = Msn9YokohamaCutsceneProps

    MONITOR_TEMPLATE = '''
    {
        entity_name="Monitor_1",
        type=MONITOR,
        template_name="",
        template_id=0
    },	
    '''

    OFFSCREEN_TEMPLATE = ''' 
    {
        entity_name="offscreen",
        type=MARKER,
        template_name="",
        lt_grp=0,
        srt_grp=0,
        usr_flg=0,
        flags=HIDDEN,
        spatialprops={pos={-10000000,-10000,0},orient={{1,0,0},{0,1,0},{0,0,1}}},
    },
    '''

    def get_scene_root(self):
        return '''
    {
        entity_name="scene_'''+self.SCENE_NAME+'''",
        type=SCENE,
        template_name="", lt_grp=0, srt_grp=0, usr_flg=0,
        spatialprops={ pos={0,0,0}, orient={{1,0,0},{0,1,0},{0,0,1}}},
        up=Y_AXIS,front=Z_AXIS,
        ambient={'''+str(self.OFFSCREEN_POS[0])+','+str(self.OFFSCREEN_POS[1])+','+str(self.OFFSCREEN_POS[2])+'''}
    },
    '''

    def get_root_entities(self):
        return [
            self.get_scene_root(),
            self.MONITOR_TEMPLATE,
            self.OFFSCREEN_TEMPLATE,
        ]

    def get_dialog_entity(self, dialog_name):
        return '''
    {
        entity_name="'''+dialog_name+'''",
        template_name="'''+dialog_name+'''",
        type=SOUND,lt_grp=0, srt_grp=0, usr_flg=0,
        spatialprops={pos={0,0,0},orient={{1,0,0},{0,1,0},{0,0,1}}},
        audioprops={attenuation=0,pan=0,dmin=50,dmax=1000,ain=360,aout=360,atout=0,rmix=0},
        userprops={category="Audio"}
    },
    '''

    def get_dialogs_entities(self):
        return [self.get_dialog_entity(dialog_name) for dialog_name in self.SCENARIO_CLASS.get_lines_names()]

    def get_entities(self):
        return DIVIDER.join(self.get_root_entities() + self.get_dialogs_entities())

    def get_content(self):
        entities = self.get_entities()
        events = ''
        content = '''
entities = {
    '''+entities+'''
}
events = {
    '''+events+'''
}
'''
        return content



class Msn9YokohamaCutsceneThorn(CutsceneThorn):


    TEMPLATE_FILE = 'm9_yokohama'









