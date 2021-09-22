# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:39:03 2021

@author: Wisnu
"""

import cv2
from matplotlib import pyplot as plt


img = cv2.imread('gambar5.jpg',0) #file diisi disini


histr = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(histr)
plt.show()