# tugas-PSO 2
## Here is convolution script program that was self-built without a single library 
```python
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
```
    
  Convolution process runs by calling function of  ``` convselfmade(sinyal, filter)```. sinyal is your signal that will be convoluted. filter is your kernel of convolution base.
    
  Here is some result of the convolution result by self-made program and some comparison with numpy library
  ![Screenshot (10)](https://github.com/dheatirtaa/tugas-PSO/assets/144766452/c6a70e47-f582-49ce-a11c-153f56832d91)
