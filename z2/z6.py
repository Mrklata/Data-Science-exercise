def fib():
    num = int(input('Input fib number you would like to know'))
    temp = [1, 2]
    for i in range(num - 2):
        temp.append(temp[i] + temp[i+1])
    return temp[-1]

print(fib())