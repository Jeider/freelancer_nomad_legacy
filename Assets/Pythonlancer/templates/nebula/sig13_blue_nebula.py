from templates.simple_template import SimpleTemplate


class Sig13BlueNebulaTemplate(SimpleTemplate):
	TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\crow_shapes.ini

[Fog]
fog_enabled = 1
near = 150
distance = 2000
color = 0, 50, 80

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
plane_slices = 3
bit_radius = 25000
bit_radius_random_variation = 0.200000
min_bits = 5
max_bits = 8
move_bit_percent = 0.750000
equator_bias = 0.500000
color = 30, 80, 130

[NebulaLight]
ambient = 20, 40, 50
sun_burnthrough_intensity = 0.500000
sun_burnthrough_scaler = 2


[Clouds]
max_distance = 300
puff_count = 20
puff_radius = 100
puff_colora = 50, 150, 255
puff_colorb = 255, 255, 255
puff_max_alpha = 0.500000
puff_shape = crow_cloud1
puff_shape = crow_cloud2
puff_shape = crow_cloud3
puff_shape = crow_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 1.000000
near_fade_distance = 125, 200
lightning_intensity = 1.000000
lightning_color = 25, 75, 85
lightning_gap = 20.000000
lightning_duration = 0.500000

[BackgroundLightning]
duration = 0.750000
gap = 3.000000
color = 50, 50, 50

'''
