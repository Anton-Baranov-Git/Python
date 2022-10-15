# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.



import random


def input_num():
    while True:
        try:
            n = int(input("Введите длину списка: "))
            return n
        except:
            print("Неправильный ввод, попробуйте снова")
            

def create_random_lst(size):
    lst = []
    while True:
        try:
            iMin = int(input("Введите минимальное рандомное число: "))
            iMax = int(input("Введите максимальное рандомное число: "))
            break
        except:
            print("Неправильный ввод, попробуйте снова")
  
    for i in range(size):
        lst.append(random.randint(iMin, iMax))
    return lst


def sum_pair_number(lst):
    current = 1
    new_lst = []
    for i in range(int(len(lst) / 2 + 1)):
        new_lst.append(lst[i] * lst[-current])
        current += 1
    return new_lst
        


my_lst = create_random_lst(input_num())
print(my_lst)
print(sum_pair_number(my_lst))

