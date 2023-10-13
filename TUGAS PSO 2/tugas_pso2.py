# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:46:55 2023

@author: ASUS
"""

print("Dhea Tirta Ananta")
print("NRP : 5009201030")

#bismillah
#pembuatan fungsi untuk konvolusi data 1 dimensi
def convselfmade(sinyal, filter):
    #identifikasi panjang setiap sinyal
    panjang_filter = len(filter)
    panjang_sinyal = len(sinyal)
    panjang_output = panjang_sinyal + panjang_filter - 1
    #penentuan output awal sebagai himpunan nol
    output = [0] * panjang_output
    # konvolusi dengan looping 2x
    for i in range(panjang_output):
        #mengisi nol di awal untuk setiap indeks
        output[i] = 0
        #konvolusi setiap satu data dengan syarat
        for j in range(panjang_filter):
            if i - j >= 0 and i - j < panjang_sinyal:
                output[i] += sinyal[i - j] * filter[j]

    return output
 
filter=[10, 14, 22]
sinyal=[1,0,3,0]
#panggil fungsi konvolusi untuk 2 sinyal   
hasil=convselfmade(sinyal, filter)
print(hasil)

