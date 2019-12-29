def file_creator(num):
    dictionary = {}
    with open("./dictionary.txt", "w+") as file:
        for i in range(num):
            polish_word = input("Polish word")
            english_word = input("English word")
            dictionary[polish_word] = english_word
        file.write(str(dictionary))


if __name__ == '__main__':
    file_creator(3)
