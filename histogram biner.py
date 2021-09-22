# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:39:03 2021

@author: Wisnu
"""
from os.path import basename
from os.path import splitext
from matplotlib import pyplot as plt

def get_file_name(file_path):
    return splitext(basename(file_path))[0]

def histogrambiner(gambar):
    img = plt.imread(gambar)

    plt.hist(img.flatten(), bins=[-.5,.5,1.5], ec="k")
    plt.xticks((0,1))
    plt.title('Histogram ' + gambar)
    plt.xlabel('Binary')
    plt.ylabel('Number of Pixel')
    plt.savefig('histogram biner ' + get_file_name(gambar) + '.jpg')
    plt.show()

histogrambiner('gambar1.jpg')
histogrambiner('gambar2.jpg')
histogrambiner('gambar3.jpg')
histogrambiner('gambar4.jpg')
histogrambiner('gambar5.jpg')
