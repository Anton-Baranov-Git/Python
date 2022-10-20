# Вычислить число PI c заданной точностью d
from math import pi


def input_number():
    while True:
        try:
            d = int(input('Введите точность определения числа ПИ (количество знаков после запятой): '))
            return d
        except:
            print('Ошибка ввода, попробуйте еще раз')
            



def number_PI(d):
    PI = 0
    for i in range(1, d * 2 ** 22):
        PI = PI + 4 * ((-1) ** (i + 1)) / ( 2 * i - 1)
    print(f"Число ПИ равно = {round(PI, d)}")


diametr = input_number()
print(f"Число ПИ равно = {round(pi, diametr)} - способ с библиотекой")  # Я не мог не сделать так :)
number_PI(diametr)

# от 1 до 7 считает довольно быстро, далее теряеться точность, нужно повышать степень
