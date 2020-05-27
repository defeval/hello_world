a = [1, 2, 3]
b = [4, 5, 6]
l = list(zip(a, b))
print(l)

for (x, y) in zip(a, b):
    print('{} + {} = {}'.format(x, y, x + y))


# создание словаря
d = dict(zip(a, b))
print(d)

