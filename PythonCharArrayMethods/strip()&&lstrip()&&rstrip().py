##strip metodu bazı gereksiz karakterleri temizlemede kullanılabilir

## ilk olarak sağında ve solunda boşluk olan bir karakter dizisini bu boşluklardan kurtaralım

city = "istanbul    "

print(city.strip(),"*")


##parametre girilmediğinde karakter dizisinin sağındave solunda bulunna şu karakterleri temizler
                    ## " ", \t , \n , \r , \f , \v


##eğer parametre girersek istediğimiz baştaki ve sondaki karaktreleri de kırpmasını sağlayabiliriz
## önemli nokta şu ; bu metod karakter dizisinin başındaki ve sonundaki karakterlerle ilgilenir

print(city.strip("l"))

## lstrip ve rstrip metodları da yalnızca soldan veya yalnızca sağdan kırpma yapacağımız zaman kullanırız
