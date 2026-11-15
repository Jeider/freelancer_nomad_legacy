import json
from pathlib import Path

import bpy
from mathutils import Quaternion, Vector

DUMP = Path(r"D:\Games\FL_MOD\Assets\SCENES\DUMPS\m01_s13_done.json")
OUT = Path(r"D:\Games\FL_MOD\Assets\SCENES\m01_s13_done.blend")
TRENT = r"E:\FL\room\trent_stand.obj"
CAMERAS = {"cam_trent_drinking", "cam_full_scene"}
CHAR_MARKERS = {"char_alaric", "char_trent"}
RX_NEG = Quaternion((1.0, 0.0, 0.0), -1.5708)
RX_POS = RX_NEG.inverted()

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.wm.obj_import(filepath=TRENT)
source = bpy.context.selected_objects[0]
mesh = source.data
bpy.data.objects.remove(source, do_unlink=True)

data = json.loads(DUMP.read_text(encoding="utf-8"))
for name, item in data.items():
    if name in CHAR_MARKERS:
        obj = bpy.data.objects.new(name, mesh)
    elif name in CAMERAS:
        obj = bpy.data.objects.new(name, bpy.data.cameras.new(name))
    else:
        obj = bpy.data.objects.new(name, None)
        obj.empty_display_type = "SPHERE"
        obj.empty_display_size = 0.15
    dump_quat = Quaternion(item["orientation"])
    obj.rotation_mode = "QUATERNION"
    obj.rotation_quaternion = RX_POS @ dump_quat
    obj.location = Vector(item["position"])
    bpy.context.scene.collection.objects.link(obj)

bpy.ops.wm.save_as_mainfile(filepath=str(OUT))
print(f"saved {OUT} objects {len(data)}")
