from text.dividers import SINGLE_DIVIDER

JOB_SCOUT = 'scout'
JOB_ASSAULT = 'assault'
JOB_DEFEND = 'defend'

JOBS = [JOB_SCOUT, JOB_ASSAULT, JOB_DEFEND]


class Encounter:
    NICKNAME = None
    FILENAME = None

    DEFINITION_TEMPLATE = '''[EncounterParameters]
nickname = {nickname}
filename = {filename}'''

    def get_filename(self):
        if self.FILENAME is None:
            raise Exception(f'Encounter {self} have no filename!')
        return self.FILENAME

    def get_definition(self):
        return self.DEFINITION_TEMPLATE.format(nickname=self.get_nickname(), filename=self.get_filename())

    def get_nickname(self):
        if self.NICKNAME is None:
            raise Exception(f'Encounter {self} have no nickname!')
        return self.NICKNAME


class NpcShipEncounter:
    def __init__(self, name, npc, count):
        self.name = name
        self.npc = npc
        self.count = count

    def get_name(self):
        return self.name

    def get_count(self):
        return self.count


class DynamicEncounter(Encounter):

    def __init__(self, system, nickname, ship_encounters: list[NpcShipEncounter], job: str):
        self.system = system
        self.nickname = nickname
        self.ship_encounters = ship_encounters
        self.job = job

        if self.job not in JOBS:
            raise Exception(f'Encounter {self} have unknown job {self.job}')

    def get_nickname(self):
        return self.nickname

    def get_filename(self):
        return f'missions\\NPC\\GENERATED\\{self.nickname}.ini'

    def get_file_content(self):
        ships_data = []

        i = 0
        for ship_enc in self.ship_encounters:
            self.system.add_custom_encounter_ship_name(ship_enc.get_name())
            if i == 0:
                ships_data.append(
                    f'''
ship_by_npc_arch = {ship_enc.get_count()}, {ship_enc.get_count()}, {ship_enc.npc.get_npc_shiparch_nickname()}
pilot_job = {self.job}_leader_job
make_class = wanderer
'''
                )
            else:
                ships_data.append(
                    f'''
ship_by_npc_arch = {ship_enc.get_count()}, {ship_enc.get_count()}, {ship_enc.npc.get_npc_shiparch_nickname()}, -1
pilot_job = {self.job}_job
make_class = wanderer
'''
                )

            i += 1

        content = f'''
[EncounterFormation]
{SINGLE_DIVIDER.join(ships_data)}

formation_by_class = fighters
behavior = wander
arrival = all, -tradelane, -object_jump_gate
allow_simultaneous_creation = yes
zone_creation_distance = 0
times_to_create = infinite

[Creation]
permutation = 0, 5
        '''

        return content


class MainDefend(Encounter):
    NICKNAME = 'main_defend'
    FILENAME = 'missions\\NPC\\GENERIC\\main_defend.ini'


class MainPatrol(Encounter):
    NICKNAME = 'main_patrol'
    FILENAME = 'missions\\NPC\\GENERIC\\main_patrol.ini'


class MainScout(Encounter):
    NICKNAME = 'main_scout'
    FILENAME = 'missions\\NPC\\GENERIC\\main_scout.ini'


class MainTrade(Encounter):
    NICKNAME = 'main_trade'
    FILENAME = 'missions\\NPC\\GENERIC\\main_trade.ini'


class MainTradeTLR(Encounter):
    NICKNAME = 'main_trade_tlr'
    FILENAME = 'missions\\NPC\\GENERIC\\main_trade_tlr.ini'


class PatrolPolice(Encounter):
    NICKNAME = 'patrol_police'
    FILENAME = 'missions\\NPC\\patrol_police.ini'


class PatrolTLR(Encounter):
    NICKNAME = 'patrol_tlr'
    FILENAME = 'missions\\NPC\\patrol_tlr.ini'


class PatrolTLREliteOnly(Encounter):
    NICKNAME = 'patrol_tlr_elite'
    FILENAME = 'missions\\NPC\\patrol_tlr_elite.ini'


class AresXScout(Encounter):
    NICKNAME = 'area_xscout'
    FILENAME = 'missions\\NPC\\area_rebels.ini'


class BhTrade(Encounter):
    NICKNAME = 'bh_trade'
    FILENAME = 'missions\\npc\\generic\\bh_trade.ini'


class BhTradeTLR(Encounter):
    NICKNAME = 'bh_trade_tlr'
    FILENAME = 'missions\\npc\\generic\\bh_trade_tlr.ini'


class BhPatrol(Encounter):
    NICKNAME = 'bh_patrol'
    FILENAME = 'missions\\npc\\generic\\bh_patrol.ini'


class RhCruiser(Encounter):
    NICKNAME = 'rh_grp_main_cruiser'
    FILENAME = 'missions\\npc\\rh\\rh_grp_main_cruiser.ini'


class RhGunboat(Encounter):
    NICKNAME = 'rh_grp_main_gunboat'
    FILENAME = 'missions\\npc\\rh\\rh_grp_main_gunboat.ini'


class LiCruiser(Encounter):
    NICKNAME = 'li_grp_main_cruiser'
    FILENAME = 'missions\\npc\\li\\li_grp_main_cruiser.ini'


class BrDestroyer(Encounter):
    NICKNAME = 'br_grp_main_cruiser'
    FILENAME = 'missions\\npc\\br\\br_grp_main_destroyer.ini'


class BrGunboat(Encounter):
    NICKNAME = 'br_grp_main_gunboat'
    FILENAME = 'missions\\npc\\br\\br_grp_main_gunboat.ini'


class KuDestroyer(Encounter):
    NICKNAME = 'ku_grp_main_cruiser'
    FILENAME = 'missions\\npc\\ku\\ku_grp_main_destroyer.ini'


class KuGunboat(Encounter):
    NICKNAME = 'ku_grp_main_gunboat'
    FILENAME = 'missions\\npc\\ku\\ku_grp_main_gunboat.ini'


class RhTransport(Encounter):
    NICKNAME = 'tr_grp_rh_transport'
    FILENAME = 'missions\\npc\\rh\\tr_grp_rh_transport.ini'


class RhTransportTLR(Encounter):
    NICKNAME = 'tr_grp_rh_transport_tlr'
    FILENAME = 'missions\\npc\\rh\\tr_grp_rh_transport_tlr.ini'


class LiTransport(Encounter):
    NICKNAME = 'tr_grp_li_transport'
    FILENAME = 'missions\\npc\\li\\tr_grp_li_transport.ini'


class LiTransportTLR(Encounter):
    NICKNAME = 'tr_grp_li_transport_tlr'
    FILENAME = 'missions\\npc\\li\\tr_grp_li_transport_tlr.ini'


class BrTransport(Encounter):
    NICKNAME = 'tr_grp_br_transport'
    FILENAME = 'missions\\npc\\br\\tr_grp_br_transport.ini'


class BrTransportTLR(Encounter):
    NICKNAME = 'tr_grp_br_transport_tlr'
    FILENAME = 'missions\\npc\\br\\tr_grp_br_transport_tlr.ini'


class KuTransport(Encounter):
    NICKNAME = 'tr_grp_ku_transport'
    FILENAME = 'missions\\npc\\ku\\tr_grp_ku_transport.ini'


class KuTransportTLR(Encounter):
    NICKNAME = 'tr_grp_ku_transport_tlr'
    FILENAME = 'missions\\npc\\ku\\tr_grp_ku_transport_tlr.ini'


class Lifter(Encounter):
    NICKNAME = 'corp_lifter'
    FILENAME = 'missions\\npc\\lifter.ini'
