from math import sqrt as sqrt

from Quadratic import Quadratic

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

    D = schetovod.discrim(a, b, c)
    if D < 0:
        return "negative discriminant"

    elif D == 0:
        x1 = x2 = schetovod.discrim(a, b, D)

    elif D > 0:
        x1 = schetovod.quadratic(a, b, D)
        x2 = schetovod.quadratic(a, b, D, znak="")


    return (x1, x2)


if __name__ == "__main__":
    schetovod = Quadratic()
    while True:

        try:
            a, b, c = schetovod.input_data()

        except ZeroDivisionError:
            print("Ошибка : А=0")
        except ValueError:
            print("Ошибка : Введено не число")
        else:

            break

    #result = main(1, 1, 1)
    result = main(a, b, c)
    print(result)


