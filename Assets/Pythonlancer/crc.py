import sys

from tools.crc import crc32_hex_from_str, crc32_int_from_str, crc32_minus_from_str

try:
    material = sys.argv[1]
except IndexError:
    raise Exception('Enter the material as argument')

print(crc32_minus_from_str(material))
print(crc32_int_from_str(material))
crc = crc32_hex_from_str(material)
print(crc)
print(f'0x{crc[2:].upper()}')
