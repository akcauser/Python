# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


"""import keyword"""
"""import os"""
import sys

"""os.getcwd"""

print("hello world")

"""print(keyword.kwlist)"""

dosya = open("deneme1.txt","w")

"""
file - Normalde print fonksiyonu file parametresi ile beraber gelir. 
       Default olarak sys.stdout değerini alır. bu değer standart çıktı anlamına gelir 
       ve konsola verilerin yazılmasını sağlar
flush - dosyayı kapatmadan dosya içerisine verilerin akmasın istiyorsak flush parametresi kullanılır.
        Bu parametreni öntanımlı değeri False 'tır.
sep - seperate anlamına gelen sep parametresi default olarak " " değerini alır. 
        parameteyi override ederek iki parametere arasına farklı bir değer girebiliriz.
end - sep komutuna benzer ama bu sefer adından da anlaşılabileceği gibi satırın sonuna gelmesini 
        istediğimiz değeri girmemizi sağlar.Default olarak "/n" değeri ile gelir.
        
"""

print("ali","veli",sep=" "+"5"+" ",end=".",file=dosya,flush=True)

dosya.close  

"""  *'lı ipuçları """

print(*"Alanya",sep=".")

f = open("dosya.txt","w")

sys.stdout ,f = f, sys.stdout

print(sys.stdout,flush=True)

sys.stdout ,f = f, sys.stdout

print("artık yazıklarımız dosya.txt isimli dosyaya yazılıyor",flush=True)

"""
Bu arada kaçış dizilerini yani '\' işaretinin kullanımı ile alakalı bir bölümü işledik
"""

isim = "ali"
sehir = "İstanbul"

print("isim :",isim,"\n",
      "sehir:",sehir,"\n",
      sep = "")

#işareti yorum satırı anlamına gelmektedir.









    











