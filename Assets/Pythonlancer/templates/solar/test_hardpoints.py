import random

XML_MAIN_TEMPLATE = '''<?xml version="1.0" encoding="ISO-8859-1"?>
<!-- XML generated by UTFXML Version 2.2 built 19-Aug-2010 -->
<UTFXML filename="hardpoints.3db">
   <UTF_ROOT>
      
      
   
     <Hardpoints>
        <Fixed>
           {hardpoints}
        </Fixed>
     </Hardpoints>
      
     
   </UTF_ROOT>
</UTFXML>
'''

HARDPOINT_TEMPLATE = '''
       <{hp_name}>
          <Orientation type="Matrix">
               {matrix_x1}, {matrix_x2}, {matrix_x3},
               {matrix_y1}, {matrix_y2}, {matrix_y3},
               {matrix_z1}, {matrix_z2}, {matrix_z3}
          </Orientation>
          <Position type="Vector">{pos_x}, {pos_y}, {pos_z}</Position>
       </{hp_name}>
'''

EQUIP_TEMPLATE = 'equip = {equip}, {hp_name}'


MATRIX_INIT = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
)
MATRIX_ROT_Y90 = (
    (0, 0, 1),
    (0, 1, 0),
    (-1, 0, 0),
)
MATRIX_ROT_Y90_reverse = (
    (0, 0, -1),
    (0, 1, 0),
    (1, 0, 0),
)
MATRIX_ROT_Y180 = (
    (-1, 0, 0),
    (0, 1, 0),
    (0, 0, -1),
)
MATRIX_ROT_X90 = (
    (1, 0, 0),
    (0, 0, -1),
    (0, 1, 0),
)
MATRIX_ROT_X90_reverse = (
    (1, 0, 0),
    (0, 0, 1),
    (0, -1, 0),
)
MATRIX_ROT_Z90 = (
    (0, -1, 0),
    (1, 0, 0),
    (0, 0, 1),
)
MATRIX_ROT_Z90_reverse = (
    (0, 1, 0),
    (-1, 0, 0),
    (0, 0, 1),
)

hardpoints = {
    'HpMiner01': (0, 150, 0),
    'HpTunnel01': (0, 15, 132),
    'HpTunnel02': (0, 15, -132),
    'HpPanel01': (0, 45, -125),
    'HpPanel02': (0, 45, 125),
    'HpControl01': (0, 280, 0),
    'HpInd01': (0, -75, 0),
    'HpInd02': (75, -25, 0.1),
    'HpInd03': (-75, -25, -0.1),
    'HpInd04': (-50, 50, 0.1),
    'HpInd05': (50, 50, -0.1),
    'HpRing01': (0, 0, 41),
    'HpRing02': (0, 0, -41),
    'HpTank01': (45, -95, 0),
    'HpTank02': (-45, -95, 0),
    'HpTank03': (110, -40, 0),
    'HpTank04': (-110, -40, 0),
}

hps_xml = []
loadout = []

for hp_name, hp_pos in hardpoints.items():
    rot_matrix = MATRIX_INIT

    pos_x, pos_y, pos_z = hp_pos

    matrix_x1, matrix_x2, matrix_x3 = rot_matrix[0]
    matrix_y1, matrix_y2, matrix_y3 = rot_matrix[1]
    matrix_z1, matrix_z2, matrix_z3 = rot_matrix[2]

    hps_xml.append(HARDPOINT_TEMPLATE.format(
        hp_name=hp_name,
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
    loadout.append(
        EQUIP_TEMPLATE.format(equip='any', hp_name=hp_name)
    )
    
    


# xml_file = XML_MAIN_TEMPLATE.format(
    # hardpoints="\n".join(hps_xml),
# )

# print(xml_file)

print("\n".join(loadout))