# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.

from random import randint

        
def input_number():
    while True:
        try:
            n = int(input("Введите натуральную степень: "))
            return n
        except:
            print('Ошибка ввода, попробуйте еще раз')

def create_mult(k):
    lst = []
    for i in range(k + 1):
        lst.append(randint(0, 101))
    return lst

def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x ** {len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}y'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

koef = create_mult(input_number())
with open('list_coefficients.txt', 'w') as file:
    file.write(create_str(koef))
    print("Файл записан")
    print(create_str(koef))

