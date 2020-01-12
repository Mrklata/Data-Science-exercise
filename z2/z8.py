from math import factorial as fc


def foo(n):
    a = []
    for x in range(1, n+2):
        a.append(int((fc(n)) / (fc(n-(x-1)) * fc(x - 1))))
    return a


print(foo(5))
