# Работа со словарями
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict['Masha']}')
print(f'Not existing value: {my_dict.get('Sasha')}')
my_dict.update({'Ksmala': 1981, 'Artem': 1915})
print(f'Deleted value: {my_dict.pop('Egor')}')
print(f'Modified dictionary: {my_dict}')
# Работа с множествами
my_set = {1, 'Яблоко', 1, 42.314, 'Яблоко'}
print(f'Set: {my_set}')
my_set.update({13, (5, 6, 1.6)})
my_set.remove(1)
print(f'Modified set: {my_set}')