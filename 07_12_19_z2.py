def change_to_number(number):
    num_ready = number.split()
    dictionary = {'jeden': 1, 'dwa': 2, 'trzy': 3, 'cztery': 4, 'pięć': 5,
                  'sześć': 6, 'siedem': 7, 'osiem': 8, 'dziewięć': 9, 'dziesięć': 10,
                  'jedynaście': 11, 'dwanaście': 12, 'trzynaście': 13, 'czternaście': 14,
                  'piętnaście': 15, 'szesnaście': 16, 'siedemnaście': 17, 'osiemnaście': 18,
                  'dziewiętnaście': 19, 'dwadzieścia': 20, 'trzydzieśći': 30,
                  'czterdzieści': 40, 'pięćdziesiąt': 50}
    temp = 0
    for i in num_ready:
        if i in dictionary:
            temp += int(dictionary[i])
    print(temp)
    print(type(temp))


change_to_number('dwadzieścia dwa')
