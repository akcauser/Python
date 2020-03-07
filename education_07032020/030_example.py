#Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayıp ekrana yazdıran program

maas = float(input())
zamOrani = float(input())

zamMiktari = maas*zamOrani/100

maas = maas + zamMiktari

print(maas)