# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 03:09:28 2021

@author: Wisnu
"""

from PIL import Image

def clipping(intensitas):
    if intensitas < 0:
        return 0
    if intensitas > 0:
        return 255
    return intensitas

def citrapencerahan(gambar, nilaicerah, after_save):
    CITRA_PENCERAHAN = Image.open(gambar)
    PIXEL = CITRA_PENCERAHAN.load()
    
    ukuran_horizontal = CITRA_PENCERAHAN.size[0]
    ukuran_vertika = CITRA_PENCERAHAN.size[1]
    
    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertika):
            R = clipping(PIXEL[x,y][0] + nilaicerah)
            G = clipping(PIXEL[x,y][1] + nilaicerah)
            B = clipping(PIXEL[x,y][2] + nilaicerah)
            PIXEL[x,y] = (R, G, B)
            
    CITRA_PENCERAHAN.save(after_save)
    
citrapencerahan('gambar1.jpg', 10, 'gambar1_dicerahkan.jpg')
citrapencerahan('gambar1.jpg', -170, 'gambar1_digelapkan.jpg')
citrapencerahan('gambar2.jpg', 10, 'gambar2_dicerahkan.jpg')
citrapencerahan('gambar2.jpg', -170, 'gambar2_digelapkan.jpg')
citrapencerahan('gambar3.jpg', 10, 'gambar3_dicerahkan.jpg')
citrapencerahan('gambar3.jpg', -170, 'gambar3_digelapkan.jpg')
citrapencerahan('gambar4.jpg', 10, 'gambar4_dicerahkan.jpg')
citrapencerahan('gambar4.jpg', -170, 'gambar4_digelapkan.jpg')
citrapencerahan('gambar5.jpg', 10, 'gambar5_dicerahkan.jpg')
citrapencerahan('gambar5.jpg', -120, 'gambar5_digelapkan.jpg')