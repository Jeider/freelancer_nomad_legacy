from templates.simple_template import SimpleTemplate


class Tau31MainNebulaTemplate(SimpleTemplate):
	TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\edge_shapes.ini
file = solar\\nebula\\generic_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 1400
color = 30, 55, 40

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
plane_slices = 3
bit_radius = 8000
bit_radius_random_variation = 0.200000
min_bits = 5
max_bits = 12
move_bit_percent = 0.250000
equator_bias = 0.500000
color = 170, 150, 170

[NebulaLight]
ambient = 20, 40, 30

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
puff_colora = 0, 50, 50
puff_colorb = 60, 150, 100
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