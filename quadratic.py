import random
from math import sqrt
from random import randint, sample
class Quadratic:
    '''решение квдратных уравнений'''
    __list_obj = []
    __list_res = []

    @classmethod
    def get_list(cls):

        return Quadratic.__list_res

    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
        self.D = None
        self.x1 = None
        self.x2 = None
        self.error = None
        Quadratic.__list_obj.append(self)

    def __str__(self):
        return str(vars(self))

    def check(self):
        try:
            float(self.a)
            1/self.a
            float(self.b)
            float(self.c)
        except ValueError:
            self.error = "ValueError"
        except ZeroDivisionError:
            self.error = "ZeroDivisionError"
        else:
            self.error = None

    def discrim(self):
        self.D = (self.b ** 2) - 4 * self.a * self.c
        if self.D < 0:
            self.error = "negative discriminant"
        else:
            self.error = None
        return self.D

    def quadratic(self, znak = None):
        '''Если передан знак, то знак = "+", иначе "-" '''
        if not znak is None:
            znak = "+"
        else:
            znak = "-"
        s = sqrt(self.D)
        chislitel = eval(f" -{self.b} {znak} {s}")
        znamenatel = 2 * self.a
        return round(chislitel / znamenatel, 2)


    def run(self):
        self.check()
        if self.error is None:
            self.discrim()

        if self.error is None and self.D == 0:
            self.x1 = self.x2 = self.quadratic()

        elif self.error is None and self.D > 0:
            self.x1 = self.quadratic()
            self.x2 = self.quadratic(znak="")

        Quadratic.__list_res.append(vars(self))



if __name__ == "__main__":
    for _ in range(10):
        rl = sample(range(-10, 10), 3)
        u1 = Quadratic(*rl)
        u1.run()
    #print(Quadratic.get_list())
    [print(str(i) + "\n" + "-"*100) for i in Quadratic.get_list()]

    #Quadratic.get_list()



