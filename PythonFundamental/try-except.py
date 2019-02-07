#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 17:34:28 2018

@author: ertugrulgaziakca
"""

sayi1 = 5
sayi2 = "asd"

try:
    
    print(sayi1/sayi2)
except ZeroDivisionError:
    print("sayılar 0 a bölünmez")
except ValueError:
    print("sadece sayılar birbirine bölünebilir.")   
except TypeError:
    print("Bir hata oluştu")
    
