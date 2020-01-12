from math import factorial


def iterating():
    num = int(input('Insert number'))
    temp = []
    for i in range(1, num + 1):
        temp.append(i)
    result = 1
    for i in temp:
        result = result * i
    return result


def library():
    num = int(input('Insert number'))
    result = factorial(num)
    return result


print(iterating())
print(library())
