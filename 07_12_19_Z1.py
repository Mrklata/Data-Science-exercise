from random import randint


def open_file():
    with open("./dictionary") as file:
        file_read = file.read()
    return file_read


def create_dictionary():
    file_read = open_file()
    file_split = file_read.replace("- ", ", ")
    file_split = file_split.split(", ")
    dictionary = {}
    question = []
    for i in range(0, len(file_split), 2):
        dictionary[file_split[i]] = file_split[i + 1]
        question.append(file_split[i])
    return dictionary, question


def main():
    dictionary = create_dictionary()[0]
    question = create_dictionary()[1]
    right_answers = 0
    for i in range(10):
        i = randint(0, len(question) - 1)
        print(question[i])
        temp = dictionary[question[i]]
        answer = str(input('answer = '))
        if str(temp) == answer:
            print("You are correct!!!")
            right_answers += 1
        else:
            print(f"Wrong, answer is {dictionary.get(question[i])}!!!")
    print(f"You answered {right_answers} out of 10 questions")


if __name__ == '__main__':
    main()
