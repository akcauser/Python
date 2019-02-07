
isim = input("isminizi giriniz:")
soyisim = "veli"
print(isim[0:5],"...",sep="")

#2 tane karakter dizisi biçimlendirme aracımız bulunmaktadır
#   1 -> % ile biçimlendirme
#   2 -> format metodu ile biçimlendirme (python 3 te geldi )


print("isminiz %s %s" %(isim,soyisim))
print("isminiz {} {}".format(isim,soyisim))

print("isminiz %(name)s"%{"name":"isim"})


#f-string metodu var

print(f"isminiz {isim}")

#f harfini koyduğumuzda doğrudan değişkenleri süslü parantez içinde yerine yazabiliyoruz