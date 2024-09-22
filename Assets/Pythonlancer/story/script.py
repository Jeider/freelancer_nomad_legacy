class MissionSegment(object):
    ALIAS = ''
    VOICE_LINES = []

    COMMENT_TEMPLATE = '<p class="comment_before_line">{comment}</p>'
    LINE_TEMPLATE = '<p class="line_name">{name}</p><p class="line_value"><span class="line_content">{value}</span></p>'

    def __init__(self, mission):
        self.mission = mission

    @classmethod
    def get_name_for_line(cls, line):
        raise NotImplementedError

    @classmethod
    def get_lines_for_script(cls):
        lines = []
        for line in cls.VOICE_LINES:
            content = []
            if line.comment != '':
                content.append(
                    cls.COMMENT_TEMPLATE.format(comment=line.comment)
                )
            content.append(
                cls.LINE_TEMPLATE.format(
                    name=cls.get_name_for_line(line),
                    value=line.get_ru_story_text()
                )
            )
            lines.append(''.join(content))
        return lines

    @classmethod
    def get_lines_names(cls):
        return [cls.get_name_for_line(line) for line in cls.VOICE_LINES]


class CutsceneProps(MissionSegment):
    ALIAS = 'scene'
    VOICE_LINES = []
    MISSION_INDEX = None

    LINE_NAME_TEMPLATE = 'm{mission_index:02d}_{scene_alias}_{voiceline_index:04d}_{actor_name}'

    @classmethod
    def get_name_for_line(cls, line):
        return cls.LINE_NAME_TEMPLATE.format(
            mission_index=cls.MISSION_INDEX,
            scene_alias=cls.ALIAS,
            voiceline_index=line.index,
            actor_name=line.actor.NAME,
        )



class SpaceVoiceProps(MissionSegment):
    VOICE_LINES = []

    LINE_NAME_TEMPLATE = 'dx_m{mission_index:02d}_{voiceline_index:04d}_{actor_name}'

    @classmethod
    def get_name_for_line(cls, line):
        return cls.LINE_NAME_TEMPLATE.format(
            mission_index=cls.MISSION_INDEX,
            voiceline_index=line.index,
            actor_name=line.actor.NAME,
        )



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
.comment_before_line {
    font-weight: bold;
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

    CUTSCENE_CONTAINER_TEMPLATE = '''
        <h3>{title}</h3>
        <p>{description}</p>
        {lines}
    '''

    SPACE_CONTAINER_TEMPLATE = '''
        <h3>Космос</h3>
        {lines}    
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

    def get_space_lines(self):
        return

    def get_story_script_content(self):
        content = []
        for cutscene in self.cutscenes:
            scene_content = self.CUTSCENE_CONTAINER_TEMPLATE.format(
                title=cutscene.TITLE,
                description=cutscene.DESCRIPTION,
                lines=''.join(cutscene.get_lines_for_script()),
            )
            content.append(scene_content)
        space_content = self.SPACE_CONTAINER_TEMPLATE.format(
            lines=''.join(self.SPACE_CLASS.get_lines_for_script()),
        )
        content.append(space_content)
        return content
