import random

from templates.solar.base_solar import MineableSolar


XML_MAIN_TEMPLATE = '''<?xml version="1.0" encoding="ISO-8859-1"?>
<!-- XML generated by UTFXML Version 2.2 built 19-Aug-2010 -->
<UTFXML filename="{out_file}">
   <UTF_ROOT>
      <Cmpnd>
         <Cons>
            <Fix type="Fix" count="{fix_count}">
                {fix_content}
            </Fix>
         </Cons>

         {parts_obj_content}

         <Root>
            <Object_name name="Object name" type="text">Root</Object_name>
            <File_name name="File name" type="text">debris_box_root_lod14210921702.3db</File_name>
            <Index type="int">0</Index>
         </Root>
      </Cmpnd>
      
      
      {obj_content}
      
      <debris_box_root_lod14210921702.3db>
 
       <VMeshPart>
          <VMeshRef type="VMeshRef">
             <!-- header size  --> 60,
             <!-- vmesh lib    --> fl.debris_box_cmp.lod0-112.vms,
             <!-- start vert   --> 0,
             <!-- num verts    --> 20,
             <!-- start index  --> 0,
             <!-- num indices  --> 36,
             <!-- start mesh   --> 0,
             <!-- num meshes   --> 1,
             <!-- bounding box -->  0.29166669,  0.33333382,  0.19383606,
                                   -0.29166669, -0.24999952, -0.38949728,
             <!-- center       -->  0,           0,           0,
             <!-- radius       --> 0.29166669
          </VMeshRef>
       </VMeshPart>
       
         <Hardpoints>
            <Fixed>
               <HpRoot>
                  <Orientation type="Matrix">
                       1.0000000000,   0.0000000000,   0.0000000000,
                       0.0000000000,   1.0000000000,   0.0000000000,
                       0.0000000000,   0.0000000000,   1.0000000000
                  </Orientation>
                  <Position type="Vector">0, 0, 0</Position>
               </HpRoot>
               {extra_hardpoints}
               <HpShield01>
                  <Orientation type="Matrix">
                       1.0000000000,   0.0000000000,   0.0000000000,
                       0.0000000000,   1.0000000000,   0.0000000000,
                       0.0000000000,   0.0000000000,   1.0000000000
                  </Orientation>
                  <Position type="Vector">0, 0, 0</Position>
               </HpShield01>
            </Fixed>
         </Hardpoints>
      </debris_box_root_lod14210921702.3db>
      
     
   </UTF_ROOT>
</UTFXML>
'''

VMESH_LIB = '''
      <VMeshLibrary>
         <jeider_s_debris_box1.lod0-112.vms include="debris_box_modern_3db\\lod0-112.vms.xml"/>
      </VMeshLibrary>
'''
VMESH_PART = '''
      <VMeshPart>
         <VMeshRef type="VMeshRef">
            <!-- header size  --> 60,
            <!-- vmesh lib    --> jeider_s_debris_box1.lod0-112.vms,
            <!-- start vert   --> 0,
            <!-- num verts    --> 291,
            <!-- start index  --> 0,
            <!-- num indices  --> 816,
            <!-- start mesh   --> 0,
            <!-- num meshes   --> 1,
            <!-- bounding box -->  2.3986983,  2.44,         2.4808981,
                                  -2.3986983, -2.36,        -2.4,
            <!-- center       -->  0,          0.039999962,  0.040449023,
            <!-- radius       --> 4.1796584
         </VMeshRef>
      </VMeshPart>
'''

PART_TEMPLATE = '''
<part>
  <!-- parent      --> "Root",
  <!-- child       --> "box{index:02d}_lod1",
  <!-- position    --> {pos_x}, {pos_y}, {pos_z}
  <!-- orientation -->  {matrix_x1}, {matrix_x2}, {matrix_x3},
                        {matrix_y1}, {matrix_y2}, {matrix_y3},
                        {matrix_z1}, {matrix_z2}, {matrix_z3} 
</part>
'''

PART_OBJ_TEMPLATE = '''
         <Part_box{index:02d}_lod1>
            <Object_name name="Object name" type="text">box{index:02d}_lod1</Object_name>
            <File_name name="File name" type="text">debris_box_x{count}_el_{index:02d}.3db</File_name>
            <Index type="int">{index}</Index>
         </Part_box{index:02d}_lod1>
'''

OBJ_TEMPLATE = '''
      <debris_box_x{objs}_el_{index:02d}.3db>
        {vmesh_part}
      </debris_box_x{objs}_el_{index:02d}.3db>
'''

HARDPOINT_TEMPLATE = '''
       <HpFX{index:02d}>
          <Orientation type="Matrix">
               1.0000000000,   0.0000000000,   0.0000000000,
               0.0000000000,   1.0000000000,   0.0000000000,
               0.0000000000,   0.0000000000,   1.0000000000
          </Orientation>
          <Position type="Vector">{pos_x}, {pos_y}, {pos_z}</Position>
       </HpFX{index:02d}>
'''

SUR_MAIN_TEMPLATE = '''
# Wavefront OBJ exported by MilkShape 3D

mtllib debris_box_2024.mtl

v -2.413580 2.334524 2.416590
v -2.413580 -2.369179 2.416590
v 2.413580 2.334524 2.416590
v 2.413580 -2.369179 2.416590
v 2.413580 2.334524 -2.410570
v 2.413580 -2.369179 -2.410570
v -2.413580 2.334524 -2.410570
v -2.413580 -2.369179 -2.410570
v -0.046667 -14.934118 0.062516
v -0.046667 -15.027452 0.062516
v 0.046667 -14.934118 0.062516
v 0.046667 -15.027452 0.062516
v 0.046667 -14.934118 -0.030817
v 0.046667 -15.027452 -0.030817
v -0.046667 -14.934118 -0.030817
v -0.046667 -15.027452 -0.030817
# 16 vertices

vt 0.000000 1.000000
vt 0.000000 0.000000
vt 1.000000 1.000000
vt 1.000000 0.000000
# 4 texture coordinates

vn 0.000000 0.000000 1.000000
vn 1.000000 0.000000 0.000000
vn 0.000000 0.000000 -1.000000
vn -1.000000 0.000000 0.000000
vn 0.000000 1.000000 0.000000
vn 0.000000 -1.000000 0.000000
# 6 normals

g derbris_root
usemtl debris_no_alpha
s 1
f 9/1/1 10/2/1 11/3/1
f 10/2/1 12/4/1 11/3/1
s 2
f 11/1/2 12/2/2 13/3/2
f 12/2/2 14/4/2 13/3/2
s 1
f 13/1/3 14/2/3 15/3/3
f 14/2/3 16/4/3 15/3/3
s 2
f 15/1/4 16/2/4 9/3/4
f 16/2/4 10/4/4 9/3/4
s 3
f 15/1/5 9/2/5 13/3/5
f 9/2/5 11/4/5 13/3/5
f 10/1/6 16/2/6 12/3/6
f 16/2/6 14/4/6 12/3/6
# 12 triangles in group

{sur_parts}
'''

SUR_PART_TEMPLATE = '''
g box{index:02d}_lod1
usemtl debris_no_alpha
s 1
f 1/1/1 2/2/1 3/3/1
f 2/2/1 4/4/1 3/3/1
s 2
f 3/1/2 4/2/2 5/3/2
f 4/2/2 6/4/2 5/3/2
s 1
f 5/1/3 6/2/3 7/3/3
f 6/2/3 8/4/3 7/3/3
s 2
f 7/1/4 8/2/4 1/3/4
f 8/2/4 2/4/4 1/3/4
s 3
f 7/1/5 1/2/5 5/3/5
f 1/2/5 3/4/5 5/3/5
f 2/1/6 8/2/6 4/3/6
f 8/2/6 6/4/6 4/3/6
# 12 triangles in group
'''

FUSE_TEMPLATE = '''[fuse]
name = {fuse_main_name}{index:02d}
lifetime = 0.100000
death_fuse = true

[start_effect]
effect = dast_debris_explosion
hardpoint = HpFX{index:02d}
at_t = 0.000000

[destroy_group]
at_t = 0.000000
group_name = box{index:02d}_lod1
fate = disappear
'''

FUSE_DROP_TEMPLATE = '''[fuse]
name = {fuse_drop_name}{index:02d}
lifetime = 0.100000
death_fuse = true

[start_effect]
effect = dast_debris_explosion
hardpoint = HpFX{index:02d}
at_t = 0.000000

[dump_cargo]
at_t = 0.99
origin_hardpoint = HpDrop

[destroy_group]
at_t = 0.000000
group_name = box{index:02d}_lod1
fate = disappear
'''

COLLISION_TEMPLATE = '''[CollisionGroup]
obj = box{index:02d}_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
;;separation_explosion = dast_debris_explosion
fuse = {fuse_name}{index:02d}, 0.000000, 1
explosion_resistance = 0.0001
hit_pts = 1000
root_health_proxy = false
'''

MATRIX_ROT_1 = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
)
MATRIX_ROT_2 = (
    (0, 0, 1),
    (0, 1, 0),
    (-1, 0, 0),
)
MATRIX_ROT_3 = (
    (0, 0, -1),
    (0, 1, 0),
    (1, 0, 0),
)
MATRIX_ROT_4 = (
    (-1, 0, 0),
    (0, 1, 0),
    (0, 0, -1),
)
MATRIX_ROT_5 = (
    (1, 0, 0),
    (0, 0, -1),
    (0, 1, 0),
)
MATRIX_ROT_6 = (
    (1, 0, 0),
    (0, 0, 1),
    (0, -1, 0),
)
MATRIX_ROT_7 = (
    (0, -1, 0),
    (1, 0, 0),
    (0, 0, 1),
)
MATRIX_ROT_8 = (
    (0, 1, 0),
    (-1, 0, 0),
    (0, 0, 1),
)
MATRICES = [
    MATRIX_ROT_1,
    MATRIX_ROT_2,
    MATRIX_ROT_3,
    MATRIX_ROT_4,
    MATRIX_ROT_5,
    MATRIX_ROT_6,
    MATRIX_ROT_7,
    MATRIX_ROT_8,
]

FUSE_MAIN = 'debris_box_dmg_box'
FUSE_DROP = 'debris_box_dmg_xdrop_box'


class DebrisBoxFactory(object):

    def __init__(self):
        init = 2.35
        step = 5.3

        pos_x = 0
        pos_y = init
        pos_z = 0

        x_index = 1
        z_index = 1
        max_pos_index = 3

        items = 29

        rot_select = 0
        rot_select_max = 7

        file = 'debris_box_x29_cube.cmp'

        out_item = random.randint(1, items-1)

        parts = []
        part_objs = []
        objs = []
        collis = []
        hps = []
        sur_items = []
        fuses = []
        fuses_drop = []
        for i in range(1, items+1):
            rot_matrix = random.choice(MATRICES)
            # rot_matrix = MATRICES[rot_select]
            # rot_select += 1
            # if rot_select > rot_select_max:
                # rot_select = 1

            matrix_x1, matrix_x2, matrix_x3 = rot_matrix[0]
            matrix_y1, matrix_y2, matrix_y3 = rot_matrix[1]
            matrix_z1, matrix_z2, matrix_z3 = rot_matrix[2]

            parts.append(PART_TEMPLATE.format(
                index=i,
                pos_x=pos_x,
                pos_y=pos_y,
                pos_z=pos_z,
                matrix_x1=matrix_x1,
                matrix_x2=matrix_x2,
                matrix_x3=matrix_x3,
                matrix_y1=matrix_y1,
                matrix_y2=matrix_y2,
                matrix_y3=matrix_y3,
                matrix_z1=matrix_z1,
                matrix_z2=matrix_z2,
                matrix_z3=matrix_z3,
            ))
            part_objs.append(PART_OBJ_TEMPLATE.format(count=items,index=i))
            objs.append(OBJ_TEMPLATE.format(objs=items, vmesh_part=VMESH_PART, index=i))
            
            fuse_name = FUSE_DROP if out_item == i else FUSE_MAIN
            collis.append(COLLISION_TEMPLATE.format(fuse_name=fuse_name, index=i))
            
            hps.append(HARDPOINT_TEMPLATE.format(
                index=i,
                pos_x=pos_x,
                pos_y=pos_y,
                pos_z=pos_z,
            ))
            sur_items.append(SUR_PART_TEMPLATE.format(index=i))
            fuses.append(FUSE_TEMPLATE.format(fuse_main_name=FUSE_MAIN, index=i))
            fuses_drop.append(FUSE_DROP_TEMPLATE.format(fuse_drop_name=FUSE_DROP, index=i))

            x_index += 1
            pos_x += step

            if x_index > max_pos_index:
                z_index += 1
                pos_z += step

                x_index = 1
                pos_x = 0

            if z_index > max_pos_index:
                z_index = 1
                pos_z = 0
                pos_y += step


        self.final_xml_file = XML_MAIN_TEMPLATE.format(
            out_file=file,
            fix_count=items,
            fix_content="\n".join(parts),
            parts_obj_content="\n".join(part_objs),
            obj_content="\n".join(objs),
            extra_hardpoints="\n".join(hps),
        )

        self.final_sur_items = "".join(sur_items)
            

        self.final_parts = "\n".join(parts)
        self.final_part_objs = "\n".join(part_objs)
        self.final_objs = "\n".join(objs)
        self.final_collis = "\n".join(collis)

        self.final_fuses = "\n".join(fuses)
        self.final_fuses_drop = "\n".join(fuses_drop)


INIT_ITEMS_TEMPLATE = 'equip = attached_xast_exploder, {hp}'


class DebrisBox(MineableSolar):
    ALIAS = 'debris_box'

    DEFAULT_ARCHETYPE = 'debris_box_x29_cube'
    ARCHETYPE_REWARD_MEDIUM = 'debris_box_x29_cube'
    ARCHETYPE_REWARD_HIGH = 'debris_box_x29_cube'
    ARCHETYPE_REWARD_ULTRA = 'debris_box_x29_cube'
    # ARCHETYPE_REWARD_MEDIUM = 'debris_box_x29_cube_medium'
    # ARCHETYPE_REWARD_HIGH = 'debris_box_x29_cube_high'
    # ARCHETYPE_REWARD_ULTRA = 'debris_box_x29_cube_ultra'

    def get_default_archetype(self):
        return self.DEFAULT_ARCHETYPE

    def get_medium_reward_archetype(self):
        return self.ARCHETYPE_REWARD_MEDIUM

    def get_high_reward_archetype(self):
        return self.ARCHETYPE_REWARD_HIGH

    def get_ultra_reward_archetype(self):
        return self.ARCHETYPE_REWARD_ULTRA