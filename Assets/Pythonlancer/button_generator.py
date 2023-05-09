x1 = 25500
x2 = 53
x3 = 81070

/*
type 1 - impulse
type 2 - impulse + shield/hull
type 3 - shield/hull

*/


red_unlocker5 = 'hacker_red_unlocker'
red_unlocker6 = 'hacker_red_unlocker'
red_trigger = 'hacker_red_trigger'
red_empty = 'hacker_red_empty'

blue_unlocker5 = 'hacker_blue_unlocker'
blue_unlocker6 = 'hacker_blue_unlocker'
blue_trigger = 'hacker_blue_trigger'
blue_empty = 'hacker_blue_empty'

green_unlocker5 = 'hacker_green_unlocker'
green_unlocker6 = 'hacker_green_unlocker'
green_trigger = 'hacker_green_trigger'
green_empty = 'hacker_green_empty'



nickname_format = 'nickname = om15_02_hack_b{}'
pos_format = 'pos = {}, {}, {}'

poses = [
    (-9.5, -9.5),
    (-3.25, -9.5),
    (-9.5, -3.25),
    (-3.25, -3.25),
    
    (-9.5, 9.5),
    (-3.25, 9.5),
    (-9.5, 3.25),
    (-3.25, 3.25),
    
    (9.5, -9.5),
    (3.25, -9.5),
    (9.5, -3.25),
    (3.25, -3.25),
    
    (9.5, 9.5),
    (3.25, 9.5),
    (9.5, 3.25),
    (3.25, 3.25),
  
]

i = 1

for xa, xb in poses:
    print('[Object]')
    print(nickname_format.format(i))
    print(pos_format.format(x1 + xa, x2, x3 + xb))
    print('rotate = 0, 180, 0')
    print('archetype = hacker_button_red')
    print('')
    
    i += 1


