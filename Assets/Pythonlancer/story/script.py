from text.dividers import SINGLE_DIVIDER

from audio.sound import SpaceSound, CutsceneSound
from audio.voice import MaleVoice, FemaleVoice, TrentVoice


class MissionSegment(object):
    ALIAS = ''
    VOICE_LINES = []
    MISSION_INDEX = None

    COMMENT_TEMPLATE = '<p class="comment_before_line">{comment}</p>'
    LINE_TEMPLATE = ('<p class="line_name actor_{actor_name}">{name}</p>'
                     '<p class="line_value actor_{actor_name}""><span class="line_content">{value}</span></p>')

    def __init__(self, mission):
        self.mission = mission

    def get_sounds(self):
        named_lines = []
        for line in self.get_lines():
            named_lines.append(
                self.get_sound_item(line)
            )
        return named_lines

    def get_sound_item(self, line):
        raise NotImplementedError

    @classmethod
    def get_name_for_line(cls, line):
        raise NotImplementedError

    @classmethod
    def get_lines(cls):
        return cls.VOICE_LINES

    @classmethod
    def get_line_by_index(cls, index):
        """not efficient, for debug"""
        for item in cls.VOICE_LINES:
            if index == item.index:
                return item
        raise Exception('index %d not found' % index)

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
                    actor_name=line.actor.NAME,
                    name=cls.get_name_for_line(line),
                    value=line.get_ru_story_text(),
                )
            )
            lines.append(''.join(content))
        return lines

    @classmethod
    def get_actors(cls):
        return set([line.actor for line in cls.VOICE_LINES])

    @classmethod
    def get_lines_names(cls):
        return [cls.get_name_for_line(line) for line in cls.VOICE_LINES]


class CutsceneProps(MissionSegment):
    ALIAS = 'scene'
    VOICE_LINES = []

    LINE_NAME_TEMPLATE = 'm{mission_index:02d}_{scene_alias}_{voiceline_index:04d}_{actor_name}'

    @classmethod
    def get_name_for_line(cls, line):
        return cls.LINE_NAME_TEMPLATE.format(
            mission_index=cls.MISSION_INDEX,
            scene_alias=cls.ALIAS,
            voiceline_index=line.index,
            actor_name=line.actor.NAME,
        )

    def get_destination(self):
        return f'audio\\mod\\m{self.MISSION_INDEX:02d}'

    def get_sound_item(self, line):
        return CutsceneSound(
            name=self.get_name_for_line(line),
            line=line,
            destination=self.get_destination()
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

    def get_sound_item(self, line):
        return SpaceSound(
            name=self.get_name_for_line(line),
            line=line,
            attenuation=line.actor.get_attenuation(),
        )


class StoryMission(object):
    SPACE_VOICE_LINES = []
    SPACE_CLASS = None
    CUTSCENES = []
    MISSION_TITLE = None
    MISSION_INDEX = None
    SYNC_SPACE = False

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
    background-color: #FFFF8F;
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
<h1>{mission_title}</h1>
<p><a href="{root_link}"><- Вернуться в корень сценария</a></p>
<hr>
<h2>Актёры</h2>
{actors}
<h2>Текст</h2>
{script_content}
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

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __init__(self):
        self.cutscenes = [cutscene(self) for cutscene in self.CUTSCENES]
        self.space = self.SPACE_CLASS(self)
        self.actors = self.get_story_actors()

    def get_story_script(self, actor=None):
        styles = self.STYLES
        if actor:
            styles += f'''
            .actor_{actor.NAME} .line_content {{
                background-color: #50C878;
            }}
             
            '''
        return self.SCRIPT_TEMPLATE.format(
            mission_title=self.MISSION_TITLE,
            styles=styles,
            root_link=ScriptIndex.get_index_filename(),
            actors=self.get_actors_content(),
            script_content=f'{SINGLE_DIVIDER}<hr>'.join(self.get_story_script_content())
        )

    def get_story_actors(self):
        actors = set()
        for cutscene in self.cutscenes:
            actors |= cutscene.get_actors()
        actors |= self.SPACE_CLASS.get_actors()

        return sorted(list(actors), key=lambda x: x.RU_NAME)

    def get_actors_content(self):
        content = []
        for actor in self.actors:
            content.append(f'<p><a href="{self.get_actor_file_link(actor)}">{actor.RU_NAME}</a></p>')
        return SINGLE_DIVIDER.join(content)

    def get_space_lines(self):
        return self.SPACE_CLASS.get_lines()

    def get_space_line_by_id(self, id):
        return self.SPACE_CLASS.get_line_by_id(id)

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

    def get_root_file_link(self):
        return f'mission{self.MISSION_INDEX}.html'

    def get_actor_file_link(self, actor):
        return f'mission{self.MISSION_INDEX}_{actor.NAME}.html'

    def get_short_name(self):
        return f'Миссия {self.MISSION_INDEX}'

    def get_alias(self):
        return f'mission{self.MISSION_INDEX}'

    def get_male_voice_root(self):
        return f'echo_m{self.MISSION_INDEX:02d}'

    def get_female_voice_root(self):
        return f'echo_m{self.MISSION_INDEX:02d}_female'

    def get_player_voice_root(self):
        return f'echo_m{self.MISSION_INDEX:02d}_player'

    def get_voice_root_for_sound(self, sound):
        if sound.line.actor.is_male():
            return self.get_male_voice_root()
        if sound.line.actor.is_female():
            return self.get_female_voice_root()
        if sound.line.actor.is_player():
            return self.get_player_voice_root()
        raise Exception('unknown voice root exception')

    def get_male_space_voice(self):
        return MaleVoice(
            voice_name=self.get_male_voice_root(),
            sounds=[sound for sound in self.space.get_sounds() if sound.line.actor.is_male()],
        )

    def get_female_space_voice(self):
        return FemaleVoice(
            voice_name=self.get_female_voice_root(),
            sounds=[sound for sound in self.space.get_sounds() if sound.line.actor.is_female()],
        )

    def get_trent_space_voice(self):
        return TrentVoice(
            voice_name=self.get_player_voice_root(),
            sounds=[sound for sound in self.space.get_sounds() if sound.line.actor.is_player()],
        )

    def get_voices(self):
        return [
            self.get_male_space_voice(),
            self.get_female_space_voice(),
            self.get_trent_space_voice(),
        ]

    def get_cutscene_sounds(self):
        sounds = []
        for segment in self.cutscenes:
            sounds.extend(segment.get_sounds())
        return sounds


class ScriptIndex(object):
    STORY_TEMPLATE = '''
<html>
<head>
<meta charset="utf-8">
<title>Сценарий Наследия Номадов</title>
</head>
<body>
<h2>Сценарий Наследия Номадов</h2>
{content}
</body>
</html>
    '''

    INDEX_FILENAME = 'index.html'

    @classmethod
    def get_index_filename(cls):
        return cls.INDEX_FILENAME

    @classmethod
    def get_index_content(cls, missions):
        links = []
        for mission in missions:
            links.append(f'<p><a href="{mission.get_root_file_link()}">{mission.get_short_name()}</a></p>')
        content = SINGLE_DIVIDER.join(links)
        return cls.STORY_TEMPLATE.format(content=content)

