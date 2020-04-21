# # First script on python
# import sys
#
# print(sys.platform)
# print(2 ** 100)
# x = 'Spam'
# print(x * 8)
#
# s = 0
# n = 0
# while s < 111:
#     s = s + 10
#     n = n + 2
# print(n)

n = '8' * 81
while '888' in n or '777' in n:
    if '777' in n:
        n = n.replace('777', '8')
    else:
        n = n.replace('888', '7')
print(n)


def my_func():
    ...
    print('Some text')


my_func()



