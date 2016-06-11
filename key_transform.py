#python script for Blender for copy animation data to different keyframes
import bpy
from bpy.props import *
target = ''
soucre = ''

#this function is for сopy animations from given frames from start to end
def animation_transform(target,source, start, end):
	bpy.ops.object.select_by_type(type='EMPTY')
	bpy.data.objects[target].select = True
	turn = bpy.data.objects["target_armature"].rotation_euler.x
	if turn !=0.0:
		bpy.ops.transform.rotate(value=(0-turn), axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
	frame_num = start
	while frame_num < end:
		frame_transform(target, source, frame_num)
		bpy.context.scene.update()
		frame_num = frame_num+1

def frame_transform(target, source, frame_num):
	print(frame_num)
	transform(target,source)
	
	bpy.ops.anim.keyframe_insert_menu(type='Available')
	bpy.context.scene.frame_set(frame_num)

#this function is for copying animation from one armature to another for one frame	
def transform(target,source):
	
	source_armature = bpy.data.objects[source]
	source_armature_bones = source_armature.data.bones
	for bone in source_armature_bones:
		bpy.data.objects[target].pose.bones[bone.name].matrix = bpy.data.objects[source].pose.bones[bone.name].matrix
		bpy.context.scene.update()
		bpy.ops.anim.keyframe_insert_menu(type='Available')

		
#this is interface
def initSceneProperties(scn):
    bpy.types.Scene.StartFrame = IntProperty(
        name = "Start Frame", 
        description = "Enter an Start Frame",
        default = 0,
        min = 0,
        max = 100)
    scn['StartFrame'] = 0
    
    bpy.types.Scene.EndFrame = IntProperty(
		name = "End Frame", 
		description = "Enter an End Frame",
        default = 0,
        min = 0,
        max = 100)
    scn['EndFrame'] = 0
 

 
    bpy.types.Scene.TargetArmature = StringProperty(
        name = "Target Armature")
    scn['TargetArmature'] = "target_armature"
    
    bpy.types.Scene.SourceArmature = StringProperty(
        name = "Source Armature")
    scn['SourceArmature'] = "source_armature"
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
        layout.prop(scn, 'StartFrame')
        layout.prop(scn, 'EndFrame')
        layout.prop(scn, 'TargetArmature')
        layout.prop(scn, 'SourceArmature')
        layout.operator("idname_must.be_all_lowercase_and_contain_one_dot")
 

class OBJECT_OT_PrintPropsButton(bpy.types.Operator):
    bl_idname = "idname_must.be_all_lowercase_and_contain_one_dot"
    bl_label = "Make magic"
 
    def execute(self, context):
        scn = context.scene
        printProp("StartFrame:    ", 'StartFrame', scn)
        printProp("EndFrame:    ", 'EndFrame', scn)
        printProp("TargetArmature: ", 'TargetArmature', scn)
        printProp("SourceArmature: ", 'SourceArmature', scn)
        target = scn['TargetArmature']
        source = scn['SourceArmature']
        start = scn['StartFrame']
        end = scn['EndFrame']
        animation_transform(target, source, start, end)
        return{'FINISHED'}    
 
def printProp(label, key, scn):
    try:
        val = scn[key]
    except:
        val = 'Undefined'
    print("%s %s" % (key, val))
 

bpy.utils.register_module(__name__)
