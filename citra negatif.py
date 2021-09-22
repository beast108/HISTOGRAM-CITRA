# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 03:05:01 2021

@author: Wisnu
"""


from PIL import Image
def citranegatif(gambar):
    CITRA_NEGATIF = Image.open(gambar)
    ukuran_horizontal = CITRA_NEGATIF.size[0]
    ukuran_vertikal = CITRA_NEGATIF.size[1]

    PIXEL = CITRA_NEGATIF.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            R = 255 - PIXEL[x, y][0]
            G = 255 - PIXEL[x, y][1]
            B = 255 - PIXEL[x, y][2]
            PIXEL[x, y] = (R, G, B)

    after_save = gambar + 'negatif.jpg'
    CITRA_NEGATIF.save(after_save)

    
citranegatif('gambar1.jpg')
citranegatif('gambar2.jpg')
citranegatif('gambar3.jpg')
citranegatif('gambar4.jpg')
citranegatif('gambar5.jpg')