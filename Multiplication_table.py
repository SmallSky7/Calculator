def math1(a, b):
    return a*b

"""for i in range(1, 10):
    for j in range(i, 10):
        while j < 9:
            c = math1(i, j)
            print(i, '*', j, '=', c, end=",")
            break
        while j >= 9:
            c = math1(i, j)
            print(i, '*', j, '=', c)
            break
"""

for i in range(1, 10):
    for j in range(i, 10):
        c = math1(i, j)
        if j < 9:
            print(i, '*', j, '=', c, end=",")
        else:
            print(i, '*', j, '=', c)









