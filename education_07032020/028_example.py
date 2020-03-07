#girilen sayını faktöriyel değerini bulan program

sayi = int(input())

sum = 1
for i in range(1,sayi+1):
    sum = sum * i

print(sum)