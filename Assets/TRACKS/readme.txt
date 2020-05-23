; This is the format used by Tracks.  A single section here will generate the
; multiple sections that Freelancer wants.  Tracks accepts multiple files, each
; file will restore the default settings.  Multiple settings can be used in a
; single file, but if you use a different system the trade lane and path
; numbers are not reset (i.e. if you want them to restart at 1, you must
; explicitly set them so).


[Settings]
system = LINE		; used for nicknames
distance = FLOAT	; default distance between trade lane rings (7000)
reputation = LINE	; default reputation for rings
loadout = LINE		; default loadout for rings

[TradeLane]
number = INT		; nickname suffix (previous ring + 1)
distance = FLOAT	; override settings
count = INT		; number of intermediate rings (based on distance)
first = FLOAT, FLOAT, FLOAT, INT  ; point and ids of first ring
last = FLOAT, FLOAT, FLOAT, INT   ; point and ids of last ring
reputation = STRING	; override settings
loadout = LINE		; override settings (no per-ring loadout, yet)
			; (difficulty_level and pilot are not used)
zone = FLOAT[, INT]	; if present generate zone with size (width & height),
			;  nickname number (previous zone + 1)
; everything else copied to the zone (lane_id and tradelane_down are not used)

[Path]
name = STRING[, INT]	; used to generate nickname and path_label, combined
			;  with the number (previous number + 1)
usage = LINE		; trade (patrol)
pos = FLOAT, FLOAT, FLOAT  ; start point
pos = FLOAT, FLOAT, FLOAT[, return]  ; end point
tradelane_attack = FLOAT  ; specific to this leg (attack_ids is not used)
pos = ...		; repeat for each leg
; everything else copied to each leg


; That will generate (values enclosed in percents are substituted with an
; appropriate value):


[Object]		; for each ring
nickname = %SYSTEM%_Trade_Lane_Ring_%NUMBER%
ids_name = 260921
pos = %POS%
rotate = %ROTATE%
Archetype = Trade_Lane_Ring
ids_info = 66170
prev_ring = %NICKNAME-1%	; if not FIRST
next_ring = %NICKNAME+1%	; if not LAST
behavior = NOTHING
tradelane_space_name = %IDS%	; if FIRST or LAST
reputation = %REPUTATION%
loadout = %LOADOUT%

[Zone]			; if ZONE
nickname = Zone_%SYSTEM%_Tradelane_%NUMBER%
pos = %POS%		; midpoint of FIRST and LAST
rotate = %ROTATE%
shape = BOX
size = %SIZE%, %SIZE%, %DISTANCE+%SIZE%%  ; distance between FIRST and LAST
%COPY%

[Zone]			; for each leg
nickname = Zone_%SYSTEM%_path_%NAME%_%NUMBER%
pos = %POS%
rotate = %ROTATE%
shape = CYLINDER
size = 750, %DISTANCE%
usage = %USAGE%
path_label = %NAME%, %NUMBER%, %LEGS-NUMBER+1%	; last value only if return
tradelane_attack = %TRADELANE_ATTACK%	; if present
%COPY%
