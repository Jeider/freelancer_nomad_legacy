import os
import json

from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *

base_name = os.path.splitext(os.path.basename(bpy.data.filepath))[0] + '.json'
result_filename = os.getcwd() + "\\DUMPS\\" + base_name


results = {}

for key, value in C.scene.objects.items():
    value.rotation_mode = 'QUATERNION'
    orient = value.rotation_quaternion
    results[str(key)] = {
        'position': [value.location[0], value.location[1], value.location[2]],
        'orientation': [orient[0], orient[1], orient[2], orient[3]],
    }

print(result_filename)
print(results)


with open(result_filename, 'w') as dump_file:
    json.dump(results, dump_file)



# COMMAND:
# import os; filename = os.getcwd() + '\\SCRIPTS\\dumper.py'; exec(compile(open(filename).read(), filename, 'exec'))