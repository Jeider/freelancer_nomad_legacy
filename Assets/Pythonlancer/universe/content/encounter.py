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


class BhTradeRh(Encounter):
    NICKNAME = 'bh_grp_rh_trade'
    FILENAME = 'missions\\npc\\rh\\bh_grp_rh_trade.ini'


class BhTradeRhTLR(Encounter):
    NICKNAME = 'bh_grp_rh_trade_tlr'
    FILENAME = 'missions\\npc\\rh\\bh_grp_rh_trade_tlr.ini'


class BhPatrolRh(Encounter):
    NICKNAME = 'bh_grp_rh_patrol'
    FILENAME = 'missions\\npc\\rh\\bh_grp_rh_patrol.ini'


class BhTradeLi(Encounter):
    NICKNAME = 'bh_grp_li_trade'
    FILENAME = 'missions\\npc\\li\\bh_grp_li_trade.ini'


class BhTradeLiTLR(Encounter):
    NICKNAME = 'bh_grp_li_trade_tlr'
    FILENAME = 'missions\\npc\\li\\bh_grp_li_trade_tlr.ini'

class BhPatrolLi(Encounter):
    NICKNAME = 'bh_grp_li_patrol'
    FILENAME = 'missions\\npc\\li\\bh_grp_li_patrol.ini'


class BhTradeBr(Encounter):
    NICKNAME = 'bh_grp_br_trade'
    FILENAME = 'missions\\npc\\br\\bh_grp_br_trade.ini'


class BhTradeBrTLR(Encounter):
    NICKNAME = 'bh_grp_br_trade_tlr'
    FILENAME = 'missions\\npc\\br\\bh_grp_br_trade_tlr.ini'


class BhPatrolBr(Encounter):
    NICKNAME = 'bh_grp_br_patrol'
    FILENAME = 'missions\\npc\\br\\bh_grp_br_patrol.ini'


class BhTradeKu(Encounter):
    NICKNAME = 'bh_grp_ku_trade'
    FILENAME = 'missions\\npc\\ku\\bh_grp_ku_trade.ini'


class BhTradeKuTLR(Encounter):
    NICKNAME = 'bh_grp_ku_trade_tlr'
    FILENAME = 'missions\\npc\\ku\\bh_grp_ku_trade_tlr.ini'


class BhPatrolKu(Encounter):
    NICKNAME = 'bh_grp_ku_patrol'
    FILENAME = 'missions\\npc\\ku\\bh_grp_ku_patrol.ini'


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
