
   #   replace() metodu parametreleri şu şekildedir. 1. parametrede girilen değeri bulup 2. parametreyi onun yerine koyar

myHome = "memleketket"

print(myHome.replace("ket","KET"))

print(myHome)  # ama kalıcı değildir

# eğer birden fazla aynı değer var ise hepsini birden değiştiri

print(myHome.replace("ket","KET",1))

# yani 3. parametre bu terimlerin kaç tanesinin değiştirileceğinin girildiği parametredir

##NOT: karakter dizileri yani string ler değiştirilemez yapılardır. başka bir atama işlemi yaılmadan değiştirilemezler



