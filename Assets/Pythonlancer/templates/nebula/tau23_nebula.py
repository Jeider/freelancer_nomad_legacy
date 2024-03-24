from templates.simple_template import SimpleTemplate


class Tau23MainNebulaTemplate(SimpleTemplate):
	TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\white_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 1800
color = 50, 70, 100

[properties]
flag = nebula

[Exclusion Zones]
{exclusions}

[Exterior]
shape = white_exterior1
shape = white_exterior2
shape = white_exterior3
shape = white_exterior4
shape_weights = 1, 1, 1, 1
fill_shape = white_circle
plane_slices = 3
bit_radius = 7000
bit_radius_random_variation = 0.200000
min_bits = 8
max_bits = 20
move_bit_percent = 0.750000
equator_bias = 0.500000
color = 190, 160, 210

[NebulaLight]
ambient = 90, 95, 130
sun_burnthrough_intensity = 0.75
sun_burnthrough_scaler = 1.5

[Clouds]
max_distance = 1500
puff_count = 100
puff_radius = 100
puff_colora = 255, 255, 255
puff_colorb = 140, 220, 255
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