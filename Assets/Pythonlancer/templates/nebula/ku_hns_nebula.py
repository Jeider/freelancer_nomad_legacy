from templates.simple_template import SimpleTemplate


class HonshuLargeBlueNebulaTemplate(SimpleTemplate):
    TEMPLATE = '''
[TexturePanels]
file = solar\\nebula\\generic_shapes.ini

[properties]
flag = nebula

[Fog]
fog_enabled = 1
near = 0
distance = 1000
color = 15, 15, 30

[Exclusion Zones]
{exclusions}

[Exterior]
shape = generic_exterior1
shape = generic_exterior2
shape = generic_exterior3
shape = generic_exterior4
shape_weights = 1, 1, 1, 1
fill_shape = nebula_circle2
plane_slices = 5
bit_radius = 8000
bit_radius_random_variation = 0.200000
min_bits = 8
max_bits = 12
move_bit_percent = 0.0
equator_bias = 0.3
color = 60, 60, 90

[NebulaLight]
ambient = 15, 10, 45
sun_burnthrough_intensity = 0.500000
sun_burnthrough_scaler = 1.750000

[Clouds]
max_distance = 1500
puff_count = 100
puff_radius = 100
puff_colora = 60, 60, 90
puff_colorb = 90, 60, 120
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
lightning_gap = 5.000000
lightning_duration = 0.500000

[BackgroundLightning]
duration = 0.750000
gap = 3.000000
color = 35, 15, 65

[DynamicLightning]
gap = 1
duration = 0.400000
color = 180, 200, 220
ambient_intensity = 1
intensity_increase = 1

'''