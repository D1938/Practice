class Quadratic:
    '''решение квдратных уравнений'''

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.D = None
#self.x1, self.x2, self.error

    def discrim(self) -> float:
        self.D = (self.b ** 2) - 4 * self.a * self.c
        return self.D

    def quadratic(self, a, b, D, znak = None):
        '''Если передан знак, то знак = "+", иначе "-" '''
        if not znak is None:
            znak = "+"
        else:
            znak = "-"
        chislitel = eval(f" -{b} {znak} sqrt({D})")
        znamenatel = 2 * a
        return chislitel / znamenatel

if __name__ == "__main__":
    u1 = Quadratic(1,0,1)
    print(u1.D)
    u1.discrim()
    print(u1.D)
    print("-"*100)
