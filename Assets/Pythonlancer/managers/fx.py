from tools.data_folder import DataFolder

from fx.alchemy import FX

from text.dividers import DIVIDER


class FxManager:
    def __init__(self, lancer_core):
        self.core = lancer_core

        self.effects = []
        self.vis_effects = []

        self.init_effects()

        self.sync_data()

    def init_effects(self):
        for fx in FX.subclasses:
            for member in fx.get_members():
                self.effects.append(
                    fx.get_effect(member)
                )
                self.vis_effects.append(
                    fx.get_vis_effect(member)
                )

    def get_effects_content(self):
        return DIVIDER.join(self.effects)

    def get_vis_effects_content(self):
        return DIVIDER.join(self.vis_effects)

    def sync_data(self):
        if not self.core.write:
            return
        data_folder = DataFolder(build_to_folder=self.core.build_folder)
        data_folder.sync_effects(self.get_effects_content())
        data_folder.sync_vis_effects(self.get_vis_effects_content())
