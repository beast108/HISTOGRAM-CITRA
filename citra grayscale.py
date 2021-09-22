# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 16:09:00 2021

@author: Wisnu
"""

from PIL import Image

def citragrayscale(gambar):
    CITRA_GRAYSCALE = Image.open(gambar)
    NEWGRAY = CITRA_GRAYSCALE.convert('L')
    
    after_save = gambar + 'negatif.jpg'
    NEWGRAY.save(after_save)
    
citragrayscale('gambar1.jpg')
citragrayscale('gambar2.jpg')
citragrayscale('gambar3.jpg')
citragrayscale('gambar4.jpg')
citragrayscale('gambar5.jpg')