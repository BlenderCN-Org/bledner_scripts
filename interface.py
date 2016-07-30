#interface for typical plugin in blender
#this template can print parameter from user input in Blender interface to terminal
import bpy
from bpy.props import *
p_str= ''
p_number = 0


		
#this is interface
def initSceneProperties(scn):
    bpy.types.Scene.p_str = StringProperty(
        name = "Parameter 1")
    scn['p_str'] = 'example of string input'
    bpy.types.Scene.p_number = IntProperty(
        name = "Parameter 2")
    scn['p_number'] = 'example of int input'
    return
 
initSceneProperties(bpy.context.scene)

#this is the place for script  interface
class UIPanel(bpy.types.Panel):
    bl_label = "Property panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
 
    def draw(self, context):
        layout = self.layout
        scn = context.scene
        layout.prop(scn, 'p_str')
        layout.prop(scn, 'p_number')
        layout.operator("idname.1")
 

class OBJECT_OT_PrintPropsButton(bpy.types.Operator):
    bl_idname = "idname.1"
    bl_label = "Make magic"
 
    def execute(self, context):
        scn = context.scene
        printProp("Parameter 1: ", 'p_str', scn)
        printProp("Parameter 2: ", 'p_number', scn)

        return{'FINISHED'}    
 
def printProp(label, key, scn):
    try:
        val = scn[key]
    except:
        val = 'Undefined'
    print("%s %s" % (key, val))
 

bpy.utils.register_module(__name__)
