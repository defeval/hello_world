def seq(a, b):
    res = []
    for x in a:
        if x in b:
            res.append(x)
    return res


print(seq('asd', 'asf'))

