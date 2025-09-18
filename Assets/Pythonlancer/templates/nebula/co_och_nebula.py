from templates.simple_template import SimpleTemplate


class OchEdgeNebulaTemplate(SimpleTemplate):
	TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\generic_shapes.ini
file = solar\\nebula\\edge_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 1400
color = 40, 80, 60

[properties]
flag = nebula

[Exclusion Zones]
{exclusions}

[Exterior]
shape = edge_exterior1
shape = edge_exterior2
shape = edge_exterior3
shape = edge_exterior4
shape_weights = 1, 1, 1, 1
fill_shape = edge_circle
plane_slices = 7
bit_radius = 7000
bit_radius_random_variation = 0.250000
min_bits = 3
max_bits = 7
move_bit_percent = 0.500000
equator_bias = 0.500000
color = 170, 170, 170

[NebulaLight]
ambient = 40, 80, 65
sun_burnthrough_intensity = 0.500000
sun_burnthrough_scaler = 1.500000


[;Clouds]
max_distance = 400
puff_count = 30
puff_radius = 100
puff_colora = 60, 60, 60
puff_colorb = 120, 120, 130
puff_shape = edge_cloud1
puff_shape = edge_cloud2
puff_shape = edge_cloud3
puff_shape = edge_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 2.000000
near_fade_distance = 150, 225

[Clouds]
max_distance = 1500
puff_count = 50
puff_radius = 100
puff_colora = 0, 50, 50
puff_colorb = 60, 150, 100
puff_shape = edge_cloud1
puff_shape = edge_cloud2
puff_shape = edge_cloud3
puff_shape = edge_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 2.000000
near_fade_distance = 250, 400
lightning_intensity = 1.000000
lightning_color = 255, 55, 55
lightning_gap = 20.000000
lightning_duration = 0.000000

[Clouds]
max_distance = 1500
puff_count = 70
puff_radius = 100
puff_colora = 10, 25, 25
puff_colorb = 30, 75, 50
puff_shape = generic_cloud1
puff_shape = generic_cloud2
puff_shape = generic_cloud3
puff_shape = generic_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 2.000000
near_fade_distance = 600, 700
puff_max_alpha = 0.50000

[BackgroundLightning]
duration = 0.750000
gap = 5.000000
color = 20, 20, 20

'''


class OchWalkerNebulaTemplate(SimpleTemplate):
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
