#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:45:56 2018

@author: ertugrulgaziakca
"""


d1 = open("deneme1.txt")
d1_satirlar = d1.read()
print(d1_satirlar)
harf = "ö"

i=0
for s in d1_satirlar:
      if s == harf:
        i += 1

print(i)        
   
d1.close 





