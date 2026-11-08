"""Build the first static RPG contact. Pure generation; never modifies the game by default.

May also be run from Pythonlancer/tools/rpg_contacts.py after installation.
"""
import argparse
from pathlib import Path

# TODO: Игнорирование внедрения во фрил через DataFolder недопустимо: только DataFolder меняет саму игру


CONTACT = "rpg_biz_contact"
BASE = "rh_biz_01_base"
SPOT = "Zg/NPC/mFloor2/01/A/Stand"
FIDGET = r"scripts\extras\fidget_stand_male_01.thn"
CLICK_SCRIPT = r"scripts\generated\m10_offer_accept.thn"

# Native special marker/camera mapping resolves these against the contact's spot.
# The client loops this entry until a dialogue choice closes it.
CHOICE_THN = '''duration=60
entities={
 {entity_name="RpgChoiceScene",type=SCENE,template_name="",spatialprops={pos={0,0,0},orient={{1,0,0},{0,1,0},{0,0,1}}}},
 {entity_name="RpgMonitor",type=MONITOR,template_name=""},
 {entity_name="special/p",type=MARKER,template_name="",spatialprops={pos={0,0,0},orient={{1,0,0},{0,1,0},{0,0,1}}}},
 {entity_name="camera/PCU",type=CAMERA,template_name="",spatialprops={pos={0,0,0},orient={{1,0,0},{0,1,0},{0,0,1}}},cameraprops={fovh=30,hvaspect=1.333333,nearplane=0.1,farplane=10000}},
 {entity_name="RpgPlayer",type=DEFORMABLE,template_name="trent",flags=LIT_DYNAMIC,spatialprops={pos={0,0,0},orient={{1,0,0},{0,1,0},{0,0,1}}},userprops={Actor="Player",category="Character"}}
}
events={
 {0,ATTACH_ENTITY,{"RpgPlayer","special/p"},{duration=60,offset={0,0,0},target_type=ROOT,flags=POSITION+ORIENTATION}},
 {0,START_MOTION,{"RpgPlayer"},{animation="Sc_MLBODY_STND_IDLE_000LV_XB_04",duration=60,time_scale=1,start_time=0,weight=1,heading=-1,event_flags=2}},
 {0,SET_CAMERA,{"RpgMonitor","camera/PCU"}}
}
'''


def generate(destination: Path):
    files = {
        "DATA/RPG/contacts.ini": f"""; Generated static RPG catalog. No StoryLauncher dependency.
[RpgContact]
nickname = {CONTACT}
enabled = true
base = {BASE}
rtc = RPG\\rh_biz_contact.ini

[RpgContact]
nickname = rpg_om15_dispatcher
enabled = true
base = om15_01_base
rtc = RPG\\om15_train_contact.ini

[RpgContact]
nickname = rpg_bremen_clerk
enabled = true
base = rh_biz_02_base
rtc = RPG\\rh_biz_02_clerk.ini
""",
        "DATA/RPG/rh_biz_02_clerk.ini": """[CharacterEncounter]
Location = rh_biz_02_base, Bar
click_script = scripts\\generated\\m10_offer_accept.thn
choices = true

[Reserve]
spot = Zg/NPC/mFloor1/01/A/Stand

[Char]
npc = rpg_bremen_clerk
actor = rpg_bremen_clerk
spot = Zg/NPC/mFloor1/01/A/Stand
fidget = scripts\\extras\\fidget_stand_male_01.thn

[NPC]
nickname = rpg_bremen_clerk
body = rh_male_guard_body
head = br_brighton_head
lefthand = benchmark_male_hand_left
righthand = benchmark_male_hand_right
accessory = prop_hat_male_rh_elite
affiliation = rh_grp
voice = rvp101
individual_name = 196847
""",
        "DATA/RPG/om15_train_contact.ini": """; Freeport Lubeck dispatcher. Cutscene, then a yes/no that starts the script.
[CharacterEncounter]
Location = om15_01_base, Bar
click_script = scripts\\generated\\m10_offer_accept.thn
choices = true
script_offer = true

[Reserve]
spot = Zg/NPC/mFloor1/01/A/Stand

[Char]
npc = rpg_om15_dispatcher
actor = rpg_om15_dispatcher
spot = Zg/NPC/mFloor1/01/A/Stand
fidget = scripts\\extras\\fidget_stand_male_01.thn

[NPC]
nickname = rpg_om15_dispatcher
body = rh_male_guard_body
head = br_brighton_head
lefthand = benchmark_male_hand_left
righthand = benchmark_male_hand_right
accessory = prop_hat_male_rh_elite
affiliation = rh_grp
voice = rvp101
individual_name = 196847
""",
        "DATA/RPG/rh_biz_contact.ini": f"""; RPG contact: idle animation and a self-contained story THN on click.
[CharacterEncounter]
Location = {BASE}, Bar
click_script = {CLICK_SCRIPT}
choices = true

[Reserve]
spot = {SPOT}

[Char]
npc = {CONTACT}
actor = {CONTACT}
spot = {SPOT}
fidget = {FIDGET}

; Local NPC catalog; deliberately independent of missions/specific_npc.ini.
[NPC]
nickname = {CONTACT}
body = rh_male_guard_body
head = br_brighton_head
lefthand = benchmark_male_hand_left
righthand = benchmark_male_hand_right
accessory = prop_hat_male_rh_elite
affiliation = rh_grp
voice = rvp101
; Existing localized Rheinland faction label until a named dialogue is authored.
individual_name = 196847
""",
    }
    files["DATA/RPG/dialogue_choice.thn"] = CHOICE_THN
    files["DATA/RPG/space.ini"] = """; One shared NPC, present while players are in this system.
[RpgShip]
nickname = rpg_biz_hassler
enabled = true
; Seconds after disappearance. Zero disables respawn until the world is reloaded.
respawn_seconds = 60
system = rh_biz
anchor = rh_biz_01
; World-space offset from the live docking ring, clear of the launch lane.
offset = -1000, 200, 400
ship_archetype = rh_elite
loadout = ms3_hassler
pilot = mod_fighter_universe
affiliation = fc_uk_grp
individual_name = 33604
head = rh_hassler_head
body = rh_male_elite_body
accessory = comm_rh_reichman
"""
    for relative, content in files.items():
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True,
                        help="Staging root; DATA/RPG is created beneath it")
    args = parser.parse_args()
    generate(args.output)
    print("Generated", args.output / "DATA/RPG")
