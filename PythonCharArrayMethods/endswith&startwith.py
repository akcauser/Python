#endwith metodu bize boolean değeri döndürür
#içine sorgulamak istedğimiz parametreyi yazıyoru.
#eğer karakter dizisinin son indexi girilen parametre ile aynı değer ise 'true' değer döndürü.

cityName = "Alanya"

if cityName.endswith("a"):
    print(cityName,"a harfi ile bitiyor")

d1 = "ses.mp3"
d2 = "resim.jpg"
d3 = "movie.avi"
d4 = "falanca.mp3"

list = [d1,d2,d3,d4]

for i in list:
    if i.endswith(".mp3"):
        print(i)

#startwiths metodu da aynı işlmin tersini yapar
#yani ilk indexin değerini kontrol için kullanılır

for i in list:
    if i.startswith("f"):
        print(i)

