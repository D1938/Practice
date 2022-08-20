import sys
from Quadratic import Quadratic


def input_data():
    '''получение данных от пользователя'''
    print("Введите данные: ")

    a = float(input("Введите значение А "))
    1 / a
    b = float(input("Введите значение B "))
    c = float(input("Введите значение C "))

    return a, b, c

def main(a ,b, c):
    '''Ф-ция'''
    try:

        raschet = Quadratic(a, b, c)

    except Exception as e:
        print(str(e).split(":")[0])
        return str(e).split(":")[0]

    raschet.discrim()
    if D < 0:
        return "negative discriminant"

    elif D == 0:
        x1 = x2 = raschet.discrim(a, b, D)

    elif D > 0:
        x1 = raschet.quadratic(a, b, D)
        x2 = raschet.quadratic(a, b, D, znak="")


    return (x1, x2)


if __name__ == "__main__":
        key = input("Произвести расчет? y/n ")
        while True:

            if key == "y":
                try:
                    result = main(*input_data())
                    print(result)

                    key = input("Расчитать еще одно уравнение? y/n ")
                    if key == "n":
                        print("Программа завершила свою работу")
                        sys.exit()

                except ZeroDivisionError:
                    print("Ошибка : А=0")
                except ValueError:
                    print("Ошибка : Введено не число")

            else:
                break





