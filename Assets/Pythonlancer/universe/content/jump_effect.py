class JumpEffect(object):
    JUMP_EFFECT = None
    GATE_TUNNEL = None


class Edge(JumpEffect):
    JUMP_EFFECT = 'jump_effect_edge'
    GATE_TUNNEL = 'gate_tunnel_edge'


class Crow(JumpEffect):
    JUMP_EFFECT = 'jump_effect_crow'
    GATE_TUNNEL = 'gate_tunnel_crow'


class Walker(JumpEffect):
    JUMP_EFFECT = 'jump_effect_walker'
    GATE_TUNNEL = 'gate_tunnel_walker'


class Barrier(JumpEffect):
    JUMP_EFFECT = 'jump_effect_barrier'
    GATE_TUNNEL = 'gate_tunnel_barrier'


class Dark(JumpEffect):
    JUMP_EFFECT = 'jump_effect_dark'
    GATE_TUNNEL = 'gate_tunnel_dark'


class Rheinland(JumpEffect):
    JUMP_EFFECT = 'jump_effect_edge'
    GATE_TUNNEL = 'gate_tunnel_edge'


class Kusari(JumpEffect):
    JUMP_EFFECT = 'jump_effect_walker'
    GATE_TUNNEL = 'gate_tunnel_walker'


class Liberty(JumpEffect):
    JUMP_EFFECT = 'jump_effect_crow'
    GATE_TUNNEL = 'gate_tunnel_crow'


class Bretonia(JumpEffect):
    JUMP_EFFECT = 'jump_effect_barrier'
    GATE_TUNNEL = 'gate_tunnel_barrier'
