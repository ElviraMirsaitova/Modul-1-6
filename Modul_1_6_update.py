my_dict = {'Elvira' : 1989, 'Rinat' : 1991}     #Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение
print(my_dict)                                  #Выведите на экран словарь my_dict
print(my_dict['Elvira'])                        #Выведите на экран одно значение по существующему ключу
print(my_dict.get('Artur'))                     #Выведите на экран одно значение по отсутствующему ключу без ошибки.
my_dict.update({'Mama' : 1958,                  #Добавьте ещё две произвольные пары
                'Papa' : 1951})
print(my_dict)
del my_dict ['Papa']                            #Удалите одну из пар в словаре по существующему ключу
print(my_dict)

#множества
my_set = {4,5,8,5,7,8,9,'Elvira',True}          #Создайте переменную my_set и присвойте ей множество
print(my_set)                                   #Выведите на экран множество my_set
list_ = [3,2]                                   #Добавьте 2 произвольных элемента в множество
list_ = set(list_)
print(my_set.update(list_))
print(my_set.discard(8))                        #Удалите один любой элемент из множества
print(my_set)                                   #Выведите на экран измененное множество
