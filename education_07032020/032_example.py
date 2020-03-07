#kullanıcının girdiği 2 sayı arasındaki çift sayıların ortalamasını bulup ekrana yazdıran fonksiyonu
#en büyük ve en küçüç çift sayıların toplamının yarısı ortalamalarını verir

def ortalamaCift(a,b):
    sum = 0
    sayac = 0
    for i in range(a,b):
        if i % 2 == 0:
            sum = sum + i
            sayac = sayac + 1
    average = sum / sayac
    return average

sayi1 = int(input())
sayi2 = int(input())
print(ortalamaCift(sayi1,sayi2))