##capitalize metodu  -> Kullanılan karakter dizisinin yalnızca ilk harfini büyütmek için kullanılır.

cityName = "istanbul"

print(cityName.capitalize())

## diğer metodlarda olduğu gibi "i" ve "ı" harflerinde sıkıntılar var onları da aşağıdak gibi aşabiliriz

if cityName.startswith("i"):
    cityName = "İ" + cityName[1:]
elif cityName.startswith("i"):
    cityName = "I" + cityName[1:]

print(cityName.capitalize())


