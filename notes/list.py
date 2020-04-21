# Списки - упорядочные коллекции объектов произвольных типов
# Доступ к элементам по смещению
# Переменная длина, гетерогенность и произвольное число уровней вложенности
# Относятся к категории изменяемых объектов
# Массивы ссылок на объекты

some_list = []  # Пустой список
print(some_list)  # Return []

some_list = [0, 1, 2, 3]  # 4 элемента с индексами 0-3
print(some_list)  # Return [0, 1, 2, 3]

some_list = ['abc', ['def', 'ghi']]  # Вложенные объекты
print(some_list, '\n', some_list[1][1])

some_list = list('spam')  # Создание списка из итерируемого объекта
print(some_list)  # Return ['s', 'p', 'a', 'm']

some_list = list(range(-8, 8, 2))  # Создание списка из непрерывной последовательности
print(some_list)  # Return [-8, -6, -4, -2, 0, 2, 4, 6]

some_list = ['abc', ['def', 'ghi'], 14]
print(some_list[1], '|', some_list[1][1], '|', some_list[:1])  # Return ['def', 'ghi'] | ghi | ['abc']

print(len(some_list))  # List length

my_list = [12, 14, 1.25]

print(some_list + my_list)  # Return ['abc', ['def', 'ghi'], 14, 12, 14, 1.25]

print(some_list * 3)

for x in some_list:
    print(x)

some_list.append(4)  # append to last? if some_list.append([4]) -  вставил лист 4 как лист
print(some_list)

some_list.extend([5, 5, 7])  # extend, принимает на вход лист
print(some_list)

some_list.insert(1, 'New Second Element')  # добавление в список
print(some_list)

print(some_list.index('abc'))  # if in list return index, else except
print(some_list.count(5))  # Подсчитает количество объекто в списке

non_sorted_list = [5, 7, 1, 8]
non_sorted_list.sort()  # отсортирует, если объекты можно отсортеровать
print(non_sorted_list)

non_sorted_list.reverse()  # реверс листов
print(non_sorted_list)

print(non_sorted_list.pop())  # Delete and return last element
print(non_sorted_list)

print(non_sorted_list.remove(8))  # Delete element if in list, return None
print(non_sorted_list)

print(5 in non_sorted_list)  # Return true or false


my_list[0] = 13

# генераторы списков
m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

cols2 = [row[1] ** 3 for row in m if row[1] % 2 == 0]
print('cols2 = ', cols2)

diag = [m[i][i] for i in [2, 1, 0]]
print(diag)

triple = [int(c * 3) for c in '123z0.5' if c.isnumeric()]
print(triple)

g = [sum(row) for row in m]
print(g)

# Тоже генератор списка
squares = [x ** 2 for x in range(1, 6)]
print(squares)
