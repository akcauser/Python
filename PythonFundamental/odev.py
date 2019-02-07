#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:33:01 2018

@author: ertugrulgaziakca
"""

isim = input("Adınız giriniz:")
soyisim = input("Soyadınız giriniz:")
yas = input("yaşınızı giriniz:")
currentYear = input("Şu anda hangi yıldasınız:")
birthYear = int(currentYear) - int(yas) 

print("Merhaba",isim,soyisim,"ilk programıma hoş geldin",birthYear,"yılında doğdun")