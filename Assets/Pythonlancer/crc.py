import sys

from tools.crc import crc32_hex_from_str

try:
    material = sys.argv[1]
except IndexError:
    raise Exception('Enter the material as argument')

crc = crc32_hex_from_str(material)
print(crc)
print(f'0x{crc[2:].upper()}')
