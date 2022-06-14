import bpy
import sys

file = open('D:/Blender/dataset/dataset0607/groundtruth/trajectory_0607.txt', 'w')
sys.stdout = file

start_frame = 0
end_frame = 2400

bpy.context.scene.frame_start = start_frame
bpy.context.scene.frame_end = end_frame

cam = bpy.context.scene.objects["Camera"]

for frame in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end):
    bpy.context.scene.frame_set(frame)
    
    #print(frame, cam.matrix_world[0][3], cam.matrix_world[1][3], cam.matrix_world[2][3], cam.matrix_world.to_euler('XYZ'))
    print(frame, cam.matrix_world[0][3], cam.matrix_world[1][3], cam.matrix_world[2][3], cam.pose.rotation_quaternion)    
    
sys.stdout = sys.__stdout__

file.close()