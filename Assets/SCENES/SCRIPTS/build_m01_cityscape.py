import json
from pathlib import Path

import bpy
from mathutils import Quaternion, Vector

DUMP = Path(r"D:\Games\FL_MOD\Assets\SCENES\DUMPS\m01_cityscape.json")
OUT = Path(r"D:\Games\FL_MOD\Assets\SCENES\m01_cityscape.blend")
TRENT = r"E:\FL\room\trent_stand.obj"
CAMERAS = {"cam_bar", "cam_start", "cam_stuard", "cam_trent", "cam_read", "cam_walk", "cam_dbg"}
CHAR_MARKERS = {"trent_init_pos"}
RX_NEG = Quaternion((1.0, 0.0, 0.0), -1.5708)
RX_POS = RX_NEG.inverted()

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.wm.obj_import(filepath=TRENT)
source = bpy.context.selected_objects[0]
mesh = source.data
bpy.data.objects.remove(source, do_unlink=True)

data = json.loads(DUMP.read_text(encoding="utf-8"))
for name, item in data.items():
    if name.startswith("Char_") or name in CHAR_MARKERS:
        obj = bpy.data.objects.new(name, mesh)
    elif name in CAMERAS:
        cam = bpy.data.cameras.new(name)
        obj = bpy.data.objects.new(name, cam)
    else:
        obj = bpy.data.objects.new(name, None)
        obj.empty_display_type = "ARROWS" if name.startswith("Wingman") or name.startswith("Prop_") else "SPHERE"
        obj.empty_display_size = 0.3
    dump_quat = Quaternion(item["orientation"])
    obj.rotation_mode = "QUATERNION"
    obj.rotation_quaternion = RX_POS @ dump_quat
    obj.location = Vector(item["position"])
    bpy.context.scene.collection.objects.link(obj)
    back = RX_NEG @ obj.rotation_quaternion
    if (Vector(back) - Vector(dump_quat)).length > 1e-4:
        raise SystemExit(f"quat roundtrip failed for {name}")

bpy.ops.wm.save_as_mainfile(filepath=str(OUT))
print(f"saved {OUT} objects {len(data)}")
