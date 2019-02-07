#Created by Ertuğrul Gazi AKÇA at 15.01.2019


#use this method to copy a list without reference


list1 = list()

list1.append("ders1")

list2 = list1.copy() #just value not reference

list1[0] = "ders1change" #list2 dont change

print(list2) # ders1


