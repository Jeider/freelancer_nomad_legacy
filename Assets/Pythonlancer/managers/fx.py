from tools.data_folder import DataFolder

from fx.alchemy import FX
from fx.sound import AutoSoundFX

from text.dividers import DIVIDER


class FxManager:
    def __init__(self, lancer_core):
        self.core = lancer_core

        self.effects = []
        self.vis_effects = []
        self.sounds = []
        self.sound_equips = []
        self.sound_loadouts = []

        self.init_effects()

        self.sync_data()

    def init_effects(self):
        for fx in FX.subclasses:
            for member in fx.get_members():
                self.effects.append(
                    fx.get_effect(member)
                )
                if not fx.REFERENCE:
                    self.vis_effects.append(
                        fx.get_vis_effect(member)
                    )

        sound_fx = AutoSoundFX(russian=self.core.russian)
        for member in sound_fx.get_members():
            self.effects.append(
                sound_fx.get_effect(member)
            )
            self.sounds.append(
                sound_fx.get_sound(member)
            )
            self.sound_equips.append(
                sound_fx.get_equip(member)
            )
            self.sound_loadouts.append(
                sound_fx.get_loadout(member)
            )

    def get_effects_content(self):
        return DIVIDER.join(self.effects)

    def get_vis_effects_content(self):
        return DIVIDER.join(self.vis_effects)

    def get_sound_content(self):
        return DIVIDER.join(self.sounds)

    def get_sound_equip_content(self):
        return DIVIDER.join(self.sound_equips)

    def get_sound_loadouts_content(self):
        return DIVIDER.join(self.sound_loadouts)

    def sync_data(self):
        if not self.core.write:
            return
        data_folder = DataFolder(build_to_folder=self.core.build_folder)
        data_folder.sync_effects(self.get_effects_content())
        data_folder.sync_vis_effects(self.get_vis_effects_content())
        data_folder.sync_sound(self.get_sound_content())
        data_folder.sync_equip('sound_equip', 'GENERATED', self.get_sound_equip_content())
        data_folder.sync_solar_gen_sound_loadouts(self.get_sound_loadouts_content())
