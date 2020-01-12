def fib(num_1, num):
    if num_1 > num:
        raise ValueError('First number must be bigger')
    else:
        suma = sum([i for i in range(num_1, num + 1)])
        print(suma)
    pass


def check():
    try:
        num_1 = int(input('Input start number'))
        num = int(input('Input end number'))
        print(fib(num_1, num))

    except ValueError as x:
        print(x)


if __name__ == '__main__':
    check()
