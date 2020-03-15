
takimAdiA = input("1. Takim adini giriniz")
takimAdiB = input("2. Takim adini giriniz")

takimPuaniA = [0,0,0,0]
takimPuaniB = [0,0,0,0]




while True:

    hangiPeriyot = int(input("Kaçıncı periyottayız? (Bitirmek için 0 ye basınız)"))

    if hangiPeriyot == 0:
        break
    print("Hangi takıma puan eklemek istiyorsunuz(", takimAdiA, "-", takimAdiB, ")?")
    hangiTakim = input()

    kacPuan = input("Kaç puan eklemek istiyorsunuz")

    if hangiPeriyot == 1:
        if hangiTakim == takimAdiA:
            takimPuaniA[0] += int(kacPuan)
            print(takimAdiA,"takımına", kacPuan, "eklendi")
        elif hangiTakim == takimAdiB:
            takimPuaniB[0] += int(kacPuan)
            print(takimAdiB, "takımına", kacPuan, "eklendi")


    elif hangiPeriyot == 2:
        if hangiTakim == takimAdiA:
            takimPuaniA[1] += int(kacPuan)
            print(takimAdiA, "takımına", kacPuan, "eklendi")
        elif hangiTakim == takimAdiB:
            takimPuaniB[1] += int(kacPuan)
            print(takimAdiB, "takımına", kacPuan, "eklendi")


    elif hangiPeriyot == 3:
        if hangiTakim == takimAdiA:
            takimPuaniA[2] += int(kacPuan)
            print(takimAdiA, "takımına", kacPuan, "eklendi")
        elif hangiTakim == takimAdiB:
            takimPuaniB[2] += int(kacPuan)
            print(takimAdiB, "takımına", kacPuan, "eklendi")


    elif hangiPeriyot == 4:
        if hangiTakim == takimAdiA:
            takimPuaniA[3] += int(kacPuan)
            print(takimAdiB, "takımına", kacPuan, "eklendi")
        elif hangiTakim == takimAdiB:
            takimPuaniB[3] += int(kacPuan)
            print(takimAdiB, "takımına", kacPuan, "eklendi")


    else:
        print("Yanlış değer")

    print("---------------------------------")
    print("|", "\t\t\t", takimAdiA, "\t", takimAdiB)
    print("|", "1.periyot \t", takimPuaniA[0], "\t\t", takimPuaniB[0], "\t\t|")
    print("|", "2.periyot \t", takimPuaniA[1], "\t\t", takimPuaniB[1], "\t\t|")
    print("|", "3.periyot \t", takimPuaniA[2], "\t\t", takimPuaniB[2], "\t\t|")
    print("|", "4.periyot \t", takimPuaniA[3], "\t\t", takimPuaniB[3], "\t\t|")
    print("|", "toplam \t", sum(takimPuaniA), "\t\t", sum(takimPuaniB), "\t\t|")
    print("---------------------------------")

print("---------------------------------")
print("|", "\t\t\t\t", takimAdiA, "\t\t", takimAdiB)
print("|", "1.periyot \t", takimPuaniA[0], "\t\t", takimPuaniB[0], "\t\t|")
print("|", "2.periyot \t", takimPuaniA[1], "\t\t", takimPuaniB[1], "\t\t|")
print("|", "3.periyot \t", takimPuaniA[2], "\t\t", takimPuaniB[2], "\t\t|")
print("|", "4.periyot \t", takimPuaniA[3], "\t\t", takimPuaniB[3], "\t\t|")
print("|", "toplam \t\t", sum(takimPuaniA), "\t\t", sum(takimPuaniB), "\t\t|")
print("---------------------------------")