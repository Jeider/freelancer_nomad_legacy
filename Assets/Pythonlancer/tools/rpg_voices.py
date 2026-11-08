"""Prepare/record/install audio for one selected RPG base-dialogue group."""
import argparse
from pathlib import Path
import re

from managers.rpg_voice import RpgVoiceManager


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["prepare", "voices", "install-audio", "build", "scenes", "runtime", "owners"])
    parser.add_argument("--group", default="rm0001")
    parser.add_argument("--language", choices=["ru", "en", "both"], default="both")
    parser.add_argument("--vendor-actor", help="Override this group's vendor actor; default from catalog casting")
    parser.add_argument("--dry-run", action="store_true", help="Plan without generation or game writes")
    parser.add_argument("--output", type=Path, help="Recording sheets/plan only; never DATA")
    parser.add_argument("--game-root", type=Path, help="Installation target; default is the working FL_MOD game")
    args = parser.parse_args(argv)
    if not re.fullmatch(r"rm[0-9]{4}", args.group):
        parser.error("--group must be rmNNNN")
    if args.command not in ('voices', 'build') and args.vendor_actor:
        parser.error('--vendor-actor is only used for voice generation')
    if args.command == 'prepare' and args.dry_run:
        parser.error('prepare only exports recording sheets; omit --dry-run')
    if args.command not in ('build', 'install-audio', 'scenes', 'runtime', 'owners') and args.game_root:
        parser.error('--game-root is only used for audio installation')
    root = Path(__file__).resolve().parents[1]
    output = args.output or root / "results/rpg" / args.group / args.command / args.language
    if args.command == 'owners':
        from core import get_core
        from tools.data_folder import DataFolder
        from managers.courier_owners import generate
        _, _, report = generate(get_core().universe, DataFolder(root=args.game_root or root.parent.parent),
                                root, output, args.dry_run)
        print(f'Locomotive owners: {len(report)} bases')
        return
    manager = RpgVoiceManager(root, root / "story/rpg" / (args.group + ".json"))
    if manager.script.name != args.group:
        parser.error("Catalog ID does not match --group")
    languages = ("ru", "en") if args.language == "both" else (args.language,)
    if args.command == "prepare":
        manager.prepare(output)
    elif args.command == 'voices':
        manager.voices(output, languages, args.vendor_actor, args.dry_run)
    elif args.command == 'scenes':
        from managers.rpg_scene import RpgSceneManager
        scenes = RpgSceneManager(root, manager.script, args.game_root)
        report = scenes.build(languages, output, args.dry_run)
        print(f'{"Planned" if args.dry_run else "Built"}: {report["fragments"]} THN fragments; runtime connection pending')
    elif args.command == 'runtime':
        from managers.rpg_runtime import install_runtime
        install_runtime(root, manager.script, args.game_root, output, args.dry_run)
    else:
        from managers.rpg_audio import RpgAudioManager
        audio = RpgAudioManager(root, manager.script, args.game_root)
        if args.command == 'build':
            # Fail on a wrong target before starting potentially long generation.
            for name in ('freelancer.ini', 'freelan_en_port.ini'):
                if not audio.folder.rpg_bin_path(name).is_file():
                    parser.error(f'Missing working game configuration: {name}')
            manager.voices(output, languages, args.vendor_actor, args.dry_run)
            if args.dry_run:
                print(f'After recording, this group alone will be installed into {audio.game}/DATA/AUDIO')
                return
        report = audio.install(languages, output, args.dry_run)
        print(f'{"Planned" if args.dry_run else "Installed"}: {report["recordings"]} recordings for {args.group}')
    print(f"{args.group}: {len(manager.script.fragments)} lines per language; {args.command}; {output.resolve()}")


if __name__ == "__main__":
    main()
