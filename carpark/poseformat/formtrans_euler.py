import sys

fileA = open('D:/Blender/dataset/dataset0607/groundtruth/trajectory_0607_euler.txt', 'r')
fileB = open('D:/Blender/dataset/dataset0607/groundtruth/trajectory_0607_euler_after.txt', 'w')

sys.stdout = fileB

for i in range(0, 2400):
    data = fileA.readline()
    data = data.replace("<Euler (", '')
    data = data.replace("), order='XYZ'>", '')
    data = data.replace('x=', '')
    data = data.replace('y=', '')
    data = data.replace('z=', '')
    data = data.replace(',', '')
    data = data.replace(' ', ", ")
    data = data.replace('\n', '')
    print(data)

sys.stdout = sys.__stdout__
fileA.close()
fileB.close()