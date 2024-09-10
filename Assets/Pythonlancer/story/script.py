class MissionSegment(object):
    ALIAS = ''
    VOICE_LINES = []

    LINE_TEMPLATE = '<p class="line_name">{name}</p><p class="line_value"><span class="line_content">{value}</span></p>'

    def __init__(self, mission):
        self.mission = mission

    def get_name_for_line(self, line):
        raise NotImplementedError

    def get_lines_for_script(self):
        return [
            self.LINE_TEMPLATE.format(
                name=self.get_name_for_line(line),
                value=line.get_ru_story_text()
            ) for line in self.VOICE_LINES
        ]


class CutsceneProps(MissionSegment):
    ALIAS = 'scene'

    LINE_NAME_TEMPLATE = 'm{mission_index:02d}_{scene_alias}_{voiceline_index:04d}_{actor_name}'

    def get_name_for_line(self, line):
        return self.LINE_NAME_TEMPLATE.format(
            mission_index=self.mission.MISSION_INDEX,
            scene_alias=self.ALIAS,
            voiceline_index=line.index,
            actor_name=line.actor.NAME,
        )

    def get_voice_lines(self):
        return {}



class SpaceVoiceProps(MissionSegment):
    ALIAS = 'dx'
    VOICE_LINES = []



class StoryMission(object):
    SPACE_VOICE_LINES = []
    SPACE_CLASS = None
    CUTSCENES = []
    MISSION_TITLE = None

    STYLES = '''
.line_name {
    margin-bottom: 0;
}
.line_value {
    margin-top: 5px;
}
.comment {
    background-color: white;
}
.line_content {
    background-color: yellow;
}
'''
    SCRIPT_TEMPLATE = '''
<html>
<head>
<meta charset="utf-8">
<title>{mission_title}</title>
<style>
{styles}
</style>
</head>
<body>
<h2>{mission_title}</h2>
{content}
</body>
</html>
    '''

    def __init__(self):
        self.cutscenes = [cutscene(self) for cutscene in self.CUTSCENES]
        self.space = self.SPACE_CLASS(self)

    def get_story_script(self):
        return self.SCRIPT_TEMPLATE.format(
            mission_title=self.MISSION_TITLE,
            styles=self.STYLES,
            content='<hr>'.join(self.get_story_script_content())
        )

    def get_story_script_content(self):
        content = []
        for cutscene in self.cutscenes:
            content.append(''.join(cutscene.get_lines_for_script()))
        return content

