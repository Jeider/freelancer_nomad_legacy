class Encounter(object):
    NICKNAME = ''
    FILENAME = ''

    DEFINITION_TEMPLATE = '''[EncounterParameters]
nickname = {nickname}
filename = {filename}'''

    @classmethod
    def get_definition(self):
        return self.DEFINITION_TEMPLATE.format(nickname=self.NICKNAME, filename=self.FILENAME)

    @classmethod
    def get_nickname(self):
        return self.NICKNAME


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
