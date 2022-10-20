# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.

def input_number():
    lst = []
    while True:
        try:
            size = int(input("Введите длину массива: "))
            for i in range(size):
                lst.append(int(input(f"Введите число {i + 1}: ")))
            return lst
        except:
            print('Ошибка ввода, попробуйте еще раз')
        
        
# самый простой способ для вывода уникального списка, если так интерпретировать задачу

def lst_tpl(lst):
    lst = list(set(lst))
    return lst



# если выводить только уникальные значения из списка

def no_repeat_lst(lst):
    my_lst = []
    for i in lst:
        repeat_number = i  
        count_n = 0
        for j in lst:
            if i == j:
                count_n += 1
        if count_n < 2:
            my_lst.append(i)
    return my_lst
            
my_lst = input_number()
print()
print(f'Введенный массив: {my_lst}')
print()
print(f'Только уникальные значения массива: {no_repeat_lst(my_lst)}')

# Чувствую есть более лакончиное решение



# Подглядев понял, что можно проверять последоватльеность вот так:

def no_repeat_lst_2(lst):
    my_lst = []
    for char in lst:
        if lst.count(char) < 2:
            my_lst.append(char)
    return my_lst


print()
print(f'Только уникальные значения массива вторая версия: {lst_tpl(my_lst)}')
print()
print(f"Список из неповторяющихся элементов: {no_repeat_lst_2(my_lst)}")
print()