try:
    a = int(input())
    b = int(input())
    oprType = input("toplama: + \nçıkarma: - \nçarpma: * \nbölme: / \n")
    if oprType == "+":
        print(a + b)
    elif oprType == "-":
        print(a - b)
    elif oprType == "*":
        print(a * b)
    elif oprType == "/":
        print(a / b)
    else:
        print("geçersiz seçim")

except ValueError as hata:
    print("Girilen değer tamsayı değil", hata)

except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsin")

finally:
    print("Burası her zaman çalıştırılacaktır.")

