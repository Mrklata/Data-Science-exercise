class Rectangle(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def circuit(self):
        rec_circuit = self.a + self.b
        return rec_circuit

    def area(self):
        p = self.a * self.b
        return p


class Check(Rectangle):
    def is_a_square(self):
        if self.a == self.b:
            return True
        else:
            return False


check = Check(10, 11)
rectangle = Rectangle(10, 25)

print(rectangle.circuit())
print(check.is_a_square())
