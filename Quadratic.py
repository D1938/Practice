class Quadratic:
    '''решение квдратных уравнений'''

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

    def input_data(self):
        '''получение данных от пользователя'''
        print("Введите данные: ")

        a = float(input("Введите значение А "))
        1 / a
        b = float(input("Введите значение B "))
        c = float(input("Введите значение C "))

        return a, b, c

