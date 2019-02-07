##title metodu da capitalize metoduna çok benzer ama title metodunda farklı olan şey
##karakter dizisindeki bütün kelimelerin ilk harfini büyütmesidir.

city = "istanbul büyükşehir belediyesi ibb"

print(city.title())

for i in city.split():
    if i.startswith("i"):
        i = "İ" + i[1:]
    elif i.startswith("ı"):
        i = "I" + i[1:]
    i = i.title()
    print(i, end=" ")




