# Pythonlancer и файлы Freelancer

Описание ядра до нейросетей. Первое внедрение модели — VoiceStudio
(`31d214995`, Integrate VoiceStudio). До этого коммита в `tools/` нет
`voicestudio.py` и `voice_api.py`. Голос синтезирует внешний сервис,
не локальная сеть. RPG-писатели (`rpg_scene`, `rpg_audio`, парковка)
к этому ядру не относятся.

Рабочий каталог — `Assets/Pythonlancer`. Игра — на два уровня выше,
`D:\Games\FL_MOD`. Отсюда `DataFolder` берёт корень.

## Куда пишется

Три выхода, их нельзя смешивать.

`results/` — черновики. `files/writer.py` пишет только сюда: дампы строк
`results/ru`, `results/en`, временный голос Steos. Игра это не читает.

`DATA/` — живое дерево, которое запускает `bin\freelancer.exe`.
Единственная дверь — `tools/data_folder.py`, класс `DataFolder`.
Генератор не открывает файл в `DATA` сам, не копирует и не удаляет.
Новый вид контента — новый метод `DataFolder`, не прямой `write_text`.
Читать `DATA` напрямую можно.

`BUILDS/<RU|EN>_<EASY|NORMAL|HARD>/` — снимок того же дерева под язык
и сложность. `DataFolder(build_to_folder=...)` подменяет корень на
`BUILDS/<имя>`. Лаунчер при старте копирует выбранный снимок поверх
живого корня и только потом запускает exe.

Часть методов при снимке молчит и пишет только в живой `DATA`:
астероиды, туманности, энкаунтеры, `dock_key.ini`, аудио-ini, катсцены,
мимика. Снаряжение, рынки, `universe.ini` и системы уходят и в снимок.

## Запуск

`run_ru.py` / `run_en.py` поднимают лаунчер (`startup/launcher.py`).
Он не генерирует вселенную. Он пишет опции через `OptionsManager`,
копирует готовый `BUILDS/...` в корень и стартует exe из `EXE`.

Снимок собирает `build.py`: шесть прогонов `LancerCore(write=True)`
с языком и `difficulty`. Туда же кладутся equip/good, лут, лоадауты
миссий. Строки ids при этом остаются в `results/`, не в `DATA`.

`single.py` — ручной стенд: один объект, одна сцена, один голос.
`get_core()` создаёт ядро с `write=False` и ничего в игру не кладёт.

`LancerCore` собирает менеджеры. `write=True` разрешает им синхронизацию.
Порядок в конструкторе важен: вселенная после магазина и населения,
население дорисовывается уже после систем.

## Из класса в ini

Контент — Python-классы плюс Jinja в `templates/`.
`JinjaTemplateManager` подставляет поля в каркас ini. Готовый текст
уходит в `DataFolder`.

Вселенная: `universe/systems`, базы, рынки, ключи доков.
`UniverseManager.sync_data` пишет:

- `DATA/UNIVERSE/universe.ini`, `DATA/MISSIONS/mbases.ini`
- `initialworld.ini`, `newplayer.fl`, `empathy.ini`, `dacom.ini`
- систему в `DATA/UNIVERSE/<SYSTEMS_ROOT>/<SYSTEM_FOLDER>/<name>.ini`
- лоадауты соларов в `DATA/SHIPS`
- интерьеры в `DATA/UNIVERSE/GENERATED_INTERIORS` и `GENERATED_ROOMS`
- энкаунтеры в `DATA/MISSIONS/NPC/GENERATED`, если это не снимок

Система с `ALLOW_SYNC = False` не пишется.

Снаряжение и корабли: `WeaponManager`, `MiscEquipManager`, `ShiparchManager`,
`StoreManager`, `NPCArmorManager`. Файлы — `DATA/EQUIPMENT/.../GENERATED`
и корни equip, которые подключает шаблон.

Миссии: `managers/script.py` собирает реплики и субтитры,
`managers/story.py` — ini миссии, RTC и `npcships.ini` в
`DATA/MISSIONS/<folder>`. Катсцена — `Scene.sync_content` →
`DATA/SCRIPTS/GENERATED/<scene>.thn`. В снимок катсцена не входит.

Шаблоны статичных ini лежат в `templates/hardcoded_inis/static_content/`.
Генератор дописывает блок, шаблон держит каркас, который игра уже ждёт.

## Голос до VoiceStudio

Реплика — `VoiceLine` в `story/scripts`, актёр — `story/actors.py`.
Ник `DX_<mission>_<alias>_<index>_<actor>`. Длительность берётся с wav,
не из числа в THN.

Синтез — HTTP. `tools/steos.py` ходит в Steos по `STEOS_ID` актёра и
кладёт байты в `results/steos`. `tools/elevenlabs.py` — второй внешний
TTS. Локальной модели нет.

В игру файл попадает только через `DataFolder`: `move_story_audio`,
`sync_audio_ini`, `sync_subtitles`, `sync_mission_voice_props`.
Это живой `DATA/AUDIO` и `DATA/MISSIONS/voice_properties.ini`.
На снимке эти методы либо молчат, либо бросают исключение.

Мимика без мета — `facial(index, auto_lip=True)`. Когда мета записана,
`auto_lip` снимается. Рабочий файл губ — `DATA/SCRIPTS/WORKSPACE/facial.thn`.

## Чего ядро не делает

Не патчит exe и не пишет в `DLLS\BIN`. Лаунчер только копирует снимок
и стартует `EXE`.

Не хранит позиции катсцены в ini. Поза — дамп Blender
`Assets/SCENES/DUMPS`, сцена — класс `Scene`. Подробности постановки —
`docs/story_cutscenes.md`.

Не заменяет ручные THN миссий 1–7, пока у них нет `THORN_CLASS`.
Генератор их не трогает.
