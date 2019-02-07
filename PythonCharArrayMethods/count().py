
## count() metodu içerisine girilen karakterin dizi üzerinde kaç kez geçtini veren bir metod


city = "kahramanmaraş"

print(city.count("a"))
print(city.count("man"))

##içine gireildiğimiz 2 tane parametre var. 1. parametre başlangıç 2.parametre bitiş indeksini veriyor.
##yani istediğimiz indeksler arasını da tarama yapabiliyoruz

print(city.count("a",-5,13))

##parolada aynı karakteri yalnızca 1 kez girme fonksiyonu

kontrol = True

parola = input("Parola gir")

for i in parola:
    if parola.count(i) > 1:
        kontrol = False

if kontrol:
    print("Parola geçerli")
else:
    print("Same character used. Again please")

tekHarfler = ""

for i in parola:
    if i not in tekHarfler:
        tekHarfler += i

for i in tekHarfler:
    print("{} harfi {} kelimesinde {} adet geçiyor".format(i,
                                                           parola,
                                                           parola.count(i)))
