import sys

# split() metodu -> bu method bize seçilen karakter dizisindeki kelimeleri ayırarak bir diziye atar
# Her kelime dizinin bir indeksine yerleştirilir.

uniName = "İstanbul Üniversitesi"

for i in uniName.split():
    print(i[0], end="")

print()

for i in "Türkiye Büyük Millet Meclisi".split():
    print(i[0], end="")

# split metodunu parametresiz yazdığımızda girilen karakter dizisini bölerken boşlukları kullanıyor.
# eğer biz boşluklar yerine faklı bir karaktere göre bölme işlemi yapmak istiyorsak ;;;
# mesela , gibi bir karakter
# o zaman parametremiz şu şekilde

print()

ilceler = "Alanya, Finike, Manavat, Serik, Gazipaşa, Kaş, Kemer"

for i in ilceler.split(", "):
    print(i)

# split metoduna ait ikinci parametre ise 'kaç kez bölme işlemi yapılacağıdır' mesela 2
# Verilen parametereye göre karşılaşılan ilk 2 seferde bölme işlemi yapar . daha sonrakilerde ayırma işlemi yapmaz
print()

for i in ilceler.split(", ", 2):
    print(i)

# split komutu ile sürüm kontrolü nasıl yapılır?

version = sys.version.split()

print(version[0])

# split() metodu karakter dizisini soldan sağa doğru okur.
# RSPLİT() metodunda ise fark şudur. -> Karakter dizisini sağdan sola doğru olur.

paragraph ="""A paragraph is a self-contained unit of a discourse in writing dealing with a particular point or idea. 
A paragraph consists of one or more sentences. Though not required by the syntax of any language,
paragraphs are usually an expected part of formal writing, used to organize longer prose."""

print(paragraph.splitlines(True))

#splitlines metodu ise girlen karakter dizisini satır satır ayırma yapar
#aprametre olarak true-false girilebilir bu parametre her satırın sonuna "\n" eklemesi yapar

