from math import factorial


def check():
    n = int(input("Input n"))
    k = int(input("Input k"))
    result = factorial(n)/(factorial(k) * (factorial(n - k)))
    return result


print(check())