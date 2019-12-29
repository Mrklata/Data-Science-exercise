class Animal(object):

    def __init__(self, age, weight, name, colour=None):
        self.age = age
        self.weight = weight
        self.name = name
        self.colour = colour
        self.lion = False

    def introduce(self):
        if self.lion:
            answer = f"Hi my name is {self.name} i am {self.age} years old and i weight {self.weight} kg! And I am a lion"
        elif self.colour:
            answer = f"Hi my name is {self.name} i am {self.age} years old and i weight {self.weight} kg! And my colour is {self.colour}"
        else:
            answer = f"Hi my name is {self.name} i am {self.age} years old and i weight {self.weight} kg!"
        return answer

    def birthday(self):
        self.age += 1
        return self.age


class Lion(Animal):
    def introduce(self):
        self.lion = True
        answer = super().introduce()
        return answer


class Parrot(Animal):
    def introduce(self):
        answer = super().introduce()
        return answer


class Elephant(Animal):
    pass


lion = Lion(11, 100, 'adam')

parrot = Parrot(2, 20, 'david', 'red')

elephant = Elephant(11, 200, 'john')

animal = Animal(1, 30, 'ala')

print(animal.introduce())
print(lion.introduce())
print(parrot.introduce())
print(elephant.introduce())
