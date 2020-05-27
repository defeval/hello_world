# присваивание кортежа
t = [(1, 2), (3, 4), (5, 6)]
for (a, b) in t:
    print(a, b)

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, '=>', d[key])

d = {'a': 1, 'b': 2, 'c': 3}
for (key, value) in d.items():
    print(key, value)

# извлечение среза
s = 'a1s2d3f4g5h6j7k8l'
for i in s[::2]:
    print(i, end='')

