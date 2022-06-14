from distutils import filelist
from fileinput import filename
import os
import re
import sys

path = "E:\\1ggg's graduate works\\neuroslam\\test_0530"
filelist = os.listdir(path)
filetype = ".png"
for file in filelist:
    olddir = os.path.join(path, file)
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]
    newdir = os.path.join(path, filename.zfill(5) + filetype)
    os.rename(olddir, newdir)