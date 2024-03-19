from templates.simple_template import SimpleTemplate


class BizmarkBrownNebulaTemplate(SimpleTemplate):
	TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\generic_shapes.ini

[Fog]
fog_enabled = 1
near = 600
distance = 1300
color = 40, 20, 10

[properties]
flag = nebula

[Exclusion Zones]
{exclusions}

[Exterior]
shape = generic_exterior1
shape = generic_exterior2
shape = generic_exterior3
shape = generic_exterior4
shape_weights = 1, 1, 1, 1
fill_shape = nebula_circle2
plane_slices = 3
bit_radius = 8000
bit_radius_random_variation = 0.200000
min_bits = 3
max_bits = 8
move_bit_percent = 0.500000
equator_bias = 0.500000
color = 70, 52, 30

[NebulaLight]
ambient = 40, 20, 10
sun_burnthrough_intensity = 0.300000
sun_burnthrough_scaler = 1

[Clouds]
max_distance = 1500
puff_count = 100
puff_radius = 100
puff_colora = 100, 72, 40
puff_colorb = 150, 120, 60
puff_max_alpha = 0.500000
puff_shape = generic_cloud1
puff_shape = generic_cloud2
puff_shape = generic_cloud3
puff_shape = generic_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 1.000000
near_fade_distance = 125, 200
lightning_intensity = 1.000000
lightning_color = 65, 25, 85
lightning_gap = 20.000000
lightning_duration = 0.500000

[BackgroundLightning]
duration = 0.000000
gap = 4.000000
color = 230, 170, 80
'''
