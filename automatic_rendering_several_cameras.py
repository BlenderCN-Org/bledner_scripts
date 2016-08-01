#script for automatical render from several cameras
#all cameras should have standrat names (like "Camera.001")
import bpy
#function for render from one camera
def render_one_camera (frame, frame_end):
    while frame < frame_end:

        #set current frame to frame that we need
        bpy.context.scene.frame_set(frame)

        bpy.ops.render.render(write_still=True) 
        frame = frame + 1
#number of cameras
#function for setup camera as an active camera
def set_camera(camera):
    camera_name = 'Camera'
    if camera != 0:
        camera_name = 'Camera' + '.00' + str(camera)
    bpy.context.scene.camera = bpy.data.objects[camera_name]

    your_node.base_path = '//your_node' + camera_name


bpy.ops.wm.open_mainfile(filepath="youfilepath.blend")
nodes = bpy.data.scenes[0].node_tree.nodes 
your_node = nodes["File Output.001"] 
#number of cameras
cameras= 9
i = 0 
while i < cameras:
    
    set_camera(i)
    render_one_camera(0,55)
    i = i + 1


bpy.utils.register_module(__name__)
