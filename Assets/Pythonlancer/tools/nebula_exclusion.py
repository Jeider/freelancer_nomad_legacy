"""Shared Pythonlancer policy for visible, partially transparent exclusion shells.

The client's global volumetric.ini supplies continuous rendering, a 6000 m
march cap, 0.2 transition fraction, 0.15 interior density and a faint analytical
core haze (0.04 opacity per core radius). System-authored
volumetric=false remains authoritative. Shell geometry/tint are preserved.
"""
import re

SHELL_MAX_ALPHA = 0.8


def prepare_exclusion_shells(text):
    """Cap opaque shells; retain authored lower alpha and meshless exclusions."""
    def section(match):
        header, body = match[1], match[2]
        if not re.search(r'(?im)^\s*zone_shell\s*=\s*[^;\s]', body):
            return match[0]
        def alpha(value):
            number = float(value[2])
            return value[0] if number <= SHELL_MAX_ALPHA else value[1]+str(SHELL_MAX_ALPHA)
        body, count = re.subn(r'(?im)^(\s*max_alpha\s*=\s*)([+\-]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[+\-]?\d+)?)', alpha, body)
        if not count:
            newline = '\r\n' if '\r\n' in match[0] else '\n'
            body = 'max_alpha = '+str(SHELL_MAX_ALPHA)+newline+body
        return header+body
    return re.sub(r'(?ims)(^\[Exclusion Zones\][^\r\n]*\r?\n)(.*?)(?=^\[|\Z)', section, text)
