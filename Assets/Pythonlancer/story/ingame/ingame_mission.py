class IngameMission(object):
    pass


class NagVoice(object):
    DEFINITION = '''
[NPC] 
nickname = npc_nnvoice
affiliation = li_n_grp
npc_ship_arch = nnvoice_shiparch
space_costume = , robot_body_E
individual_name = 089999
voice = nn_mod

[MsnShip]
nickname = nag_voice
NPC = npc_nnvoice
jumper = false
label = the_nnvoice
position = 0,-50000,0

'''

    def get_definition(self):
        return self.DEFINITION


class Ship(object):
    DEFINIION = '''
[NPC]
nickname = alaric_m1
affiliation = fc_uk_grp
npc_ship_arch = MSN01_alaric
space_costume = rh_alaric_head_hat, pi_pirate6_body, comm_rh_alaric
individual_name = 091204
voice = pilot_f_mil_m01

[MsnShip]
nickname = MSN01_Alaric
NPC = alaric_m1
jumper = true
label = m1_friend
label = friend    
'''