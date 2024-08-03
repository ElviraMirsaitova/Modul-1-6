my_dict = {'Elvira' : 1989, 'Rinat' : 1991}
print(my_dict)
print(my_dict['Elvira'])
my_dict ['Ruslan'] = 1979
a = my_dict.pop('Ruslan')
print(a)
my_dict ['Ruslan'] = 1979
my_dict.update({'Mama' : 1958,
                'Papa' : 1951})
print(my_dict)
del my_dict ['Papa']
print(my_dict)

my_set = {4,5,8,5,7,8,9,'Elvira',True}
print(my_set)
list_ = [3,111]
list_ = set(list_)
print(my_set.update(list_))
print(my_set.discard(8))
print(my_set)
