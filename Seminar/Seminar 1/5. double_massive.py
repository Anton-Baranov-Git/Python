"""
Задача 5 VERY HARD SORT необязательная
Задайте двумерный массив из целых чисел. Количество строк и 
столбцов задается с клавиатуры. Отсортировать элементы по
возрастанию слева направо и сверху вниз."""

import random

while True:
    try:
        size_i = int(input("Введите количество строк, массива: "))
        size_j = int(input("Введите количество столбцов, массива: "))
        break
    except:
        print("Ошибка ввода, введите количество строк")


def input_number_array(): # создаем
    mas = []
    for i in range(size_i):
        mas.append([0] * size_j)
        for j in range(size_j):
            mas[i][j] = random.randint(10, 99)

    return mas


def split_mas(mas): # соединяем массив
    new_mas = []
    for i in range(size_i):
        for j in range(size_j):
            new_mas.append(mas[i][j])
    return new_mas


def sort_mas(mas): # сортируем
    for i in range(0, len(mas) - 1):
        for j in range(len(mas) - 1):
            if (mas[j] > mas[j + 1]):
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
    return mas


def join_mas(mas): # разъеденяем
    new_mas = []
    count = 0
    for i in range(size_i):
        new_mas.append([0] * size_j)

    for i in range(size_i):
            for j in range(size_j):
                new_mas[i][j] = mas[count]
                count += 1
            
    return (new_mas)

def show_mas(mas):
    for i in range(0, len(mas)):
        for i2 in range(0, len(mas[i])):
            print(mas[i][i2], end=' ')
        print()
        



my_mas = input_number_array()
print("Случайный массив: ")
show_mas(my_mas)
print()
print("Сортированный массив: ")
show_mas(join_mas(sort_mas(split_mas(my_mas))))



