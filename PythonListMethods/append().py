
#Created by Ertuğrul Gazi AKÇA at 15.01.2019

#TR/EN

#Listeye bir eleman eklemek için kullanılır
#This method use add an item to list or tuple

#Boş bir liste tanımlayalım
#list define
liste = []

#Eklediğimiz eleman listenin en sonuna eklenir
#The item that we added, adding as last item of list

liste.append("ders1")
print(liste)
liste.append("ders2")
print(liste)


#Kullanıcıdan sayıları alıp bir diziye ekle ve en sonda dizideki sayıları çarp.
#Dizideki eleman sayısı 2 den az ise kullanıcıyı uyar.

#Take some number from user and append a list
#After write to console multiplication of all number


numberList = []


while True:
    number = input("Sayı giriniz.(Çıkmak için q giriniz)")
    if len(numberList) < 2 and number == "q":
      print("please enter more number")
    elif len(numberList) >= 2 and number == "q":
        break
    else:
        numberList.append(int(number))

multiNum = 1

for i in numberList:
    multiNum *= i

print(multiNum)