
    # enumerate() bizim dizinin elemanlarının sırasını tutabileceğimiz bir yapı sağlar

print(*enumerate(dir(str)))

for i in enumerate(dir(str)):
    print(i)

for i in enumerate("alanya"):
    print(i)

for sıra,metot in enumerate(dir(int)):
    print(sıra+1,metot)

