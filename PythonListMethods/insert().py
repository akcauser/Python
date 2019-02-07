#Created by Ertuğrul Gazi AKÇA at 15.01.2019

#insert metodu listenin herhangi bir yerine bir eleman eklemek için kullanılır.
#append metodundan farkı eklemek istediğimiz indexi kenidimiz seçiyor olmamızdır

#this metod like append method. But we tell to program which index of list we want to add

list1 = []
list1.insert(0,"ders1")

print(list1)

list1.insert(1,"ders2")

print(list1)

list1.insert(0,"ders1change")

print(list1)