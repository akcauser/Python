import sys

ad = input("Adınızı giriniz:")
soyad = input("Soyadınızı giriniz:")
email = input("Email adresi giriniz:")

f = open("users.txt", "w")
standard_output = sys.stdout
sys.stdout = f

print(ad,soyad,email,sep="-")

sys.stdout = standard_output

f.close()