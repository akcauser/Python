

    ##biraz daha ilerleme zamanı artık
    ##işi karakter dizisinin bölmektir
    ## girilen parametreyi dizi içinde bulur ve o parametrenin sağ ve sol tarafı ve kendisi olmak üzere 3 e böler
    ## bunu da bir listeye atama işlemi yapar

city = "alanya"

print(city.partition("an"))

## eğer parametre dizide yoksa sondaymış gibi yapar 1. kısma tamamını diğer iki kısmı da boş olrak döndürür

print(city.partition("h"))

## peki aynı karakterden birkaç tane varsa

print(city.partition("a"))

## o zaman ilk gördüğünü alır ve işlemi bitirir.

## rpartition birazck bu durumu çözüyor ama tam değil emin olun

print(city.rpartition("a"))

## rpartition =right= yani sondan başlayarak tarama yapıyor tek farkı bu


##buradan sonra encode metodu var ama yazma ihtiyacı duymamamız normal
##expandtabs metodu da sekme boşluklarını genişletme işlemi yapıyor
