# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 03:29:36 2021

@author: Wisnu
"""

from PIL import Image

def flippingvertikal(gambar, after_save):
    CITRA_FLIPPING = Image.open(gambar)
    PIXEL = CITRA_FLIPPING.load()

    ukuran_horizontal = CITRA_FLIPPING.size[0]
    ukuran_vertikal = CITRA_FLIPPING.size[1]

    CITRA_BARU = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    PIXEL_BARU = CITRA_BARU.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            PIXEL_BARU[x, y] = PIXEL[x, ukuran_vertikal - 1 - y]

    CITRA_BARU.save(after_save)


def flippinghorizontal(gambar, after_save):
    CITRA_FLIPPING = Image.open(gambar)
    PIXEL = CITRA_FLIPPING.load()

    ukuran_horizontal = CITRA_FLIPPING.size[0]
    ukuran_vertikal = CITRA_FLIPPING.size[1]

    CITRA_BARU = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    PIXEL_BARU = CITRA_BARU.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            PIXEL_BARU[x, y] = PIXEL[ukuran_horizontal - 1 - x, y]

    CITRA_BARU.save(after_save)

def flippingtitikasal(gambar, after_save):
    CITRA_FLIPPING = Image.open(gambar)
    PIXEL = CITRA_FLIPPING.load()

    ukuran_horizontal = CITRA_FLIPPING.size[0]
    ukuran_vertikal = CITRA_FLIPPING.size[1]

    CITRA_BARU = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    PIXEL_BARU = CITRA_BARU.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            PIXEL_BARU[x, y] = PIXEL[ukuran_horizontal - 1 - x, ukuran_vertikal -1 -y]

    CITRA_BARU.save(after_save)

flippingvertikal('gambar1.jpg', 'gambar1_flip_vertikal.jpg')
flippinghorizontal('gambar1.jpg', 'gambar1_flip_horizontal.jpg')
flippingtitikasal('gambar1.jpg', 'gambar1_flip_titik_asal.jpg')
flippingvertikal('gambar2.jpg', 'gambar2_flip_vertikal.jpg')
flippinghorizontal('gambar2.jpg', 'gambar2_flip_horizontal.jpg')
flippingtitikasal('gambar2.jpg', 'gambar2_flip_titik_asal.jpg')
flippingvertikal('gambar3.jpg', 'gambar3_flip_vertikal.jpg')
flippinghorizontal('gambar3.jpg', 'gambar3_flip_horizontal.jpg')
flippingtitikasal('gambar3.jpg', 'gambar3_flip_titik_asal.jpg')
flippingvertikal('gambar4.jpg', 'gambar4_flip_vertikal.jpg')
flippinghorizontal('gambar4.jpg', 'gambar4_flip_horizontal.jpg')
flippingtitikasal('gambar4.jpg', 'gambar4_flip_titik_asal.jpg')
flippingvertikal('gambar5.jpg', 'gambar5_flip_vertikal.jpg')
flippinghorizontal('gambar5.jpg', 'gambar5_flip_horizontal.jpg')
flippingtitikasal('gambar5.jpg', 'gambar5_flip_titik_asal.jpg')