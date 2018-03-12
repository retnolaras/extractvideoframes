# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:55:51 2016

@author: user
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

import matplotlib.pyplot as plt
import numpy as np
import cv2
from sklearn.cross_validation import train_test_split
from sklearn import cross_validation
import random

#%%


#%%

# image specification

fourcc = cv2.VideoWriter_fourcc(*'MJPG')

listing = os.listdir('NegsVid/')
success = True
count = 0

for vid in listing:
    vidn = 'NegsVid/'+vid
    #print vidn
    cap = cv2.VideoCapture(vidn)
    count = 0
    success = True
    while success:
        success,image = cap.read()
        #cv2.imshow("image", image)
        if count%40 == 0:
            cv2.imwrite('NegsKelas/' + vid[:-4] + "_Frame%d.jpg" % count, image)     # save frame as JPEG file
        count += 1
        
    cap.release()
cv2.destroyAllWindows()



