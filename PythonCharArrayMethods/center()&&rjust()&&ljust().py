
## center() komutu  karakter dizilerini ortalama işlemi yapmaktadır

## yani mesela parametre olrak 10 girdiysek 10 karakterlik bir bölgede ortalama işlemi yapacaktır


city = "alanya"

print(str.center(city,10,"-"))

## 1.parametre kaç karakterlik yer kaplayacak ?? 10
## 2. parametre ise boşlukları nasıl dolduracak ---> default değeri " " olmaktadır.

## rjust metodu ile ljust metodu da sağa ve sola yaslama işlmelerini gerçekleştirmektedir.
## 2. parametre de aynı görevi yani boşlukların ne ile dldurulacağını söyler


print(city.rjust(10,"-"))
print(city.ljust(10,"-"))