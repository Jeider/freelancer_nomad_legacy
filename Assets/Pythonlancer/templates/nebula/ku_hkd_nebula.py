from templates.simple_template import SimpleTemplate


class KuHkdOrangeNebulaTemplate(SimpleTemplate):
    TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\walker_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 2000
color = 150, 100, 20 ;120, 60, 0

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
plane_slices = 8
bit_radius = 6000
bit_radius_random_variation = 0.500000
min_bits = 5
max_bits = 9
move_bit_percent = 0.500000
equator_bias = 0.500000
color = 255, 255, 255


[NebulaLight]
ambient = 150, 100, 20
sun_burnthrough_intensity = 0.500000
sun_burnthrough_scaler = 2

[Clouds]
max_distance = 1500
puff_count = 200
puff_radius = 150
puff_colora = 250, 180, 70
puff_colorb = 60, 43, 0
puff_max_alpha = 0.3
puff_shape = walker_cloud1
puff_shape = walker_cloud2
puff_shape = walker_cloud3
puff_shape = walker_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 3.000000
near_fade_distance = 100, 200

[BackgroundLightning]
duration = 0.550000
gap = 4.000000
color = 0, 0, 0

'''


class HokkaidoBarrierNebulaTemplate(SimpleTemplate):
    TEMPLATE = '''[TexturePanels]
file = solar\\nebula\\generic_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 1800
color = 130, 80, 60

[Exclusion Zones]
{exclusions}

[properties]
flag = nebula

[Exterior]
shape = generic_exterior1
shape = generic_exterior2
shape = generic_exterior3
shape = generic_exterior4
shape_weights = 1, 1, 1, 1
fill_shape = white_circle
plane_slices = 3
bit_radius = 7000
bit_radius_random_variation = 0.200000
min_bits = 7
max_bits = 15
move_bit_percent = 0.750000
equator_bias = 0.500000
color = 140, 40, 80

[NebulaLight]
ambient = 75, 40, 30
sun_burnthrough_intensity = 0.700000
sun_burnthrough_scaler = 1.750000

[Clouds]
max_distance = 1500
puff_count = 100
puff_radius = 100
puff_colora = 200, 40, 150
puff_colorb = 140, 40, 80
puff_max_alpha = 0.5
puff_shape = generic_cloud1
puff_shape = generic_cloud2
puff_shape = generic_cloud3
puff_shape = generic_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 1.000000
near_fade_distance = 125, 200

[BackgroundLightning]
duration = 0.750000
gap = 10.000000
color = 55, 50, 60




'''
