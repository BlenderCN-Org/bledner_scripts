#simple python function that prints coordinates of selected vertex in blender
import bpy
import bmesh
from bpy.props import *
armature = ''
bone_name = ''
x = 0
y = 0
z = 0


def get_vertex_coords(object_reference):
    bm = bmesh.from_edit_mesh(object_reference.data)
    selected_verts = [vert for vert in bm.verts if vert.select]
    v_world = []

    mesh = bpy.context.active_object

    #just in case multiple selected verts
    for id in selected_verts:
        v_world.append(mesh.matrix_world *id.co)

    vertex_world  = v_world[0]

    print ('vertex_world')
    print (vertex_world)


    x = vertex_world[0]
    y = vertex_world[1]
    z = vertex_world[2]
    return x, y, z, vertex_world

