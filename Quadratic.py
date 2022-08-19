class Quadratic:
    '''решение квдратных уравнений'''

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def discrim(self, a, b, c: float) -> float:
        return (b ** 2) - 4 * a * c

    def quadratic(self, a, b, D, znak: bool = None):
        '''Если передан знак, то знак = "+", иначе "-" '''
        if not znak is None:
            znak = "+"
        else:
            znak = "-"
        chislitel = eval(f" -{b} {znak} sqrt({D})")
        znamenatel = 2 * a
        return chislitel / znamenatel


