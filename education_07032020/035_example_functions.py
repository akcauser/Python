#math kütüphanesinde bulunan pow fonksiyonunu kütüphane kullanmadan yazınız

def myPow(a,b):
    result = 1
    for i in range(b):
        result = result * a
    return result

print(myPow(2,3))