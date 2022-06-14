import os
import shutil

def ImageRename(olddir, newdir):
    filelist = os.listdir(olddir)
    for file in filelist:
        src = os.path.join(olddir, file)
        filename = str(int(os.path.splitext(file)[0]) + 119)
        filetype = os.path.splitext(file)[1]
        dst = os.path.join(newdir, filename.zfill(5) + filetype)
        shutil.move(src, dst)
    
if __name__ == '__main__':
    olddir = "E:\\1ggg's graduate works\\neuroslam\\dataset0530\\dataset0530\\images"
    newdir = "E:\\1ggg's graduate works\\neuroslam\\test_0530"
    ImageRename(olddir, newdir)