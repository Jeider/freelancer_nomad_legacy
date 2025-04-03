from templates.simple_template import SimpleTemplate


class SiriusInvisibleNebula(SimpleTemplate):
    TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\generic_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 2500
color = 45, 64, 79

[Exclusion Zones]
{exclusions}

[properties]
flag = nebula

[Exterior]
shape = generic_exterior1
shape_weights = 1
plane_slices = 0
bit_radius = 0
bit_radius_random_variation = 0.000000
min_bits = 1
max_bits = 2
move_bit_percent = 0
equator_bias = 0
color = 100, 125, 100

[NebulaLight]
ambient = 20, 26, 31
sun_burnthrough_intensity = 0.300000
sun_burnthrough_scaler = 1

[Clouds]
max_distance = 1500
puff_count = 100
puff_radius = 100
puff_colora = 31, 143, 44
puff_colorb = 59, 219, 137
puff_max_alpha = 0.8500000
puff_shape = generic_cloud1
puff_shape = generic_cloud2
puff_shape = generic_cloud3
puff_shape = generic_cloud4
puff_weights = 1, 1, 1, 1
puff_drift = 1.000000
near_fade_distance = 125, 200
lightning_intensity = 1.000000
lightning_color = 255, 160, 21
lightning_gap = 5.000000
lightning_duration = 1.000000

[BackgroundLightning]
duration = 0.0
gap = 0.000000
color = 0, 0, 0
'''
