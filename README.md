[Русская версия](#rus-ver)

[English version](#eng-ver)

<a id='rus-ver'></a>

# Русская версия

## Мод для Freelancer: Наследие Номадов.

Это фанатский проект. Все права принадлежат Microsoft и Digital Anvil.

Вы можете скачать проект с github, но игра не может быть запущена, не будучи установленной на вашу копию игры Freelcner.

После распаковки проекта поверх Freelancer вы должны запустить RUN_russian.bat. Это запустит лончер и позволит вам выбрать настройки и играть.

Больше о проекте на https://freelancer2.space/ru

## Системные требования

Windows 10 и новее, 64 бит (запустить на других версиях Windows можно, но без лончера)

Права на доступ файлов к записи (не используйте Program Files, фрил точно потеряет права на запись)

Активированный Direct Play

## Дополнительно

Некоторые файлы могут считать вирусом как вредоносные. Их нужно добавить в исключения. Причина этого: большинство расширений к движку Freelancer работает по той же схеме, что и вирусы. И система может их неверно определять как вирусные файлы.

## Как отключить обновления при запуске лончера

Лончер смотрит на наличие папки .git в корне. Просто переименуйте эту папку и тогда игра не будет обновляться. Эта папка скрытая и её по умолчанию не видно.

## Как запускать игру баз лончера

Игра по умолчанию настроена на FullHD экран. Вы можете запустить файл EXE/Freelancer.exe и играть. Если разрешение экрана FullHD, 2k, то проблем быть не должно

Чтобы запустить игру в окне нужно запустить EXE/Freelancer.bat. Если вам не нравится окно cmd, то вы можете сделать ярлык от файла Freelancer_window.exe и добавьте -w в конце параметра "объект" в свойствах ярлыка.

### Включить визуальные улучшения

В папке STATIC вы можете найти файл d3d8_dxwrapper.dll. Переименуйте его в d3d8.dll и положите в папку EXE

В папке STATIC найдите d3d9_reshade.dll, переименуйте в d3d9.dll и тоже положите в EXE. Так же скопируйте ReShade.ini и ReShadePreset.ini и положите в папку EXE. Это запустит Reshade. Внимание! Не используйте Reshade в оконном режиме!

### Переключение сложности вручную

Откройте папку BUILDS. Там есть 3 русских билда: RU_EASY, RU_NORMAL, RU_HARD. По умолчанию стоит RU_NORMAL. Чтобы  переключить сложность просто скопируйте DATA и EXE и вставьте их содержимое в папки в корне. Если что, лончер делает точно такую же операцию

## Как настроить игру без лончера под кастомное разрешение

### Настройка отображения статусов корабля

Нужно настроить данный файл

https://github.com/Jeider/freelancer_nomad_legacy/blob/master/DATA/INTERFACE/HudShift.ini

Если у вас экран 4:3 (1024x768) или 5:4 (1280x1024), то вы можете найти готовый HudShift.ini в папке RESOLUTIONS. Просто заменить нужным файлом файл DATA/INTERFACE/HudShift.ini

Если у вас более сложное разрешение, то нужно настроить Horizontal и позицию статуса корабля.

Вот данные, по которым работает лончер: https://github.com/Jeider/freelancer_nomad_legacy/blob/master/Assets/Pythonlancer/startup/meta.json#L34

horizontal это "Текущее значение horizontal" в HudShift.ini. Ищите такой комментарий в файле hudshift.ini
	
status_shift это "Позиция статус корабля это второе значение следующего параметра" в HudShift.ini. Ищите такой комментарий в файле hudshift.ini

wide_weapons это параметр HudWeaponGroups в самом верху HudShift.ini. Если в мета-данных ваше разрешение должно иметь значение false, то надо выставить false в HudShift.ini 

### Настройки шрифтов

Если у вас 4к монитор или просто не влезает текст скорости, то вы должны поправить шрифты. Посмотрите на данный файл:

https://github.com/Jeider/freelancer_nomad_legacy/blob/master/DATA/FONTS/fonts.ini#L41

Найдите записи с текстом "Edit this font for ultrawide" и заменить fixed_height в обоих случаях на значение 0.02. Тогда шрифт будет влезать.

<a id='eng-ver'></a>

### Субтитры в катсценах (инструкция на случай нерабочего лончера, в лончере эта функция лежит в категории "опасных")

Доступны субтитры в катсценах, но это экспериментальная фича. Смена языка происходит вместе со сменой уровня сложности. По умолчанию субтитры не лежат в игре - см. раздел "переключение сложности вручную". Скопируйте RU_NORMAL в папку основной игры и субтитры появятся в папке EXE.

Важно! Субтитры не совместимы с dxwrapper и reshade. Вы должны удалить их d3d8.dll и d3d9.dll.

Следом чтобы установить субтитры нужно скопировать файл STATIC/d3d8_sub.dll и положить в папку EXE.

Далее запускайте файл EXE/Converter.exe. Он должен обработать озвучку. Операция может зависнуть и даже намертво. В этом случае просто удалите процесс Converter.exe вашим диспетчером задач и попробуйте запустить его снова. До тех пор, пока он не выдаст результат.

Если результат не получается и вы хотите откатить результат, то просто удалить d3d8.dll от субтитров.

# English version

## Freencer mod The Nomad Legacy

This is fan project. All rights to original game belong to Microsoft and Digital Anvil.

You can download mod by gi	thub, but this files is unplayable without original Freelancer files. You MUST have original Freelancer to play this mod.

More about project at https://freelancer2.space/en

## System requirements

Windows 10 and newer, 64 bit (it's possible to run on other version of Windows, but without launcher)

Write rules inside FL folder (for example - do not place game inside Program Files)

Activated Direct Play

## Additional

Some files can be marked as viruses by your anti-virus. That's because some engine extensions for Freelancer is working like "viruses". This is not real viruses, but your system can wrongly detect them.

## How to disable sync progress on open of launcher

Launcher looks on ".git" folder inside project folder. Just rename this folder and Launcher will not sync game with github and internet. Warning! This folder is hidden, you must appear it before this operation.

## How to run game withot launcher

Game by default have installed russian version.  You must switch difficulty to english one

[Change difficulty](#toggle-diff-en)

After change difficulty you can run the game. Game by default configured for FullHD screen. Run file EXE/Freelancer_en.exe and play. Resolutions like FullHD and 2K will work without problems.

To run game in windows mode you should run EXE/Freelancer_en.bat. If you don't want to see cmd window, you can make shortcut for file Freelancer_window_en.exe. Append -w in end of parameter "object" in properties of your shortcut.

### Enable visual improvements

Inside STATIC folder you can find d3d8_dxwrapper.dll. Переименуйте его в d3d8.dll и положите в папку EXE

Inside STATIC folder you can find d3d9_reshade.dll, rename it to d3d9.dll and also place it in EXE. Also copy ReShade.ini and ReShadePreset.ini and paste inside EXE folder. It will run Reshade. YOU MUST NOT USE IT IN WINDOW MODE!

<a id='toggle-diff-en'></a>

### Toggle difficulty manual

Open BUILDS folder. There 3 english builds: EN_EASY, EN_NORMAL, EN_HARD. By default it use RUSSIAN RU_NORMAL. To run english version you must switch game to any english difficulty. Just open folder with build, copy DATA and EXE and overwrite files in root project folder. Launcher also did same opearation when it switch difficulty, so you can do it without problems.

## How to run game without launcher with custom resolution

### Settings of status window

Find this file

https://github.com/Jeider/freelancer_nomad_legacy/blob/master/DATA/INTERFACE/HudShift.ini

If you have

If you have screen 4:3 (1024x768) or 5:4 (1280x1024) you can find created HudShift.ini inside RESOLUTIONS folder. Just find hudShift.ini inside required screen aspect ratio eand replace it over DATA/INTERFACE/HudShift.ini

If you have unique aspect ratio, you must configure Horizontal and position of ship status bar.

This data used by launcher: https://github.com/Jeider/freelancer_nomad_legacy/blob/master/Assets/Pythonlancer/startup/meta.json#L34

horizontal is "Actual horizontal value" в HudShift.ini. Find this comment inside hudshift.ini
	
status_shift is "Position of PlayerStatus is second value of next parameter" в HudShift.ini. Find this comment inside hudshift.ini

wide_weapons is a parameter HudWeaponGroups on the top of HudShift.ini. If value in metadata should bе false, you must set value "false" of this paramter inside HudShift.ini 

### Configure fonts

If you have 4k monitor you not see speed and truster capacity, you must fix fonts. Open this file:

https://github.com/Jeider/freelancer_nomad_legacy/blob/master/DATA/FONTS/fonts.ini#L41

Find text "Edit this font for ultrawide" and change value of  fixed_height of both sections to 0.02. Font will be appeared after this change

### Subtitles in cutscenes (it also available in launcher as dangerous setting)

Subtitles in cutscenes is allowed as experimtal feature. Switch of launcher is happened together when you switch difficulty. By default there's no subtitles in game - look at "change difficulty" section. Copy EN_NORMAL to main game and subtitles will be appear. That's the same for any english difficulty.

Important! Subtitles not compatible with dxwrapper and reshade. You must delete d3d8.dll and d3d9.dll of this features.

Next turn - you need copy STATIC/d3d8_sub.dll and place it in EXE folder of main project.

Next you need to run EXE/Converter.exe. It should process sounds. Operation can be freezed forever. In this case you must remove Converter.exe process by your Windows Task Manager and try to run Conveter.exe again. Do it until Conveter.exe will show you successs result.

You have wrong result and want to remove subtitles? Just remove d3d8.dll of subtitles.
