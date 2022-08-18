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

    a = float(input("Введите значение А "))
    1 / a
    b = float(input("Введите значение B "))
    c = float(input("Введите значение C "))

    return a, b, c


def main(a:float, b:float, c:float):
    '''Ф-ция'''
    try:
       float(a)
       float(b)
       float(c)
       1/a

    except Exception as e:
        print(str(e).split(":")[0])
        return str(e).split(":")[0]

    D = discrim(a, b, c)
    if D < 0:
        return "negative discriminant"

    elif D == 0:
        x1 = x2 = quadratic(a, b, D)

    elif D > 0:
        x1 = quadratic(a, b, D)
        x2 = quadratic(a, b, D, znak="")


    return (x1, x2)


if __name__ == "__main__":
    while True:
        break
        try:
            a, b, c = input_data()

        except ZeroDivisionError:
            print("Ошибка : А=0")
        except ValueError:
            print("Ошибка : Введено не число")
        else:

            break

    result = main('ff', 1, 1)
    #result = main(a, b, c)
    print(result)


