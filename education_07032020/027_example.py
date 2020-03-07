#girilen sayının asal mı değil mi olduğunu bulan program
sayi = int(input())

isPrime = True
for i in range(2,sayi):
    if  sayi % i == 0:
        isPrime = False
        break

if isPrime:
    print("Asaldır")
else:
    print("Asal değildir")