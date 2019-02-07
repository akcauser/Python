
# bu metod da center metoduna benzer ama işlevi biraz farklı

##yalnızca girilen karakter dizisinin sol tarafına girilen parametre kadar yere yazar ve boşluklara 0 ekleme işlevi görür


city = "alanya"

print(city.zfill(10))


##bunu rjust ile de yapabilriiz -- aynı işlemdir

print(city.rjust(10,"0"))


