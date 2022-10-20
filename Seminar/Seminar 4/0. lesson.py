# _______________________________________________________________________________________________
# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

def input_number():
    lst = []
    lst = list(map(int, input("Введите числа через пробел: ").split()))
    return lst


def maximum_minimum_number_lst(lst):
    i_min = lst[0]
    i_max = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > i_max:
            i_max = lst[i]
        if lst[i] < i_min:
            i_min = lst[i]
    print(f"Максимальное число: {i_max}")
    print(f"Минимальное число: {i_min}")


maximum_minimum_number_lst(input_number())

# _______________________________________________________________________________________________

# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python

# while True:
#     try:
#         num_A = int(input("Введите число A: "))
#         num_B = int(input("Введите число B: "))
#         num_C = int(input("Введите число C: "))
#         if num_A == 0:
#             print('А должен быть больше 0, введите еще раз')
#         else:
#             break
#     except:
#         print('Ошибка ввода, попробуйте еще раз')


# def exp(num_1, num_2, num_3):
#     des = num_B ** 2 - 4 * num_C * num_A
#     x = (- num_B + des ** 0.5) / (2 * num_A)
#     x2 = (- num_B - des ** 0.5) / (2 * num_A)

#     if des < 0:
#         print("Корней нет")
#     elif des == 0:
#         print(f"Корень один равен: {x}")
#     else:
#         print(f"Первый корень: {x}")
#         print(f"Второй корень: {x2}")


# exp(num_A, num_B, num_C)


# _______________________________________________________________________________________________
# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# while True:
#     try:
#         num_A = int(input("Введите число A: "))
#         num_B = int(input("Введите число B: "))
#         break
#     except:
#         print('Ошибка ввода, попробуйте еще раз')


# def multiple_all_number(num_1, num_2):
#     for i in range(1, max(num_1,num_2, )):
#         if num_1 % i == 0 and num_2 % i == 0:
#             return i
#         else:
#             return -1

# nod = multiple_all_number(num_A, num_B)

# if nod > 0:
#     print(f"НОK равен: {(num_A * num_B) / nod}")
# else:
#     print(f"НОK равен: {num_A * num_B}")


# _______________________________________________________________________________________________
