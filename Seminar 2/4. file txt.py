# Задайте список из N элементов, заполненных числами из промежутка [-N, N]
# Найдите произведение элементов на указанных позициях. Позиции хранятся в
# файле file.txt в одной строке одно число.

import random


def create_random_number():
    text_ = open("Seminar 2/number.txt", "w")
    while True:
        try:
            number_ = int(input("Какое количество случайных чисел создать: "))
            break
        except:
            print("Неправильный ввод, попробуйте снова")

    for i in range(number_):
        text_.write(f"{str(random.randint(1, 9))}\n")
    return number_
    print("Числа созданы")

def input_num(min_num):
    while True:
        try:
            n = int(input(f"Введите длину массива, но не меньше чем {min_num}: "))
            if n < min_num:
                print("""
                      Вы ввели число меньше количества индексов,
                      массив должен быть больше, чем максимальный
                      индекс
                      """)
            else:
                return n
        except:
            print("Неправильный ввод, попробуйте снова")

def create_lst(num):
    lst = []
    for i in range(num + 1):
        number = random.randint(-num, num)
        if number == 0:
            lst.append(number + 1)
        else:
            lst.append(number)
    return lst

def multiplication(lst):
    text_ = open("Seminar 2/number.txt", "r")
    sum = 1
    for i in text_:
        print(f"Индекс позиции '{int(i)}' число в нем '{lst[int(i)]}' {sum} * {lst[int(i)]} = {sum * lst[int(i)]}")
        sum = sum * lst[int(i)]
    return sum



my_lst = (create_lst(input_num(create_random_number())))
print()
print(my_lst)
print()
print(f"\nПроизведение элементов на случайных позициях указанных в файле 'number.txt' равно '{multiplication(my_lst)}'")


# немного понесло с этой задачей, много букв, но вроде все по делу, сделал защиту от любого ввода не по делу :)
# еще немного показалось что я мог ошибиться в условиях, если так то готв исправить
