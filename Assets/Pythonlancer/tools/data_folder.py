import pathlib
import shutil
import json

LOADOUTS_GEN = 'loadout_gen.ini'



def get_and_create(folder):
    if not folder.exists():
        folder.mkdir()
    return folder


class DataFolder:

    def __init__(self, build_to_folder=None, *, root=None):
        self.root = pathlib.Path(root).resolve() if root is not None else pathlib.Path().resolve().parent.parent
        self.build_to_folder = build_to_folder
        if self.build_to_folder:
            self.root = self.root / 'BUILDS' / self.build_to_folder

    # Central DATA output API, also used for staging and installation rollback.
    def data_path(self, relative):
        relative = pathlib.Path(str(relative).replace('\\', '/'))
        if (relative.is_absolute() or relative.drive or not relative.parts or
                '..' in relative.parts or any(':' in part for part in relative.parts)):
            raise ValueError('Expected a path relative to DATA: ' + str(relative))
        root = (self.get_root() / 'DATA').resolve()
        target = (root / relative).resolve()
        if not target.is_relative_to(root) or target == root:
            raise ValueError('Path escapes DATA: ' + str(relative))
        return target

    def sync_data_file(self, relative, content):
        target = self.data_path(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, str):
            target.write_text(content, encoding='utf-8')
        else:
            target.write_bytes(content)
        return target

    def remove_data_file(self, relative):
        # Only an individual DATA file; never remove a directory recursively.
        self.data_path(relative).unlink(missing_ok=True)

    def sync_ship_parking(self, files):
        for relative in files:
            name = str(relative).replace('\\', '/')
            if not (name in ('RPG/ship_parking.ini', 'RPG/parking_contacts.ini') or
                    (name.startswith('RPG/parking/') and name.endswith('.ini'))):
                raise ValueError('Unexpected ship parking file: ' + name)
            self.data_path(name)
        for relative, content in files.items():
            self.sync_data_file(relative, content)


    # BEGIN RPG AUDIO OUTPUT
    def rpg_bin_path(self, name):
        if name not in ('freelancer.ini', 'freelan_en_port.ini'):
            raise ValueError('Unexpected RPG audio launch configuration')
        root = self.get_root().resolve()
        path = (root / 'bin' / name).resolve()
        if not path.is_relative_to(root / 'bin'):
            raise ValueError('RPG launch configuration escaped bin')
        return path

    def sync_rpg_bin_file(self, name, content):
        path = self.rpg_bin_path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)

    def sync_rpg_audio(self, group, files, configs, backup_root):
        """One group's audio transaction. All DATA writes and rollback stay here."""
        import re
        if not re.fullmatch(r'rm[0-9]{4}', group):
            raise ValueError('Invalid RPG audio group')
        for relative in files:
            wav = re.fullmatch(r'AUDIO/(MOD|MOD_ENG)/RPG/' + group + '/' + group +
                               r'_frag[0-9]{4}_l001_(vendor|player)\.wav', relative)
            if not wav and relative not in (f'AUDIO/RPG/{group}.json', f'AUDIO/RPG/{group}_sounds.ini'):
                raise ValueError('Unexpected RPG audio target: ' + relative)
            self.data_path(relative)
        for name in configs:
            self.rpg_bin_path(name)
        self._sync_rpg_files(group, files, configs, backup_root)

    def sync_rpg_scenes(self, group, files, backup_root):
        import re
        if not re.fullmatch(r'rm[0-9]{4}', group):
            raise ValueError('Invalid RPG scene group')
        for relative in files:
            pattern = (r'SCRIPTS/RPG/' + group + r'/(ru|en)/(' + group +
                       r'_frag[0-9]{4}\.thn|manifest\.json|subtitles\.xml)')
            gesture = r'SCRIPTS/RPG/' + group + r'/gestures/(vendor|player)_0[1-8]\.thn'
            if not re.fullmatch(pattern, relative) and not re.fullmatch(gesture, relative):
                raise ValueError('Unexpected RPG scene target: ' + relative)
            self.data_path(relative)
        self._sync_rpg_files(group, files, {}, backup_root)

    def _sync_rpg_files(self, group, files, configs, backup_root):
        backup_root = pathlib.Path(backup_root).resolve()
        if backup_root == self.get_root().resolve() or backup_root.is_relative_to(self.data_path('AUDIO').parent):
            raise ValueError('Backup must be outside game DATA')
        backup = DataFolder(root=backup_root)
        before = {name: self.data_path(name).read_bytes() if self.data_path(name).exists() else None
                  for name in files}
        before_configs = {name: self.rpg_bin_path(name).read_bytes() for name in configs}
        changed = {name: content for name, content in files.items() if before[name] != content}
        changed_configs = {name: content for name, content in configs.items() if before_configs[name] != content}
        for name in changed:
            if before[name] is not None:
                backup.sync_data_file(name, before[name])
        for name in changed_configs:
            backup.sync_rpg_bin_file(name, before_configs[name])
        backup_root.mkdir(parents=True, exist_ok=True)
        (backup_root / 'transaction.json').write_text(json.dumps({
            'group': group, 'destination': str(self.get_root()),
            'data_files': {name: before[name] is not None for name in changed},
            'bin_files': list(changed_configs)}, indent=2), encoding='utf-8')
        touched, touched_configs = [], []
        try:
            for name, content in changed.items():
                touched.append(name)
                self.sync_data_file(name, content)
            for name, content in changed_configs.items():
                touched_configs.append(name)
                self.sync_rpg_bin_file(name, content)
        except Exception:
            for name in reversed(touched_configs):
                self.sync_rpg_bin_file(name, before_configs[name])
            for name in reversed(touched):
                if before[name] is None:
                    self.remove_data_file(name)
                else:
                    self.sync_data_file(name, before[name])
            raise
    def sync_rpg_runtime(self, files, backup_root):
        allowed = {'RPG/rm0001_dialog.ini', 'RPG/rh_biz_contact.ini', 'SCRIPTS/RPG/conversation.thn'}
        if set(files) != allowed:
            raise ValueError('Unexpected RPG runtime targets')
        for relative in files:
            self.data_path(relative)
        self._sync_rpg_files('rm0001', files, {}, backup_root)
    def sync_rpg_parking_runtime(self, files, backup_root):
        allowed = {'RPG/rm0002_dialog.ini', 'RPG/parking/br_avl_01_base.ini'}
        if set(files) != allowed:
            raise ValueError('Unexpected Avalon parking runtime targets')
        for relative in files:
            self.data_path(relative)
        self._sync_rpg_files('rm0002', files, {}, backup_root)
    # END RPG AUDIO OUTPUT

    def sync_parking_commandants(self, files, backup_root):
        """Atomic commandants, additive parking hotspots and missing base definitions."""
        import re
        allowed = {'RPG/ship_parking.ini', 'RPG/parking_contacts.ini',
                   'Interface/Baseside/navbar.ini', 'Interface/Baseside/parking_p.3db',
                   'Universe/SYSTEMS_MOD/CO_MADRID/co_mad_04_base.ini',
                   'Universe/DANGEON/ARCH/arch_01_base.ini',
                   'Universe/DANGEON/HEAVY_BARREL2/heavy_barrel2_01_base.ini'}
        for name in files:
            # Room edits are constrained to the additive parking-hotspot transform.
            room = name.lower().startswith('universe/') and name.lower().endswith('.ini') and name not in allowed
            if room:
                from managers.parking_rooms import ensure_parking_hotspot, LANDING_PATHS
                from managers.parking_commandants import parse, one
                content = files[name]
                if isinstance(content, str): content = content.encode('utf-8')
                declared_dealer = name.lower() in LANDING_PATHS
                if not declared_dealer and not any(k == 'hotspot' and one(r, 'behavior').lower() == 'startshipdealer'
                           for k, r in parse(content)):
                    raise ValueError('Room is not a ship dealer: ' + name)
                if ensure_parking_hotspot(content, declared_dealer) != content:
                    raise ValueError('Missing parking hotspot: ' + name)
                target = self.data_path(name)
                if target.exists() and ensure_parking_hotspot(target.read_bytes(), declared_dealer) != content:
                    raise ValueError('Room changed since planning or edit is not additive: ' + name)
                continue
            if (name not in allowed and
                    not re.fullmatch(r'RPG/parking/[a-z0-9_]+_base\.ini', name) and
                    not re.fullmatch(r'RPG/rm[0-9]{4}_dialog\.ini', name) and
                    not re.fullmatch(r'SCRIPTS/RPG/rm[0-9]{4}/conversation\.thn', name)):
                raise ValueError('Unexpected parking commandant target: ' + name)
            self.data_path(name)
        self._sync_rpg_files('parking_commandants', files, {}, backup_root)

    def sync_courier_owners(self, files, backup_root):
        """Publish locomotive contacts, catalog and required transfer registrations."""
        import re
        allowed = {'RPG/courier_contacts.ini', 'RPG/rh_biz_contact.ini',
                   'MISSIONS/TrainCourier/catalog.ini', 'UNIVERSE/universe.ini', 'MISSIONS/mbases.ini'}
        for name in files:
            if (name not in allowed and
                    not re.fullmatch(r'UNIVERSE/TrainCourier/tc_[a-z0-9_]+_base\.ini', name) and
                    not re.fullmatch(r'MISSIONS/TrainCourier/launch_[a-z0-9_]+\.ini', name) and
                    not re.fullmatch(r'RPG/courier/[a-z0-9_]+_base(?:_dialog)?\.ini', name) and
                    not re.fullmatch(r'SCRIPTS/RPG/rm[0-9]{4}/(?:conversation\.thn|gestures/(?:vendor|player)_0[1-8]\.thn)', name)):
                raise ValueError('Unexpected courier owner target: ' + name)
            self.data_path(name)
        self._sync_rpg_files('courier_owners', files, {}, backup_root)


    def sync_parking_ui(self, files, backup_root):
        """Publish the parking button and presentation-only RPG contact icon edits."""
        import re
        allowed = {'Interface/Baseside/navbar.ini', 'Interface/Baseside/parking_p.3db',
                   'RPG/rh_biz_contact.ini'}
        for name in files:
            if name not in allowed and not re.fullmatch(r'RPG/(?:parking|courier)/[a-z0-9_]+\.ini', name):
                raise ValueError('Unexpected parking UI target: ' + name)
            self.data_path(name)
            if name.startswith('RPG/'):
                original = self.data_path(name).read_bytes()
                content = files[name]
                # Changing the marker must never rewrite the actor or dialogue.
                strip = lambda data: re.sub(rb'(?im)^icon\s*=[^\r\n]*\r?\n', b'', data)
                if strip(original) != strip(content):
                    raise ValueError('Contact edit is not icon-only: ' + name)
                icons = re.findall(rb'(?im)^icon\s*=\s*(mission|rumor)\s*$', content)
                if len(icons) != 1:
                    raise ValueError('Expected one valid contact icon: ' + name)
        self._sync_rpg_files('parking_ui', files, {}, backup_root)

    def sync_service_reputation(self, files, backup_root):
        import re
        for name in files:
            if (name != 'RPG/ship_parking.ini' and
                    not re.fullmatch(r'RPG/(?:parking/[a-z0-9_]+|courier/[a-z0-9_]+_base_dialog|rm[0-9]{4}_dialog)\.ini', name)):
                raise ValueError('Unexpected service reputation target: '+name)
            self.data_path(name)
        self._sync_rpg_files('service_reputation',files,{},backup_root)

    def get_root(self):
        return self.root

    def get_static(self):
        return get_and_create(self.get_root() / 'STATIC')

    def get_data(self):
        return get_and_create(self.get_root() / 'DATA')

    def get_exe(self):
        return get_and_create(self.get_root() / 'EXE')

    def get_save(self):
        return get_and_create(self.get_root() / 'SAVE')

    def get_d3d8(self):
        return self.get_exe() / 'd3d8.dll'

    def get_d3d9(self):
        return self.get_exe() / 'd3d9.dll'

    def get_reshade_props1(self):
        return self.get_exe() / 'ReShade.ini'

    def get_reshade_props2(self):
        return self.get_exe() / 'ReShadePreset.ini'

    def get_base_dxwrapper(self):
        return self.get_static() / 'd3d8_dxwrapper.dll'

    def get_base_subtitles(self):
        return self.get_static() / 'd3d8_sub.dll'

    def get_base_reshade_d3d9(self):
        return self.get_static() / 'd3d9_reshade.dll'

    def get_base_reshade_props1(self):
        return self.get_static() / 'ReShade.ini'

    def get_base_reshade_props2(self):
        return self.get_static() / 'ReShadePreset.ini'

    def get_autosave(self):
        raise Exception('obsolete')

        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        return self.get_root() / 'SAVE' / 'Accts' / 'SinglePlayer' / 'AutoSave.fl'

    def get_crashes_root(self):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        folder = self.get_save() / 'CrashData'
        if not folder.exists():
            folder.mkdir()
        return folder

    def get_audio(self):
        return get_and_create(self.get_data() / 'AUDIO')

    def get_equip(self):
        return get_and_create(self.get_data() / 'EQUIPMENT')

    def get_solar(self):
        return get_and_create(self.get_data() / 'SOLAR')

    def get_universe(self):
        return get_and_create(self.get_data() / 'UNIVERSE')

    def get_missions(self):
        return get_and_create(self.get_data() / 'MISSIONS')

    def get_random_missions(self):
        return get_and_create(self.get_data() / 'RANDOMMISSIONS')

    def get_ships(self):
        return get_and_create(self.get_data() / 'SHIPS')

    def get_interface(self):
        return get_and_create(self.get_data() / 'INTERFACE')

    def get_fx(self):
        return get_and_create(self.get_data() / 'FX')

    def get_fonts(self):
        return get_and_create(self.get_data() / 'FONTS')

    def get_scripts(self):
        return get_and_create(self.get_data() / 'SCRIPTS')

    def get_player(self):
        return get_and_create(self.get_data() / 'PLAYER')

    def get_characters(self):
        return get_and_create(self.get_data() / 'CHARACTERS')

    def get_cutscene_audio_ru(self):
        if self.build_to_folder:
            return

        return get_and_create(self.get_audio() / 'MOD')

    def get_cutscene_audio_en(self):
        if self.build_to_folder:
            return

        return get_and_create(self.get_audio() / 'MOD_ENG')

    def sync_fuse(self, fuse_name, content):
        loadouts_file = self.get_fx() / f'{fuse_name}.ini'
        loadouts_file.write_text(content, encoding='utf-8')

    def sync_effects(self, content):
        if self.build_to_folder:
            return

        equip_file = self.get_fx() / 'effects_gen.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_vis_effects(self, content):
        if self.build_to_folder:
            return

        equip_file = get_and_create(self.get_fx() / 'GENERATED') / 'gen_ale.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_sound(self, content):
        if self.build_to_folder:
            return

        equip_file = self.get_audio() / 'sounds_gen.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_solar_gen_loadouts(self, content):
        loadouts_file = self.get_solar() / LOADOUTS_GEN
        loadouts_file.write_text(content, encoding='utf-8')

    def sync_solar_gen_sound_loadouts(self, content):
        loadouts_file = self.get_solar() / 'loadout_gen_sound.ini'
        loadouts_file.write_text(content, encoding='utf-8')

    def sync_solar_gen_store_loadouts(self, content):
        loadouts_file = self.get_solar() / 'loadout_gen_store.ini'
        loadouts_file.write_text(content, encoding='utf-8')

    def sync_to_test_workspace(self, content, workspace_index=''):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        system_file = self.get_universe() / 'GENERATION_DATA' / 'WORKSPACE' / f'test{workspace_index}.ini'
        system_file.write_text(content, encoding='utf-8')

    def sync_system(self, system_name, system_root, system_folder, content):
        system_file = get_and_create(get_and_create(self.get_universe() / system_root) / system_folder) / f'{system_name}.ini'
        system_file.write_text(content, encoding='utf-8')

    def sync_asteroid_definition(self, definition_name, subfolder, content):
        if self.build_to_folder:
            return

        asteroid_file = self.get_solar() / 'ASTEROIDS_MOD' / subfolder / f'{definition_name}.ini'
        asteroid_file.write_text(content, encoding='utf-8')

    def sync_templated_nebula(self, nebula_file_name, subfolder, content):
        if self.build_to_folder:
            return

        nebula_file = self.get_solar() / 'NEBULA_MOD' / subfolder / f'{nebula_file_name}.ini'
        nebula_file.write_text(content, encoding='utf-8')

    def sync_custom_encounters(self, encounter_filename, content):
        if self.build_to_folder:
            return

        nebula_file = self.get_missions() / 'NPC' / 'GENERATED' / f'{encounter_filename}.ini'
        nebula_file.write_text(content, encoding='utf-8')

    def sync_interior(self, interior_file_name, content):
        if self.build_to_folder:
            return

        asteroid_file = self.get_universe() / 'GENERATED_INTERIORS' / f'{interior_file_name}.ini'
        asteroid_file.write_text(content, encoding='utf-8')

    def sync_interior_room(self, room_file_name, content):
        if self.build_to_folder:
            return

        asteroid_file = self.get_universe() / 'GENERATED_ROOMS' / f'{room_file_name}.ini'
        asteroid_file.write_text(content, encoding='utf-8')

    def sync_equip_root(self, equip_file_name, content):
        equip_file = self.get_equip() / f'{equip_file_name}.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_equip(self, equip_file_name, subfolder, content):
        equip_file = get_and_create(self.get_equip() / subfolder) / f'{equip_file_name}.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_equip_hardcoded(self, equip_file_name, content):
        equip_file = self.get_equip() / f'{equip_file_name}.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_knowledge_map(self, content):
        equip_file = self.get_interface() / 'knowledgemap.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_infocard_map(self, content):
        equip_file = self.get_interface() / 'infocardmap.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_universe(self, content):
        equip_file = self.get_universe() / 'universe.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_initial_world(self, content):
        equip_file = self.get_data() / 'initialworld.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_new_player(self, content):
        equip_file = self.get_exe() / 'newplayer.fl'
        equip_file.write_text(content, encoding='utf-8')

    def sync_empathy(self, content):
        equip_file = self.get_missions() / 'empathy.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_dacom(self, content):
        equip_file = self.get_exe() / 'dacom.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_subtitles(self, content):
        equip_file = self.get_exe() / 'subtitles.xml'
        equip_file.write_text(content, encoding='utf-8')

    def get_perf_options(self):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        perf_file = self.get_save() / 'PerfOptions.ini'
        if perf_file.exists():
            opened_file = open(perf_file)
            file_content = opened_file.readlines()
            opened_file.close()
            return file_content
        return ''

    def get_startup_settings(self):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        data_file = self.get_save() / 'startup_settings.json'
        data = {}
        if data_file.exists():
            with open(data_file) as db_file:
                data = json.load(db_file)
        return data

    def save_startup_settings(self, settings):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        with open(self.get_save() / 'startup_settings.json', 'w') as data_file:
            json.dump(settings, data_file)

    def sync_perf_options(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_save() / 'PerfOptions.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_hud_shift(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_interface() / 'HudShift.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_cameras(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_data() / 'cameras.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_front_light(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_player() / 'front_light.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_contrail(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_player() / 'contrail.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_player_bodyparts(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_characters() / 'bodyparts_player.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_fonts(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_fonts() / 'fonts.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_vignettes(self, content):
        equip_file = self.get_random_missions() / 'VignetteParams.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_mbases(self, content):
        equip_file = self.get_missions() / 'mbases.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_npcships(self, content):
        equip_file = self.get_missions() / 'npcships.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_faction_prop(self, content):
        equip_file = self.get_missions() / 'faction_prop.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_lootprops(self, content):
        equip_file = self.get_missions() / 'lootprops.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_shiparch(self, content):
        equip_file = self.get_ships() / 'shiparch2.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_shiparch_alt(self, content):  # make alt as main
        equip_file = self.get_ships() / 'shiparch.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_ships_loadouts(self, content):
        equip_file = self.get_ships() / 'loadout_gen.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_msn_ships_loadouts(self, content):
        equip_file = self.get_ships() / 'loadout_msn.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_story_ships_loadouts(self, content):
        equip_file = self.get_ships() / 'loadout_gen_story.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_custom_enc_ships_loadouts(self, content):
        equip_file = self.get_ships() / 'loadout_gen_custom_enc.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_dock_key(self, content):
        if self.build_to_folder:
            return

        equip_file = self.get_data() / 'dock_key.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_story_mission(self, folder, file, content):
        equip_file = get_and_create(self.get_missions() / folder) / f'{file}.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_story_npcships(self, folder, content):
        equip_file = get_and_create(self.get_missions() / folder) / f'npcships.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_story_ingame_thorn(self, file, content):
        if self.build_to_folder:
            return

        equip_file = self.get_missions() / 'GENERATED_THORN' / f'{file}.thn'
        equip_file.write_text(content, encoding='utf-8')

    def sync_audio_ini(self, file, content):
        if self.build_to_folder:
            return

        equip_file = self.get_audio() / f'{file}.ini'
        equip_file.write_text(content, encoding='utf-8')

    def sync_mission_voice_props(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        equip_file = self.get_missions() / 'voice_properties.ini'
        equip_file.write_text(content, encoding='utf-8')

    def move_story_audio(self, original_file_destination, out_file_name):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        shutil.move(
            original_file_destination,
            self.get_audio() / out_file_name
        )

    def sync_facial(self, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        facial_file = self.get_scripts() / 'WORKSPACE' / 'facial.thn'
        facial_file.write_text(content, encoding='utf-8')

    def sync_scene(self, scene_name, content):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        facial_file = self.get_scripts() / 'GENERATED' / f'{scene_name}.thn'
        facial_file.write_text(content, encoding='utf-8')

    def get_facial(self):
        if self.build_to_folder:
            raise Exception('Impossible to use with build')

        facial_file = open(self.get_scripts() / 'WORKSPACE' / 'facial.thn')
        file_content = facial_file.readlines()
        facial_file.close()
        return file_content


    def place_dxwrapper(self):
        self.remove_all_d3d8_wrappers()

        shutil.copy(
            self.get_base_dxwrapper(),
            self.get_d3d8()
        )

    def place_subtitles(self):
        self.remove_all_d3d8_wrappers()

        shutil.copy(
            self.get_base_subtitles(),
            self.get_d3d8()
        )

    def place_reshade(self):
        self.remove_all_d3d9_wrappers()

        shutil.copy(
            self.get_base_reshade_d3d9(),
            self.get_d3d9()
        )

        prop1 = self.get_reshade_props1()
        if not prop1.exists():
            shutil.copy(self.get_base_reshade_props1(), prop1)

        prop2 = self.get_reshade_props2()
        if not prop2.exists():
            shutil.copy(self.get_base_reshade_props2(), prop2)

    def remove_all_d3d8_wrappers(self):
        d3d8 = self.get_d3d8()
        if d3d8.exists():
            self.get_d3d8().unlink()

    def remove_all_d3d9_wrappers(self):
        d3d9 = self.get_d3d9()
        if d3d9.exists():
            self.get_d3d9().unlink()

    def remove_redundant_files(self):
        nnvoice = self.get_audio() / 'nnvoice.utf'
        trent_voice = self.get_audio() / 'trent_voice.utf'
        if nnvoice.exists():
            nnvoice.unlink()
        if trent_voice.exists():
            trent_voice.unlink()
