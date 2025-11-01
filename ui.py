import bpy
import bmesh

def count_faces(obj):
    bm = bmesh.from_edit_mesh(obj.data)
    tris = sum(1 for f in bm.faces if len(f.verts) == 3)
    ngons = sum(1 for f in bm.faces if len(f.verts) >= 5)
    return tris, ngons

class OFD_PT_panel(bpy.types.Panel):
    bl_label = "Odd Faces Detector"
    bl_idname = "OFD_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Odd Faces Detector'

    def draw(self, context):
        layout = self.layout
        obj = context.object

        if obj and obj.type == 'MESH' and context.mode == 'EDIT_MESH':
            tris, ngons = count_faces(obj)
            layout.label(text=f"Tris: {tris}")
            layout.label(text=f"N-Gons: {ngons}")
            layout.operator("ofd.select_tris", text="Select Tris")
            layout.operator("ofd.select_ngons", text="Select N-Gons")
        else:
            layout.label(text="Enter Edit Mode on a Mesh")