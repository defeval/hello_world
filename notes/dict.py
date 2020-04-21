# d = {'spam': 2, 'ham': 1, 'eggs': 3}
# print(d['spam'])
# print(d)
# print(len(d))
# print('ham' in d)
#
# d['ham'] = 14
# print(d)
#
# del d['spam']
# print(d)
#
# d['name'] = 'Allen'
# print(d)
#
# print(list(d.values()))
# print(list(d.keys()))
# print(list(d.items()))
#
# print(d.get('spam'))
#
# d2 = {'toast': 4, 'muffin': 5}
# d.update(d2)
# print(d)
#
# print(d.pop('muffin'))
# print(d)
#
# for food in d:
#     print(food, '\t', d[food])
#
# d = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
# print(d)
#
# # Генераторы словарей
# d = {str(x): x ** 3 for x in range(5)}
# d1 = dict.fromkeys([1, 2, 3], 50)
# print(d1)



# print()
#
# # сортировка по ключу в разборе
# key = list(d.keys())  # unsort list keys
# print(key)
#
# key.sort()
# print(key)
#
# for i in key:
#     print(i, '=>', d[i])
#
# # сортировка по ключу более простая
# for i in sorted(d):
#     print(i, '=>', d[i])
#
# print(sorted(d))
#
# if 'f' not in d:
#     print('f is not in d')
#
# d['f'] = 99
# print(sorted(d))
#
# if 'f' in d:
#     print('f in d')
#
# # get key
# value = d.get('a', 0)
# print(value)
# value = d.get('h', 0)
# print(value)





