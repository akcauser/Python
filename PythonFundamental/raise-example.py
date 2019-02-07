#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 22:01:22 2018

@author: ertugrulgaziakca
"""

tr_karakter = "şçıİğöü"
parola = input("Parolanız: ")
for i in parola:
    if i in tr_karakter:
        raise TypeError("Parolada Türkçe karakter kullanılamaz!")
    else:
        pass
print("Parola kabul edildi!")        

