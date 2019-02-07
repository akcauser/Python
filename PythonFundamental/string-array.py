#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 00:06:29 2018

@author: ertugrulgaziakca
"""

isim = input("isminizi giriniz: ")

for i in range(len(isim)):
    print("isminizin {}. harfi {}".format(i+1,isim[i]))

print(isim[::-1])

print(isim[0:3])
    

print(isim[1:2])

# karakter dizilerinde [--:--:--] 3 parametre vardır
#1. parametre nereden başlanacağğını verir default deger = 0
#2. parametre nereye kadar yazılacağını verir default deger = array.size
#3. parametre düzden mi tersten mi yazılacağını verir default deger == 1