hangiSatir = 3
#hangiSatir = hangiSatir - 1
f = open("bilgi.txt", "r")
#print(f.readlines()[hangiSatir-1])

for i in f:
    print(i, end="")

f.close()
