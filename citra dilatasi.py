# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 03:25:04 2021

@author: Wisnu
"""

from PIL import Image
from math import floor

def citraskala(gambar, s):
    CITRA_SKALA = Image.open(gambar)
    PIXEL =  CITRA_SKALA.load()

    ukuran_horizontal =  CITRA_SKALA.size[0]
    ukuran_vertikal =  CITRA_SKALA.size[1]

    ukuran_horizontal_baru = floor(ukuran_horizontal * s)
    ukuran_vertikal_baru = floor(ukuran_vertikal * s)
    
    CITRA_BARU = Image.new("RGB", (ukuran_horizontal_baru, ukuran_vertikal_baru))
    PIXEL_BARU = CITRA_BARU.load()

    for x in range(ukuran_horizontal_baru):
        for y in range(ukuran_vertikal_baru):
            x_lama = ukuran_horizontal * x / ukuran_horizontal_baru
            y_lama = ukuran_vertikal * y / ukuran_vertikal_baru
            PIXEL_BARU[x, y] = PIXEL[x_lama, y_lama]

    after_save = gambar + ' dilatasi skala ' + str(s).replace('.', ',') + '.jpg'
    CITRA_BARU.save(after_save)


citraskala('gambar1.jpg', 0.7)
citraskala('gambar1.jpg', 1.6)
citraskala('gambar2.jpg', 0.7)
citraskala('gambar2.jpg', 1.6)
citraskala('gambar3.jpg', 0.7)
citraskala('gambar3.jpg', 1.6)
citraskala('gambar4.jpg', 0.7)
citraskala('gambar4.jpg', 1.6)
citraskala('gambar5.jpg', 0.7)
citraskala('gambar5.jpg', 1.6)