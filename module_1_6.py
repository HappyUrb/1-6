# словари
my_dict = {'Яблоки': 4267, 'Бананы': 3464}
print (my_dict)
print (my_dict ['Яблоки'], my_dict.get('Арбузы'))
my_dict.update({'Мандарина': 5245,
               'Персики': 6346})
del_ = my_dict.pop ('Бананы')
print (del_)
print (my_dict)
# Множества
my_set = {1, 1, 2, 2, 3, 3}
print (my_set)
my_set.add ('Стол')
my_set.add ((1, 2, 3))
my_set.discard(1)
print (my_set)