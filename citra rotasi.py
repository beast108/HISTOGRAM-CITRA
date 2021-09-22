# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 03:35:06 2021

@author: Wisnu
"""

from PIL import Image
from math import sin, cos


def citrarotasi(gambar, derajat):
    CITRA_ROTASI = Image.open(gambar)
    PIXEL = CITRA_ROTASI.load()

    ukuran_horizontal = CITRA_ROTASI.size[0]
    ukuran_vertikal = CITRA_ROTASI.size[1]

    CITRA_BARU = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    PIXEL_BARU = CITRA_BARU.load()

    x_tengah = ukuran_horizontal // 2
    y_tengah = ukuran_vertikal // 2

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
           
            theta = derajat * 22/7 / 180

            x_baru = (cos(theta) * (x - x_tengah) - sin(theta)
                      * (y - y_tengah) + x_tengah)
            y_baru = (sin(theta) * (x - x_tengah) + cos(theta)
                      * (y - y_tengah) + y_tengah)

            if (x_baru >= ukuran_horizontal or y_baru >= ukuran_vertikal
                    or x_baru < 0 or y_baru < 0):
                PIXEL_BARU[x, y] = (0, 0, 0)
            else:
                PIXEL_BARU[x, y] = PIXEL[x_baru, y_baru]

    after_save = gambar + ' rotasi ' + str(derajat) + '.jpg'
    CITRA_BARU.save(after_save)


citrarotasi('gambar1.jpg', 45)
citrarotasi('gambar1.jpg', 90)
citrarotasi('gambar1.jpg', 180)
citrarotasi('gambar1.jpg', 270)
citrarotasi('gambar2.jpg', 45)
citrarotasi('gambar2.jpg', 90)
citrarotasi('gambar2.jpg', 180)
citrarotasi('gambar2.jpg', 270)
citrarotasi('gambar3.jpg', 45)
citrarotasi('gambar3.jpg', 90)
citrarotasi('gambar3.jpg', 180)
citrarotasi('gambar3.jpg', 270)
citrarotasi('gambar4.jpg', 45)
citrarotasi('gambar4.jpg', 90)
citrarotasi('gambar4.jpg', 180)
citrarotasi('gambar4.jpg', 270)
citrarotasi('gambar5.jpg', 45)
citrarotasi('gambar5.jpg', 90)
citrarotasi('gambar5.jpg', 180)
citrarotasi('gambar5.jpg', 270)