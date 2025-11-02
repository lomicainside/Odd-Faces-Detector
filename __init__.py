bl_info = {
    "name": "Odd Faces Detector",
    "author": "Lomica Inside",
    "version": (0, 56),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Odd Faces Detector",
    "description": "This basic Blender add-on makes modeling significantly easier by detecting and counting tris and n-gons in edit mode, with face selection buttons for each, saving the time wasted by looking for them.",
    "category": "Mesh"
}

import bpy

from . import ui
from . import tris
from . import n_gons

classes = (
    ui.OFD_PT_panel,
    tris.OFD_OT_select_tris,
    n_gons.OFD_OT_select_ngons,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
