#1den kullanıcının girdiği sayıya kadar olan tek ve çift sayıların toplamını ayrı ayrı bulan program
"""
print(pow(5,2))
print(5**2)
"""

sayi = int(input())

sumTek = 0
sumCift = 0

for i in range(1,sayi):
    if i % 2 == 0:
        sumCift = sumCift + i
    else:
        sumTek = sumTek + i

print(sumTek, sumCift)