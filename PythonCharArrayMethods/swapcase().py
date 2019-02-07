##swapcase metodu -> bu metod capitalize ve title ın benzeri bir metod
## olay şu küçük harfleri büyük - büyük harfleri küçük yapıyor

city = "İSTanb  UL"

print(city.swapcase()) ## hatalıdır


for i in city:
    if i == 'i':
        city = city.replace('i','İ')
    elif i == 'İ':
        city = city.replace('İ','i')
    else:
        city = city.replace(i,i.swapcase())

print(city)