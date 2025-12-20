class DifficultySettings:
    NPC_ARMOR_SCALE = 2
    NPC_SHIELD_CAPACITY_SCALE = 1
    NPC_SHIELD_REGENERATION_SCALE = 1
    #
    M6_NOMAD_ZONE_LAZER_DAMAGE = True
    M6_NOMAD_ZONE_LAZER_KILL_ALL_NOMADS = False
    M6_NOMAD_ZONE_LAZER_KERNEL_DAMAGE_PCT = 3  # 30 percent
    M6_REITHERMAN_ESCAPE_METHOD = 'goto_cruise'
    M6_RUNNER_RACE_METHOD = 'goto_cruise'
    M6_DOUBLE_TORPEDO = True
    M6_TORPEDO_DAMAGE = 150000
    #
    M9_SPAWN_DESTROYER_C = True
    M9_DESTROYER_B_DELAY = 60
    M9_DESTROYER_C_DELAY = 120
    M9_DESTROYER_D_DELAY = 150
    M9_DESTROYER_E_DELAY = 200
    M9_DESTROYER_F_DELAY = 300
    M9_DOUBLE_TORPEDO = True
    M9_TORPEDO_DAMAGE = 125000

    @classmethod
    def true(cls, attr):
        return getattr(cls, attr) is True

    @classmethod
    def false(cls, attr):
        return getattr(cls, attr) is False

    @classmethod
    def val(cls, attr):
        return getattr(cls, attr)


class EasyDifficulty(DifficultySettings):
    NPC_ARMOR_SCALE = 1
    NPC_SHIELD_CAPACITY_SCALE = 0.75
    NPC_SHIELD_REGENERATION_SCALE = 0.25
    #
    M6_NOMAD_ZONE_LAZER_DAMAGE = False
    M6_NOMAD_ZONE_LAZER_KILL_ALL_NOMADS = True
    M6_NOMAD_ZONE_LAZER_KERNEL_DAMAGE_PCT = 6  # 60 percent
    M6_REITHERMAN_ESCAPE_METHOD = 'goto_no_cruise'
    M6_RUNNER_RACE_METHOD = 'goto_no_cruise'
    M6_DOUBLE_TORPEDO = False
    M6_TORPEDO_DAMAGE = 75000
    #
    M9_SPAWN_WAVE_C = False
    M9_DESTROYER_B_DELAY = 60
    M9_DESTROYER_C_DELAY = 150  # Not spawn C wave
    M9_DESTROYER_D_DELAY = 150
    M9_DESTROYER_E_DELAY = 220
    M9_DESTROYER_F_DELAY = 300
    M9_DOUBLE_TORPEDO = False
    M9_TORPEDO_DAMAGE = 60000


class NormalDifficulty(DifficultySettings):
    NPC_ARMOR_SCALE = 1.5
    NPC_SHIELD_CAPACITY_SCALE = 1.5
    NPC_SHIELD_REGENERATION_SCALE = 0.5
    M6_TORPEDO_DAMAGE = 100000
    M9_SPAWN_WAVE_C = False
    M9_DESTROYER_B_DELAY = 60
    M9_DESTROYER_C_DELAY = 150  # Not spawn C wave
    M9_DESTROYER_D_DELAY = 150
    M9_DESTROYER_E_DELAY = 220
    M9_DESTROYER_F_DELAY = 300
    M9_TORPEDO_DAMAGE = 100000


class HardDifficulty(DifficultySettings):
    NPC_ARMOR_SCALE = 3
    NPC_SHIELD_CAPACITY_SCALE = 2
    NPC_SHIELD_REGENERATION_SCALE = 1
    M6_TORPEDO_DAMAGE = 150000
    M9_SPAWN_WAVE_C = True
    M9_DESTROYER_B_DELAY = 60
    M9_DESTROYER_C_DELAY = 120
    M9_DESTROYER_D_DELAY = 180
    M9_DESTROYER_E_DELAY = 220
    M9_DESTROYER_F_DELAY = 300


class ExtremeDifficulty(DifficultySettings):
    pass
