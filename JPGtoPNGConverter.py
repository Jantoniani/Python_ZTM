import sys
import os
from PIL import Image


folder_1 = sys.argv[1]

folder_2 = sys.argv[2]


def jpg_png_converter(f1=folder_1, f2=folder_2):
    if os.path.isdir(f2):
        print("Good job, Directory 2 exists!")
    else:
        print("Directory 2 is incorrect or does not exist.  It will be created")
        os.mkdir(f2)

    if os.path.isdir(f1):
        print("Good job, Directory 1 exists!")
        imgs = os.listdir(f1)
        for img in imgs:
            picture = Image.open(img)
            clean_name = os.path.splitext(img)[0]
            picture.save(f2+'/'+clean_name+'.png', 'png')
    else:
        print("Directory 1 is incorrect or does not exist")


jpg_png_converter()

