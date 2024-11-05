immutable_var = tuple([1, 2, True, 'well'])
# immutable_var[1] = 'good' - 'tuple' object does not support item assignment
print(immutable_var)


mutable_list = [1, 2, True, 'well']
mutable_list[1] = 'good'
mutable_list.remove('well')
mutable_list.append(False)
print(mutable_list)