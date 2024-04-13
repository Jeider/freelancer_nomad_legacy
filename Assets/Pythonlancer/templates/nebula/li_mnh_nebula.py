from templates.simple_template import SimpleTemplate


class ManhattanNebulaTemplate(SimpleTemplate):
	TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\crow_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 2500
color = 30, 70, 100

[properties]
flag = nebula

[Exclusion Zones]
{exclusions}

[Exterior]
shape = crow_exterior1
shape = crow_exterior2
shape = crow_exterior3
shape = crow_exterior4
shape_weights = 1, 1, 1, 1
fill_shape = crow_circle
plane_slices = 5
bit_radius = 8000
bit_radius_random_variation = 0.400000
min_bits = 8
max_bits = 14
move_bit_percent = 0.5
equator_bias = 0.5
color = 60, 120, 120

[NebulaLight]
ambient = 50, 80, 100
sun_burnthrough_intensity = 0.500000
sun_burnthrough_scaler = 2

[Clouds]
max_distance = 1500
puff_count = 100
puff_radius = 100
puff_colora = 80, 200, 200
puff_colorb = 255, 255, 200
puff_max_alpha = 0.900000
puff_shape = crow_cloud1
puff_shape = crow_cloud2
puff_shape = crow_cloud3
puff_shape = crow_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 1.000000
puff_cloud_size = 1
near_fade_distance = 125, 200
lightning_intensity = 1.000000
lightning_color = 25, 75, 85
lightning_gap = 20.000000
lightning_duration = 0.500000

[BackgroundLightning]
duration = 0.750000
gap = 5.000000
color = 60, 100, 85
'''