import sys

from tools.crc import crc32_hex_from_str, crc32_int_from_str, crc32_minus_from_str
from tools.create_id import CreateId

try:
    material = sys.argv[1]
except IndexError:
    raise Exception('Enter the material as argument')

mode = ''

try:
    mode = sys.argv[2]
except IndexError:
    pass


if mode == 'int':
    the_id = CreateId.get_int_id(material)
    print(the_id)

else:

    print(crc32_minus_from_str(material))
    print(crc32_int_from_str(material))
    crc = crc32_hex_from_str(material)
    print(crc)
    print(f'0x{crc[2:].upper()}')



