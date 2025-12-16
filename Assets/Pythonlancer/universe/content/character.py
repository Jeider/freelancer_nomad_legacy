import random

from universe.content.interior import BAR, DECK
from world.bodyparts import Costume

from text.dividers import SINGLE_DIVIDER


MALE_VOICE_RU = 'rvp101b'
FEMALE_VOICE_RU = 'rvp501b'

MALE_VOICE_EN = 'rvp101'
FEMALE_VOICE_EN = 'rvp501'

BRIBE_IDS = [16100, 16101]
BRIBE_PRICE = 10000


class Char:
    def __init__(self, core, nickname, faction, costume: Costume, room=BAR):
        self.core = core
        self.nickname = nickname
        self.faction = faction
        self.costume = costume
        if self.core.russian:
            self.voice = MALE_VOICE_RU if costume.is_male else FEMALE_VOICE_RU
        else:
            self.voice = MALE_VOICE_EN if costume.is_male else FEMALE_VOICE_EN
        self.room = room
        self.messages = []

    def get_name(self):
        return self.nickname

    def add_message(self, message):
        self.messages.append(message)

    def get_messages_definition(self):
        return [msg.get_definition() for msg in self.messages]

    def get_mbase(self):
        items = [
            '[GF_NPC]',
            f'nickname = {self.nickname}',
            f'body = {self.costume.get_body()}',
            f'head = {self.costume.get_head()}',
            f'lefthand = {self.costume.get_left_hand()}',
            f'righthand = {self.costume.get_right_hand()}',
            # 'individual_name = 220001',
            f'affiliation = {self.faction.get_code()}',
            f'voice = {self.voice}',
            f'room = {self.room}',
        ]
        if accessory := self.costume.get_accessory():
            items.append(f'accessory = {accessory}')

        if self.faction.is_give_bribes():
            for bribe_code in self.core.factions.get_by_code(self.faction.get_code()).get_bribe_factions():
                items.append(f'bribe = {bribe_code}, {BRIBE_PRICE}, {random.choice(BRIBE_IDS)}')

        items.extend(self.get_messages_definition())
        return SINGLE_DIVIDER.join(items)


# [GF_NPC]
# nickname = bar_rh_bartender
# body = rh_bartender_body
# head = rh_bartender_head
# lefthand = benchmark_male_hand_left
# righthand = benchmark_male_hand_right
# affiliation = rh_grp
# voice = rvp101

# [GF_NPC]
# nickname = bar_rh_robo_bartender
# base_appr = Robot_body_d
# affiliation = rh_grp
# voice = rvp003

# [GF_NPC]
# nickname = bar_li_bartender
# body = li_bartender_body
# head = rh_bartender_head
# lefthand = benchmark_male_hand_left
# righthand = benchmark_male_hand_right
# affiliation = li_grp
# voice = rvp101

# [GF_NPC]
# nickname = bar_li_robo_bartender
# base_appr = Robot_body_d
# affiliation = lx_grp
# voice = rvp003


