# 123.py

import sys

sys.path.append(r"C:\Users\Phil\Anaconda3\envs\houdini\Lib\site-packages")





import hou
# Create Camera - 1080
def create_camera():
    cam = hou.node("/obj").createNode("cam", "cam_1080")
  
    cam.setDisplayFlag(False)

# Create Mantra - PBR driver
def mantra_driver():
    rop = hou.node("/out").createNode("ifd")

def main():
    create_camera()
    mantra_driver()

main()