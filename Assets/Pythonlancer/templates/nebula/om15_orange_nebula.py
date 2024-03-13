from templates.simple_template import SimpleTemplate


class Omega15LargeNebulaTemplate(SimpleTemplate):
    TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\walker_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 1000
color = 150, 90, 20

[properties]
flag = nebula

[Exclusion Zones]
{exclusions}

[Exterior]
shape = walker_exterior1
shape = walker_exterior2
shape = walker_exterior3
shape = walker_exterior4
shape_weights = 1, 1, 1, 1
fill_shape = walker_circle
plane_slices = 7
bit_radius = 8000
bit_radius_random_variation = 0.200000
min_bits = 5
max_bits = 7
move_bit_percent = 0.500000
equator_bias = 0.500000
color = 255, 255, 255

[NebulaLight]
ambient = 80, 40, 0
sun_burnthrough_intensity = 0.500000
sun_burnthrough_scaler = 2

[Clouds]
max_distance = 1500
puff_count = 200
puff_radius = 100
puff_colora = 250, 180, 70
puff_colorb = 60, 43, 0
puff_max_alpha = 0.75
puff_shape = walker_cloud1
puff_shape = walker_cloud2
puff_shape = walker_cloud3
puff_shape = walker_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 3.000000
near_fade_distance = 125, 200
lightning_intensity = 1.000000
lightning_color = 150, 100, 0
lightning_gap = 3.000000
lightning_duration = 0.400000


[BackgroundLightning]
duration = 0.550000
gap = 4.000000
color = 40, 20, 10
'''



class Omega15DangerNebulaTemplate(SimpleTemplate):
    TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\walker_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 1000
color = 100, 60, 10

[properties]
flag = nebula

[Exclusion Zones]
{exclusions}

[Exterior]
shape = walker_exterior1
shape = walker_exterior2
shape = walker_exterior3
shape = walker_exterior4
shape_weights = 1, 1, 1, 1
fill_shape = walker_circle
plane_slices = 7
bit_radius = 6000
bit_radius_random_variation = 0.200000
min_bits = 5
max_bits = 7
move_bit_percent = 0.500000
equator_bias = 0.100000
color = 255, 255, 255

[NebulaLight]
ambient = 60, 40, 20
sun_burnthrough_intensity = 0.500000
sun_burnthrough_scaler = 2

[Clouds]
max_distance = 1500
puff_count = 200
puff_radius = 100
puff_colora = 255, 200, 0
puff_colorb = 80, 40, 0
puff_max_alpha = 0.500000
puff_shape = walker_cloud1
puff_shape = walker_cloud2
puff_shape = walker_cloud3
puff_shape = walker_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 3.000000
near_fade_distance = 150, 250
lightning_intensity = 1.000000
lightning_color = 150, 100, 0
lightning_gap = 3.000000
lightning_duration = 0.400000

[BackgroundLightning]
duration = 0.550000
gap = 4.000000
ambient = 60, 40, 20

[DynamicLightning]
gap = 2
duration = 0.550000
color = 255, 150, 0
ambient_intensity = 1
intensity_increase = 1

'''

class Omega15SmallNebulaTemplate(SimpleTemplate):
    TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\walker_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 1000
color = 150, 90, 20

[properties]
flag = nebula

[Exclusion Zones]
{exclusions}

[Exterior]
shape = walker_exterior1
shape = walker_exterior2
shape = walker_exterior3
shape = walker_exterior4
shape_weights = 1, 1, 1, 1
fill_shape = walker_circle
plane_slices = 7
bit_radius = 6000
bit_radius_random_variation = 0.200000
min_bits = 5
max_bits = 7
move_bit_percent = 0.500000
equator_bias = 0.100000
color = 255, 255, 255

[NebulaLight]
ambient = 80, 40, 0
sun_burnthrough_intensity = 0.500000
sun_burnthrough_scaler = 2

[Clouds]
max_distance = 1500
puff_count = 200
puff_radius = 100
puff_colora = 128, 85, 0
puff_colorb = 60, 43, 0
;puff_colora = 0, 255, 0
;;puff_colorb = 0, 0, 255
puff_max_alpha = 0.500000
puff_shape = walker_cloud1
puff_shape = walker_cloud2
puff_shape = walker_cloud3
puff_shape = walker_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 3.000000
near_fade_distance = 150, 250
lightning_intensity = 1.000000
lightning_color = 150, 100, 0
lightning_gap = 3.000000
lightning_duration = 0.400000

[BackgroundLightning]
duration = 0.550000
gap = 4.000000
color = 40, 20, 10

'''


class Omega15NorthStoryNebulaTemplate(SimpleTemplate):
    TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\walker_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 1000
color = 150, 90, 20
opacity = 0.5

[properties]
flag = nebula

[Exclusion Zones]
exclusion = Zone_OM15_MS2_EXCLUSION
fog_far = 12500.000000
zone_shell = solar\\nebula\\walker_exclusion.3db
shell_scalar = 1.000000
max_alpha = 0.30000
exclusion_tint = 200, 200, 200


[Exterior]
shape = walker_exterior1
shape = walker_exterior2
shape = walker_exterior3
shape = walker_exterior4
shape_weights = 1, 1, 1, 1
fill_shape = walker_circle
plane_slices = 7
bit_radius = 6000
bit_radius_random_variation = 0.500000
min_bits = 6
max_bits = 12
move_bit_percent = 0.500000
equator_bias = 0.000000
color = 255, 255, 255


[NebulaLight]
ambient = 80, 40, 0
sun_burnthrough_intensity = 0.500000
sun_burnthrough_scaler = 2

[Clouds]
max_distance = 1500
puff_count = 200
puff_radius = 100
puff_colora = 128, 85, 0
puff_colorb = 60, 43, 0
;puff_colora = 0, 255, 0
;;puff_colorb = 0, 0, 255
puff_max_alpha = 0.500000
puff_shape = walker_cloud1
puff_shape = walker_cloud2
puff_shape = walker_cloud3
puff_shape = walker_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 3.000000
near_fade_distance = 125, 200
lightning_intensity = 1.000000
lightning_color = 150, 100, 0
lightning_gap = 3.000000
lightning_duration = 0.400000
disable_clouds = 0

[BackgroundLightning]
duration = 0.550000
gap = 4.000000
color = 40, 20, 10

'''