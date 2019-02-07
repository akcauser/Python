
    # dir() bize içine girdiğimiz veri tipi için kullanabileceğimiz fonksiyonları döndürür.

print(dir(str))
print(dir(int))
sayac = 0
for i in dir(str):
    if "_" not in i[0]:
        sayac += 1
        print(sayac,i)

print("toplamda {} tane fonksiyon ile ilgilenmekteyiz".format(sayac))

