#kullanıcının girdiği 2 sayı arasındaki sayıların toplamını bulan program
a= int(input())
b= int(input())

sum = 0
for i in range(a,b):
    sum = sum + i

print(sum)