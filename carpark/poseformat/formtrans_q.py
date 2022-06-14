from scipy.spatial.transform import Rotation
import numpy
import sys

fileA = open('D:/Blender/dataset/dataset0607/groundtruth/trajectory_0607_euler_after.txt', 'r')
fileB = open('D:/Blender/dataset/dataset0607/groundtruth/trajectory_0607_q_after.txt', 'w')
sys.stdout = fileB

for i in range(0, 2400):
    data = fileA.readline()
    data = data.split(", ")
    frame = data[0]
    t_x = data[1]
    t_y = data[2]
    t_z = data[3]
    euler_x = float(data[4])
    euler_y = float(data[5])
    euler_z = float(data[6])

    rot = Rotation.from_euler('xyz', [euler_x, euler_y, euler_z], degrees = False)
    rot_quat = rot.as_quat()
    print(frame, t_x, t_y, t_z, "{:5f}".format(rot_quat[0]), "{:5f}".format(rot_quat[1]), "{:5f}".format(rot_quat[2]), "{:5f}".format(rot_quat[3]))

sys.stdout = sys.__stdout__
fileA.close()
fileB.close()
