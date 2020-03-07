hangiSatir = 3
#hangiSatir = hangiSatir - 1
f = open("users.txt", "r")
#print(f.readlines()[hangiSatir-1])

in_email = input("mail gir")
in_password = input("şifre gir")
logged = 0
for i in f:
    email = i.split("-")[0]
    password = i.split("-")[1]
    #print(in_email,in_password)
    if in_email == email and in_password == password:
        logged = 1
        break
"""  else:
        logged = 0 """

if (logged == 1):
    print("Hoşgeldiniz")
else:
    print("hatalı giriş")
f.close()
