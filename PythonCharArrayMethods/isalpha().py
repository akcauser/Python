##isalpha()  metodu verilen dizinin alfabetik mi olup olmadığını verir. True - False


yazi = "alanya07"
yazi1 = "alanya"

print(yazi.isalpha()) # false
print(yazi1.isalpha()) # True

## isdigit () ise aynı işlemin sayı değerli karakter dizisi olup olmamasını kontrol eder
print("----isdigit-----")
sayi1 = "134421"

print(sayi1.isdigit()) # True
print(yazi1.isdigit()) # False

#isalnum() alfanumerik yani harf ve sayı olabilir True verir

print("----isalnum-----")
print(yazi1.isalnum())  # True
print(yazi.isalnum())   #True
print("*sadda>".isalnum()) # False

#isdecimal() ondalık sayı mı değil mi_
print("----isdecimal-----")
print("123".isdecimal()) # True
print(yazi.isdecimal()) #False

#isidentifier() hangi değerini tanımlayıcı olup olamayacığını verir

print("---isidentifier------")
print("1a".isidentifier())
print("asd".isidentifier())

#isnumeric() isdigit ile aynı işlemi yapar
print("----isnumeric-----")
print()

#isspace()  tamamen boşluklardan oluşup oluşmadığını döndürür
print("----isspace-----")
print(" ".isspace())
print(" sdas  ".isspace())

#isprintable() komutu yazılamayan karakter olup olmadığını verir mesela \n \t \r  gibi
#yazılamayan karakter varsa

print("-----isprintable----")
print("\n".isprintable())
print("sda".isprintable())






