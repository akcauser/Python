
first = "şçöğüıŞÇÖĞÜİ"
end = "scoguıSCOGUI"

ceviri_tablosu = str.maketrans(first,end)
print(ceviri_tablosu)

yazi  =  "alanyamız çok güzel bir şehirdir. hepinizi alanyaya bekleriz"

print(yazi.translate(ceviri_tablosu))

## maketrans() -->> bu metodun 3 parametresi vardır. 1. parametrenin yerine 2. parametredekiler yazılır.
## 3. parametre ise silinecek olan karakterlerin girilmesidir.

silTablosu = str.maketrans('','',"aeıioöuü")

print(yazi.translate(silTablosu))

##bu şekilde sesli harfleri silmiş olduk

