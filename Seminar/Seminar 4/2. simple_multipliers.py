# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def input_number():  # создаем метод ввода
    while True:
        try:
            n = int(input("Введите число N: "))
            return n
        except:
            print('Ошибка ввода, попробуйте еще раз')


def simple_multipliers(num):
   i = 2
   lst = []
   while i * i <= num:
       while num % i == 0:
           lst.append(i)
           num = num / i
       i = i + 1
   if num > 1:
       lst.append(int(num))
   return lst
            

print(simple_multipliers(input_number()))
