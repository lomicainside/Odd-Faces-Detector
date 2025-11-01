import bpy
import bmesh

class OFD_OT_select_tris(bpy.types.Operator):
    bl_idname = "ofd.select_tris"
    bl_label = "Select Tris"
    bl_description = "Select all tris (3-vertex faces)"

    def execute(self, context):
        obj = context.object
        bm = bmesh.from_edit_mesh(obj.data)

        bpy.ops.mesh.select_mode(type="FACE")
        bpy.ops.mesh.select_all(action='DESELECT')

        for f in bm.faces:
            f.select = len(f.verts) == 3

        bmesh.update_edit_mesh(obj.data, loop_triangles=False, destructive=False)
        return {'FINISHED'}