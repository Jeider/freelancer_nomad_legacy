HOW_TO_HACK = ('\\n\\n'
               'To hack this panel you must fire on blocks with correct colors. '
               'Fire at different blocks with one of your guns. '
               'Those blocks will activate sounds corresponding to this color. '
               '\\n\\n'
               'Different blocks produce different sounds depending on the distance to the desired color: '
                "Maximal, Very high, High, Medium. Low, Very low, Minimal."
               '\\n\\n'
               'Correct color will be named as "maximal". Sound marks, how far this color is from the correct color. '
               'Nearest color will be high or very high, farest color will be low or minimal.'
               '\\n\\n'
               'Find maximal color and destroy all blocks of such color. Access to base will be granted after '
               'collecting the dropped key.')

ROID_MINER = ('In order to access to roid miner, you need to find key in one of the nearest asteroids. '
              'Correct asteroid will be marked by green color and sound of your interface. Attack and check '
              'asteroids, find correct asteroid, destroy it, get the key and access to roid miner will be granted')

GAS_MINING_GUNS = (
    'Not all your guns can liquify the gas. Looks at description of your guns. Some guns marked as effective for '
    'liquefaction job. You need a lot of time to liquify the gas without such guns. Recommended to have at least one '
    'gun with effective gas liquefaction.'
)
AST_MISSILES = (
    'Hint: all missiles, mines and torpedoes (including cheap) have big efficiency with mining of static asteroids.'
)
DEBRIS_MISSILES = (
    'Hint: all missiles, mines and torpedoes (including cheap) have big efficiency with mining of static debris.'
)

GAS_MINER_OLD = ('In order to access to this gas miner you need to find key on of the nearest ice '
                 'asteroids. You need to destroy segments of ice asteroids and get free gas puffs. Next you must '
                 'liquefy the gas by your guns. Each successful liquefaction of gas will appear correct asteroid. It '
                 'will be marked by color and sound of your interface. Liquify all gas inside correct asteroid, collect '
                 'dropped key and access to gas miner will be granted'
                 '\\n\\n' + GAS_MINING_GUNS +
                 '\\n\\n' + AST_MISSILES)

ASTEROID_ICE = ('In order to access to this abandoned research base you need to find key on of the nearest ice '
                'asteroids. You need to destroy segments of ice asteroids and get free gas puffs. Next you must '
                'liquefy the gas by your guns. Each successful liquefaction of gas will appear correct asteroid. It '
                'will be marked by color and sound of your interface. Liquify all gas inside correct asteroid, collect '
                'dropped key and access to base will be granted'
                '\\n\\n' + GAS_MINING_GUNS +
                '\\n\\n' + AST_MISSILES)

ASTEROID_ROCK = ('In order to get access to abandoned research base you need to find the key in one of the nearest '
                 'asteroids. Correct asteroid will be marked by green color and sound of your interface. '
                 'Attack and check asteroids, find correct asteroid, destroy it, get the key and then gain access '
                 'to the base '
                 '\\n\\n' + AST_MISSILES)

DEBRIS_MANUFACTORING = ('In order to get access to this smelter you should attack debris box racks. '
                        'Destroy the boxes until you get the access key. '
                        'Correct debris boxes will be marked by a green visual effect and some sound effect. '
                        'You don\'t need to destroy all the boxes of all the racks. '
                        'Find the correct debris box rack, destroy all of its boxes, get the access key and access to '
                        'this smelter will be granted'
                        '\\n\\n' + DEBRIS_MISSILES)

BATTLESHIP_HACKABLE = ('In order to get access to this battleship you should hack the doors by hackable panel, placed on '
                       'this battleship. Hack the panel and get the key. You can dock to the base after successful hack.'
                       '' + HOW_TO_HACK)

BATTLESHIP_LOCKED = ('In order to get access to this battleship, you should collect the key from one of the ship '
                     'wrecks placed near this base. Use your interface to easily find correct ship: access key is '
                     'a blue mounted component on the ship. Switch targets and look at visual projection of wreck. '
                     'Attack correct fighter with your guns, collect the key and gain access.')

LUXURY_LOCKED = ('In order to get access to this luxury liner, you should collect the key from one of the ship '
                 'wrecks placed near this base. Use your interface to easily find correct ship: access key is '
                 'a blue mounted component on the ship. Switch targets and look at visual projection of wreck. '
                 'Attack correct fighter with your guns, collect the key and gain access.')

HACKABLE_LUXURY = ('In order to access to this luxury liner you should hack the doors by hackable panel, '
                   'placed on this luxury liner. Hack the panel and get the key. You can dock to '
                   'the base after successful hack.'
                   '' + HOW_TO_HACK)

HACKABLE_SOLAR_PLANT = ('In order to get access to this power plant, you should hack the doors thanks to the '
                        'hackable panel on this solar plant. Hack the panel and get the key. You can '
                        'dock to the base after successful hack.'
                        '' + HOW_TO_HACK)

SOLAR_PLANT = ('In order to get access to this power plant, you should collect the key from one of the ship '
               'wrecks placed near this base. Use your interface to easily find correct ship: access key is '
               'a blue mounted component on the ship. Switch targets and look at visual projection of wreck. '
               'Attack correct fighter with your guns, collect the key and gain access.')

STATION_RUINS = 'You can find hackable docking points near this ruins.'

HACKABLE_STATION = ('In order to get access to docking point, you should hack the doors thanks to the '
                    'hackable panel on this docking point. Hack the panel and get the key. You can '
                    'dock to the base after successful hack.'
                    '' + HOW_TO_HACK)
