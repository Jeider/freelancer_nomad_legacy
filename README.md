[Русская версия](#rus-ver)

[English version](#eng-ver)

<a id='eng-ver'>Eng version</a>

# Русская версия {#rus-ver}

## Мод для Freelancer: Наследие Номадов.

Это фанатский проект. Все права принадлежат Microsoft и Digital Anvil.

Вы можете скачать проект с github, но игра не может быть запущена, не будучи установленной на вашу копию игры Freelcner.

После распаковки проекта поверх Freelancer вы должны запустить RUN_russian.bat. Это запустит лончер и позволит вам выбрать настройки и играть.

Больше о проекте на https://freelancer2.space/ru

## Системные требования

Windows 10 и новее, 64 бит (запустить на других версиях Windows можно, но без лончера)

Права на доступ файлов к записи

Активированный Direct Play

## Дополнительно

Некоторые файлы могут считать вирусом как вредоносные. Их нужно добавить в исключения. Причина этого: большинство расширений к движку Freelancer работает по той же схеме, что и вирусы. И система может их неверно определять как вирусные файлы.

## Как отключить обновления при запуске лончера

Лончер смотрит на наличие папки .git в корне. Просто переименуйте эту папку и тогда игра не будет обновляться. Эта папка скрытая и её по умолчанию не видно.

## Как запускать игру баз лончера

Игра по умолчанию настроена на FullHD экран. Вы можете запустить файл EXE/Freelancer.exe и играть. Если разрешение экрана FullHD, 2k, то проблем быть не должно

Чтобы запустить игру в окне нужно запустить EXE/Freelancer.bat. Если вам не нравится окно cmd, то вы можете сделать ярлык от файла Freelancer_window.exe и добавьте -w в конце параметра "объект".

## Как настроить игру без лончера под кастомное разрешение

### Включить визуальные улучшения

В папке STATIC вы можете найти файл d3d8_dxwrapper.dll. Переименуйте его в d3d8.dll и положите в папку EXE

В папке STATIC найдите d3d9_reshade.dll и тоже положите в EXE. Это запустит Reshade. Внимание! Не используйте Reshade в оконном режиме!

### Настройка отображения статусов корабля

Нужно настроить данный файл

https://github.com/Jeider/freelancer_nomad_legacy/blob/master/DATA/INTERFACE/HudShift.ini

Если у вас экран 4:3 (1024x768) или 5:4 (1280x1024), то вы можете найти готовый HudShift.ini в папке RESOLUTIONS. Просто заменить нужным файлом файл DATA/INTERFACE/HudShift.ini

Если у вас более сложное разрешение, то нужно настроить Horizontal и позицию статуса корабля.

Вот данные, по которым работает лончер: https://github.com/Jeider/freelancer_nomad_legacy/blob/master/Assets/Pythonlancer/startup/meta.json#L34

horizontal это "Текущее значение horizontal" в HudShift.ini. Ищите такой комментарий в файле
	
status_shift это "Позиция статус корабля это второе значение следующего параметра" в HudShift.ini. Ищите такой комментарий в файле

wide_weapons это параметр HudWeaponGroups в самом верху HudShift.ini. Если в мета-данных ваше разрешение должно иметь значение false, то надо выставить false в HudShift.ini 

### Настройки шрифтов

Если у вас 4к монитор или просто не влезает текст скорости, то вы должны поправить шрифты. Посмотрите на данный файл:

https://github.com/Jeider/freelancer_nomad_legacy/blob/master/DATA/FONTS/fonts.ini#L41

Найдите записи с текстом "Edit this font for ultrawide" и заменить fixed_height в обоих случаях на значение 0.02. Тогда шрифт будет влезать.

### Переключение сложности вручную

Откройте папку BUILDS. Там есть 3 русских билда: RU_EASY, RU_NORMAL, RU_HARD. По умолчанию стоит RU_NORMAL. Чтобы  переключить сложность просто скопируйте DATA и EXE и вставьте их содержимое в папки в корне. Если что, лончер делает точно такую же операцию

# English version {#eng-ver}

## Freencer mod The Nomad Legacy

This is fan project. All rights to original game belong to Microsoft and Digital Anvil.

You can download mod by gi	thub, but this files is unplayable without original Freelancer files. You MUST have original Freelancer to play this mod.

More about project at https://freelancer2.space/en

## System requirements

Windows 10 and newer, 64 bit (it's possible to run on other version of Windows, but without launcher)

Write records inside FL folder

Activated Direct Play

## Additional

Some files can be marked as viruses by your anti-virus. That's because some engine extensions for Freelancer is working like "viruses". This is not real viruses, but your system can wrongly detect them.