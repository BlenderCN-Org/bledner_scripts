#here is script for export position of every bone in txt log file
#change 'your_filepath.txt' to your filepath
import bpy
from bpy.props import *
armature = ''


def script_copy(armature):
	output = open('your_filepath.txt', 'w')
	bones = bpy.data.objects[armature].data.bones
	for bone in bones:
		output.write(bone.name  + '\n')
		output.write(str(bone.head.x) + ' ')
		output.write(str(bone.head.y) + ' ')
		output.write(str(bone.head.z) + '\n')
		output.write(str(bone.tail.x) + ' ')
		output.write(str(bone.tail.y) + ' ')
		output.write(str(bone.tail.z) + '\n')
	output.close()
		
#this is interface
def initSceneProperties(scn):
    bpy.types.Scene.Armature = StringProperty(
        name = "Armature")
    scn['Armature'] = "name"
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
        layout.prop(scn, 'Armature')
        layout.operator("idname.1")
 

class OBJECT_OT_PrintPropsButton(bpy.types.Operator):
    bl_idname = "idname.1"
    bl_label = "Make magic"
 
    def execute(self, context):
        scn = context.scene
        armature = scn['Armature']
        script_copy(armature)
        return{'FINISHED'}    

 

bpy.utils.register_module(__name__)
