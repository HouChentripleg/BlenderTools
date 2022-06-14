import os
import sys

path = "E:\\1ggg's graduate works\\neuroslam\\dataset0530\\dataset0530\\images\\0001.png"
file = open(path, "rb")
data = file.read()
file.close()
for i in range(1, 120):
    newfile = open(f"E:\\1ggg's graduate works\\neuroslam\\test_0530\\{i}.png", "wb")
    newfile.write(data)
newfile.close()

