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

