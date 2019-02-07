##BU METODLARI KULLANICIDAN ALDIĞIMIZ KARAKTER DİZİLERİNİ KONTROL ETMEK İÇİN KULLANIYORUZ

#Lower metodu ile girilen bir karakter dizisinin bütün harflerini küçük harfe çevirebiliriz

cityName = "Alanya"

print(cityName.lower())

cityName1 = "İstanbul"

print(cityName1.lower())

##Bu metodun şöyle bir problemi var. Girilen karakterin büyük İ harfi olursa çıktı biraz garip oluyor.Büyük I harfi de aynı şekilde
##elimiz armut toplanmıyor ya çözüm altta

cityName1 = cityName1.replace("İ","i").replace("I","ı").lower()

print(cityName1)

##Burada aynı zamanda metodları nasıl uç uca  eklediğimizi de görmüş olduk


##upper() metodu ise lower metodunun tam tersi olarak bütün harfleri büyük harf yapar


print(cityName.upper())

#yine aynı şekilde ı ve i harflerinde sıkkıntılarımız var düzeltelim hemen

myName = "ilyas"

print(myName.upper())

myName = myName.replace("i","İ").replace("ı","I").upper()

print(myName)

#isupper ve islower metodları ise bize boolean değerler döndürür.
#Girilen değerin bütün harflerinin küçük mü büyük mü olduğunu kontrol eder.
#Eğer bütün harfler küçükse islower değeri true isupper değeri false return edecektir.

name = "Ali"

if name.islower():
    print("bütün harfler küçük")
else:
    name = name.lower()

print(name)



