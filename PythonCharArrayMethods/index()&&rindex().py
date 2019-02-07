
#index metodu bize 1. parametrede girdiğimiz değerin ilk hangi indexkste karşılaşıldığı bilgisini verir
#2. ve 3. parametreleri ise aralık belirtir

city = "alanya"

print(city.index("a"))  # çok da iyi bir metod değildir , yerine aşağıdaki algoritma iş görüyor

counter = -1

for i in city:
    counter += 1
    if i == "a":
        print(counter)


## rindex metodu da aynı şeyi sağdan sola doğru yapmaktadır.



