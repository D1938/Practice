from math import sqrt as sqrt



def discrim(a, b, c: float) -> float:
    return (b ** 2) - 4 * a * c

def quadratic(a, b, D, znak:bool=None):
    '''Если передан знак, то знак = "+", иначе "-" '''
    if not znak is None:
        znak = "+"
    else:
        znak = "-"
    chislitel = eval(f" -{b} {znak} sqrt({D})")
    znamenatel = 2 * a
    return chislitel / znamenatel




def input_data():
    '''получение данных от пользователя'''
    print("Введите данные: ")
    while True:
        try:
            a = float(input("Введите значение А "))
            1 / a
            b = float(input("Введите значение B "))
            c = float(input("Введите значение C "))
        except ZeroDivisionError:
            print("Ошибка : А=0")
        except ValueError:
            print("Ошибка : Введено не число")
        else:

            break
    return a, b, c


def main(a, b, c: float):

    error = None
    D = discrim(a, b, c)
    if D < 0:
        error = "уравнение не имеет корней!"
    elif D == 0:
        x1 = x2 = quadratic(a, b, D)

    elif D > 0:
        x1 = quadratic(a, b, D)
        x2 = quadratic(a, b, D, znak="")
    if error:
        return error
    else:
        return (x1, x2)


if __name__ == "__main__":
    a,b,c = input_data()
    result = main(a,b,c)
    print(result)


