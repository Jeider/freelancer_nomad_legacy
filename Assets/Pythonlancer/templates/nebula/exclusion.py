CROW_EXCLUSION = 'solar\\nebula\\crow_exclusion.3db'
BARRIER_EXCLUSION = 'solar\\nebula_mod\\exclusion_barrier_m7.3db'
BARRIER_EXCLUSION_SMALL = 'solar\\nebula_mod\\exclusion_barrier_m7_small.3db'
WALKER_EXCLUSION = 'solar\\nebula_mod\\exclusion_walker_new.3db'
RHEINLAND_EXCLUSION = 'solar\\nebula_mod\\exclusion_rheinland.3db'
EDGE_EXCLUSION = 'solar\\nebula_mod\\exclusion_edge_new.3db'
GENERIC_EXCLUSION = 'solar\\nebula\\generic_exclusion.3db'
VORTEX_EXCLUSIONS_SIMPLE = 'solar\\nebula_mod\\exclusion_vortex.3db'
VORTEX_EXCLUSION = 'solar\\nebula_mod\\exclusion_vortex_new.3db'
ICE_EXCLUSION = 'solar\\nebula_mod\\exclusion_ice.3db'
LINES_EXCLUSION_SIMPLE = 'solar\\nebula_mod\\exclusion_lines.3db'
LINES_EXCLUSION = 'solar\\nebula_mod\\exclusion_lines_new.3db'


# Texture averages measured from the installed exclusion .3db texture libraries.
# These are texture colours, not the final tint. The shell multiplies the two.
SHELL_TEXTURE_RGB = {
    'solar\\nebula\\crow_exclusion.3db': (36.96, 64.47, 158.14),
    'solar\\nebula_mod\\exclusion_barrier_m7.3db': (133.58, 133.58, 133.58),
    'solar\\nebula_mod\\exclusion_barrier_m7_small.3db': (133.58, 133.58, 133.58),
    'solar\\nebula_mod\\exclusion_walker_new.3db': (134.74, 76.69, 27.45),
    'solar\\nebula_mod\\exclusion_rheinland.3db': (46.02, 102.51, 83.47),
    'solar\\nebula_mod\\exclusion_edge_new.3db': (54.44, 110.66, 91.23),
    'solar\\nebula\\generic_exclusion.3db': (156.10, 165.68, 169.68),
    'solar\\nebula_mod\\exclusion_vortex.3db': (64.98, 69.31, 86.77),
    'solar\\nebula_mod\\exclusion_vortex_new.3db': (67.76, 75.30, 96.17),
    'solar\\nebula_mod\\exclusion_ice.3db': (145.22, 159.34, 206.64),
    'solar\\nebula_mod\\exclusion_lines.3db': (45.73, 45.07, 65.47),
    'solar\\nebula_mod\\exclusion_lines_new.3db': (52.46, 53.28, 73.16),
}


# Filled from the actual TexturePanels atlas regions by exclusion_cloud_audit.py.
CLOUD_TEXTURE_SAMPLES = {'solar\\nebula\\generic_shapes.ini': {'generic_cloud1': [[165.40606098562677, 165.5773473010765, 165.40606098562677], 0.24594250473321652], 'generic_cloud2': [[165.43341249543295, 165.5873447204969, 165.43341249543295], 0.23799689797794119], 'generic_cloud3': [[165.50116185281917, 165.6339575491627, 165.50116185281917], 0.254331252154182], 'generic_cloud4': [[166.42067253096408, 166.5892995204613, 166.42067253096408], 0.24433697345210056]}, 'solar\\nebula\\edge_shapes.ini': {'edge_cloud1': [[86.55314459961686, 141.52520670440884, 122.49703213458211], 0.17759023554184858], 'edge_cloud2': [[89.15723678333423, 144.42650658376658, 130.2012077683086], 0.1848961400050743], 'edge_cloud3': [[62.47701623513421, 131.73255857126944, 113.40694057233812], 0.20574531555175782], 'edge_cloud4': [[66.37858304501529, 133.1508316745889, 118.67457945333643], 0.1939289840997434]}, 'solar\\nebula\\crow_shapes.ini': {'crow_cloud1': [[99.53891745628226, 143.74386242392728, 197.43572697596488], 0.23450290081547756], 'crow_cloud2': [[104.41653873597267, 147.24847624333017, 199.27908351171556], 0.22768405091528798], 'crow_cloud3': [[111.01180296249561, 151.92970520181987, 201.68108251398303], 0.23914176342534085], 'crow_cloud4': [[104.40979295355216, 147.2098632863037, 199.25593006242914], 0.23280284731995826]}, 'solar\\nebula\\walker_shapes.ini': {'walker_cloud1': [[162.90322392825766, 131.6236710369179, 84.7753588216495], 0.22613770354027843], 'walker_cloud2': [[161.91538365025554, 130.42653402542706, 83.27297432587474], 0.21705834631826362], 'walker_cloud3': [[161.88664775549114, 130.63114564830116, 83.82113330314769], 0.23399699716007008], 'walker_cloud4': [[161.84539160092825, 130.34673042375167, 83.17491925917204], 0.2234826405843099]}, 'solar\\nebula\\white_shapes.ini': {'generic_cloud1': [[165.40606098562677, 165.5773473010765, 165.40606098562677], 0.24594250473321652], 'generic_cloud2': [[165.43341249543295, 165.5873447204969, 165.43341249543295], 0.23799689797794119], 'generic_cloud3': [[165.50116185281917, 165.6339575491627, 165.50116185281917], 0.254331252154182], 'generic_cloud4': [[166.42067253096408, 166.5892995204613, 166.42067253096408], 0.24433697345210056]}}


def palette_sections(text):
    """Preserve repeated sections/keys and isolate disabled [;Clouds] blocks."""
    sections, values = [], {}
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith('[') and ']' in line:
            name = line[1:line.index(']')].strip().lower()
            values = {}
            sections.append((name, values))
        else:
            line = line.split(';', 1)[0].strip()
            if '=' in line:
                key, value = line.split('=', 1)
                values.setdefault(key.strip().lower(), []).append(value.strip())
    return sections


def palette_rgb(value):
    values = tuple(float(x.strip()) for x in value.split(','))
    if len(values) != 3 or any(not 0 <= x <= 255 for x in values):
        raise ValueError('Expected RGB in 0..255: ' + value)
    return values


def cloud_palette(sections):
    """Texture RGB * puff colour, weighted by shape probability and layer coverage.

    This is an authored palette estimate, not a simulation of lighting/fog.
    Missing texture measurements retain the hand-authored exclusion tint.
    """
    shapes = {}
    for name, values in sections:
        if name == 'texturepanels':
            for panel in values.get('file', []):
                shapes.update(CLOUD_TEXTURE_SAMPLES.get(panel.lower().replace('/', '\\'), {}))
    total = [0., 0., 0.]
    weight_sum = 0.
    for name, values in sections:
        if name != 'clouds':
            continue
        def last(key, default):
            return values.get(key, [default])[-1]
        count = float(last('puff_count', '0'))
        alpha = float(last('puff_max_alpha', '1'))
        if count <= 0 or alpha <= 0:
            continue
        a = palette_rgb(last('puff_colora', '255, 255, 255'))
        b = palette_rgb(last('puff_colorb', '255, 255, 255'))
        names = values.get('puff_shape', [])
        weights = [float(x) for x in last('puff_weights', ','.join(['1'] * len(names))).split(',') if x]
        if not names or len(weights) != len(names) or not sum(weights):
            return None
        if any(shape not in shapes for shape in names):
            return None
        # Relative projected coverage, including distance, alpha and puff area.
        layer = count * alpha * (float(last('puff_radius', '100')) /
                                 max(1., float(last('max_distance', '1500')))) ** 2
        for shape, weight in zip(names, weights):
            texture, coverage = shapes[shape]
            w = layer * weight / sum(weights) * coverage
            for c in range(3):
                total[c] += w * texture[c] * (a[c] + b[c]) / (2 * 255)
            weight_sum += w
    return tuple(x / weight_sum for x in total) if weight_sum and max(total) else None


def match_exclusion_palette(template, params):
    """Match a shell to its own nebula, without mutating shared system dictionaries.

    Template EXCLUSION_TINT_BY_SHELL can override the automatic tint per model.
    Template MATCH_EXCLUSION_PALETTE = False retains the authored tint verbatim.
    Unknown shells and fog-disabled nebulae retain their authored settings.
    """
    result = dict(params)
    shell = str(params.get('zone_shell', '')).lower().replace('/', '\\')
    if not getattr(template, 'MATCH_EXCLUSION_PALETTE', True):
        return result
    override = getattr(template, 'EXCLUSION_TINT_BY_SHELL', {}).get(shell)
    if override is not None:
        result['exclusion_tint'] = override
        return result
    texture = SHELL_TEXTURE_RGB.get(shell)
    if texture is None:
        return result
    sections = palette_sections(template.TEMPLATE)
    fog = next(({k: v[-1] for k, v in values.items()} for name, values in sections if name == 'fog'), {})
    if fog.get('fog_enabled', '1') == '0' or 'color' not in fog:
        return result

    def unit(colour):
        peak = max(colour)
        return tuple(x / peak for x in colour) if peak else (0., 0., 0.)

    base = palette_rgb(fog['color'])
    if not max(base):
        return result
    cloud = cloud_palette(sections)
    if cloud is None:
        return result
    # Visible cloud texture/tint dominates; fog only gently ties the wall to its surroundings.
    target = tuple(.15 * x + .85 * y for x, y in zip(unit(base), unit(cloud)))
    old = palette_rgb(str(params.get('exclusion_tint', '255, 255, 255')))
    authored = unit(tuple(t * c for t, c in zip(texture, old)))
    # Avoid replacing a hand-tuned colour already close to the cloud palette (about 10 degrees).
    cosine = sum(x * y for x, y in zip(authored, target)) / max(1e-10,
        (sum(x*x for x in authored) * sum(x*x for x in target)) ** .5)
    if cosine >= .985:
        return result
    weights = (.2126, .7152, .0722)
    brightness = sum(w * t * c / 255 for w, t, c in zip(weights, texture, old))
    gain = brightness / sum(w * c for w, c in zip(weights, target))
    corrected = [255 * gain * c / t for c, t in zip(target, texture)]
    # A tint cannot amplify a texture channel. Scale all channels together to keep hue.
    scale = min(1., 255 / max(corrected)) if max(corrected) else 1.
    corrected = [x * scale for x in corrected]
    new_brightness = sum(w * t * c / 255 for w, t, c in zip(weights, texture, corrected))
    # Saturated assets (especially blue Crow in Columbia) cannot reproduce every
    # hue by multiplication. Prefer a partial match over an almost black wall.
    if new_brightness < brightness * .75:
        blend = (brightness * .75 - new_brightness) / (brightness - new_brightness)
        corrected = [x * (1 - blend) + y * blend for x, y in zip(corrected, old)]
    result['exclusion_tint'] = ', '.join(str(round(x)) for x in corrected)
    return result
