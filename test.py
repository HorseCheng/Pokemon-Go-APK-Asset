import cv2
import numpy as np
import os
import re

cnt=0
files=os.listdir("AudioClip")
for file  in files:
    try: 
        found=re.findall(".*#[0-9]+.wav", file)[0]
        os.remove(f"AudioClip/{file}")
        print(found)
        cnt+=1
    except:
        pass
print(cnt)