# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 02:33:22 2021

@author: Wisnu
"""

from PIL import Image

#fungsi citra biner
def citrabiner(gambar, nilaiambang):
  
    CITRA_GRAYSCALE = Image.open(gambar).convert('L')
    PIXEL_GRAYSCALE = CITRA_GRAYSCALE.load()
    
    ukuran_horizontal = CITRA_GRAYSCALE.size[0]
    ukuran_vertikal = CITRA_GRAYSCALE.size[1]
    
    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            if PIXEL_GRAYSCALE[x,y] < nilaiambang:
                PIXEL_GRAYSCALE[x,y] = 0
            else:
                PIXEL_GRAYSCALE[x,y] = 255
                
    after_save = gambar + str(nilaiambang) + '.jpg'
    CITRA_GRAYSCALE.save(after_save)
    
    
citrabiner('gambar1.jpg', 50)
citrabiner('gambar1.jpg',128)
citrabiner('gambar1.jpg',200)
citrabiner('gambar1.jpg',230)

citrabiner('gambar2.jpg', 50)
citrabiner('gambar2.jpg',128)
citrabiner('gambar2.jpg',200)
citrabiner('gambar2.jpg',230)

citrabiner('gambar3.jpg', 50)
citrabiner('gambar3.jpg',128)
citrabiner('gambar3.jpg',200)
citrabiner('gambar3.jpg',230)

citrabiner('gambar4.jpg', 50)
citrabiner('gambar4.jpg',128)
citrabiner('gambar4.jpg',200)
citrabiner('gambar4.jpg',230)

citrabiner('gambar5.jpg', 50)
citrabiner('gambar5.jpg',128)
citrabiner('gambar5.jpg',200)
citrabiner('gambar5.jpg',230)