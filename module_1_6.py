my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict['Masha']}')
print(my_dict.get('Sasha'))
my_dict.update({'Ksmala': 1981, 'Artem': 1915})
print(my_dict)
a = my_dict.pop('Egor')
print(a)