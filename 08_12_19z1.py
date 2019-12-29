import math


class Ulamek(object):
    def __init__(self, licz, mian, licz_2, mian_2):
        self.licz = licz
        self.mian = mian
        self.licz_2 = licz_2
        self.mian_2 = mian_2
        self.licz_s = None
        self.mian_s = None
        self.licz_2s = None

    def skroc(self):

        dzielnik = math.gcd(self.licz, self.mian)
        dzielnik_2 = math.gcd(self.licz_2, self.mian_2)

        self.licz_2 = int(self.licz_2 / dzielnik_2)
        self.mian_2 = int(self.mian_2 / dzielnik_2)

        self.licz = int(self.licz / dzielnik)
        self.mian = int(self.mian / dzielnik)
        self.licz_s = self.licz * self.mian_2
        self.licz_2s = self.licz_2 * self.mian
        self.mian_s = self.mian * self.mian_2

        return f"{self.licz}/{self.mian}", f"{self.licz_2}/{self.mian_2}"

    def dodaj(self):
        return f"{self.licz_2s + self.licz_s}/{self.mian_s}"

    def odejmij_1_2(self):
        licz = self.licz_s - self.licz_2s
        return f"{licz}/{self.mian_s}"

    def odejmij_2_1(self):
        licz = self.licz_2s - self.licz_s
        return f"{licz}/{self.mian_s}"

    def mnoz(self):
        self.skroc()
        return f"{self.licz * self.licz_2}/{self.mian * self.mian_2}"

    def dziel_1_2(self):
        self.skroc()
        return f"{self.licz * self.mian_2}/{self.licz_2 * self.mian}"

    def dziel_2_1(self):
        self.skroc()
        return f"{self.licz_2 * self.mian}/{self.licz * self.mian_2}"


ulamek = Ulamek(2, 4, 1, 3)

print(ulamek.skroc())
print(ulamek.dodaj())
print(ulamek.mnoz())
print(ulamek.odejmij_1_2())
print(ulamek.odejmij_2_1())
print(ulamek.dziel_1_2())
print(ulamek.dziel_2_1())
