Freelancer Subtitles preview
============================

How to install
--------------

0. Install Freelancer. :) Subtitles have been tested with an out-of-the-box installation, the 1.4 unofficial patch, and 1.4 with the Russian exe (it's unprotected, was easier to debug).

1. If you don't have it already, install the .NET Framework v4.5.1. (needed for Converter.exe)

2. Start up Freelancer and set the resolution you want to play with. Widescreen resolutions haven't been tested. If you happen to change it while Subtitles is loaded (don't), restart the game to let it pick up the new resolution you're using. Use one of the "x 32" resolutions for good measure, though I suspect that Freelancer does 32-bit even if you select 16.

3. Edit EXE\dacom.ini. Look for this line:

;LOCAKABLE_BACKBUFFER= false ; should the device allow the backbuffer to be locked

Change the entire line to "LOCKABLE_BACKBUFFER=true" without the quotes (note that LOCKABLE has a typo, you need to fix that as well). Be sure to remove the first semicolon.

4. Copy d3d8.dll, Converter.exe, subtitles.dat, and subtitles.cfg to Freelancer's EXE folder.

5. Edit subtitles.cfg if you intend to customize where subtitles appear.

6. Run Converter.exe (just double-click on it). If it pops up a message box, something has gone wrong, please check the console for errors and report it. This will create flsd.dat which is tailored for your system and flsc.dat that stores your configuration. These will be read by Freelancer. If you wish, you can delete Converter.exe, subtitles.xml, and subtitles.cfg at this point.

7. Enjoy :) Subtitles.xml contains captions for the FP7 intro, the arrival on Manhattan, landing on Pittsburgh, about half of King's lines spoken in-game, and the Lonnigan scene before mission 2.

How to uninstall
----------------
Delete these files: d3d8.dll, subtitles.xml, subtitles.cfg, flsd.dat, flsc.dat, and Converter.exe if desired. Just renaming d3d8.dll is enough to disable subtitles, your game will be untouched then.
You can also undo the edits you made in dacom.ini if you want.

System requirements
-------------------

You'll need a DirectX 9 capable GPU, as well as DirectX 10.1 or higher installed on your system. You'll need Windows Vista or higher, Windows XP is not supported. With Subtitles loaded, Freelancer will use more CPU and memory than usual.

Troubleshooting
---------------

- Everything became bright!
This is the death cry of Subtitles (actually a bug that I know how to fix, but it's very useful so I'm leaving it in for now). Something has gone wrong internally. Double-check your dacom.ini and try using a different resolution. If you can reliably reproduce it, please give me a shout, and mention the GPU you have and driver version.

- Subtitles don't work at all!
If you don't even see them in the intro, and things are not super bright, it will be something related to audio. Try toggling the 3D option in Freelancer, and/or uncommenting (removing the semicolon from) the ;speakerConfiguration = 2 line in dacom.ini. Please report the sound card you're using and your speaker configuration (headphones, stereo, surround, etc.).

Known issues, unimplemented bits
--------------------------------

Subtitles look a bit different from in-game text (less sharp). This is due to DirectWrite anti-aliasing everything even if I tell it not to.

Pausing the game (F1) while subtitles are on can't be supported with my approach. Dynamic subtitles will de-sync, static subtitles will disappear and not come back when the game is resumed. This will only affect subtitles that are currently on, subsequent ones will play OK.

Cinematic subtitles have an opaque background. This is actually a workaround. Without it they would randomly disappear.

You can add several lines of text to a sound, but multiple sounds forming a single line is not yet implemented (example: "Understood. Your request" + "to land" + "is granted. Proceed" + "to land")

Subtitles.xml format
--------------------

No documentation now due to laziness, but it should be pretty self-explanatory from the entries already there. UTF keys are case sensitive (that's how they're encoded in the file, it actually spells out 0, x, 8 hex digits) and UTF folders are unimplemented.

You can technically assign captions to the "Debug" TextArea.

Subtitles.cfg format
--------------------

Refer to the comments inside the file.
