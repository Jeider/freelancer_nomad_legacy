from templates.simple_template import SimpleTemplate


class BerlinBlueNebulaTemplate(SimpleTemplate):
    TEMPLATE = '''[TexturePanels]
file = solar\\nebula\\crow_shapes.ini

[Fog]
fog_enabled = 1
near = 0
distance = 2500
color = 40, 90, 150

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
plane_slices = 7
bit_radius = 6000
bit_radius_random_variation = 0.200000
min_bits = 5
max_bits = 7
move_bit_percent = 0.50000
equator_bias = 0.1
;color = 50, 80, 160 ;TEST
;color = 40, 160, 180 ;LI ORIGINAL
color = 70, 120, 160

[NebulaLight]
ambient = 20, 40, 50
sun_burnthrough_intensity = 0.500000
sun_burnthrough_scaler = 2

[;Clouds]
max_distance = 1500
puff_count = 200
puff_radius = 200
puff_colora = 50, 150, 255
puff_colorb = 255, 255, 255
puff_max_alpha = 0.500000
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

[;Clouds]
max_distance = 1500
puff_count = 500
puff_radius = 100
puff_colora = 50, 150, 255
puff_colorb = 255, 255, 255
puff_max_alpha = 0.3
puff_shape = crow_cloud1
puff_shape = crow_cloud2
puff_shape = crow_cloud3
puff_shape = crow_cloud4
puff_weights = 1, 1, 1, 1
zwrite_clouds = 1000
puff_drift = 3.000000
puff_cloud_size = 1
near_fade_distance = 200, 300

[Clouds]
max_distance = 1500
puff_count = 150
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
gap = 5.000000
color = 60, 100, 85
'''
