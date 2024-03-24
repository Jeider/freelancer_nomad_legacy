from templates.simple_template import SimpleTemplate


class Om7MainNebulaTemplate(SimpleTemplate):
	TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\walker_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 1500
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
bit_radius = 5000
bit_radius_random_variation = 0.500000
min_bits = 20
max_bits = 30
move_bit_percent = 0.500000
equator_bias = 0.500000
color = 200, 140, 50

[NebulaLight]
ambient = 60, 40, 20
sun_burnthrough_intensity = 1
sun_burnthrough_scaler = 1

[Clouds]
max_distance = 1500
puff_count = 100
puff_radius = 100
puff_colora = 255, 200, 0
puff_colorb = 80, 40, 0
puff_max_alpha = 0.5
puff_shape = walker_cloud1
puff_shape = walker_cloud2
puff_shape = walker_cloud3
puff_shape = walker_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 3.000000
near_fade_distance = 125, 200
lightning_intensity = 1.000000
lightning_color = 65, 25, 85
lightning_gap = 20.000000
lightning_duration = 0.500000

[BackgroundLightning]
duration = 0.550000
gap = 2.000000
color = 60, 40, 10

[DynamicLightning]
gap = 2
duration = 0.550000
color = 255, 150, 0
ambient_intensity = 1
intensity_increase = 1

'''
