# Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.

# while True:
#     try:
#         number1 = int(input("Введите первое число: "))
#         number2 = int(input("Введите второе число: "))
#         if number2 < number1:
#             number1, number2 = number2, number1
#         break
#     except:
#         print("Неправильный ввод, попробуйте снова")



# def check_square():
#     if number1 * number1 == number2 or number2 * number2 == number1:
#         print(f"Число '{number1}' является квадратом числа '{number2}'")
#     else:
#         print(f"Число '{number1}' не является квадратом числа '{number2}'")
        
# check_square()


# Напишите программу которая принимает на
# вход 5 чисел и находит максимальное из них

# def create_list():
#     while True:
#         some_list = []
#         try:
#             size = int(input("Сколько чисел будете вводить: "))
#             for i in range(size):
#                 number = int(input(f"Введите число {i+1}: "))
#                 some_list.append(number)
#             break
#         except:
#             print("Неправильный ввод, попробуйте снова")
#     return some_list

# def max_number(listt):
#     maxx = listt[0]
#     for i in range(len(listt)):
#         if listt[i] > maxx:
#             maxx = listt[i]
#     print(f"Максимальное число будет: {maxx}")


# max_number(create_list())

# Напишите программу которая будет принимать на вход число N и выводить числа от -N до N

# while True:
#     try:
#         n = int(input("Введите число N: "))
#         break
#     except:
#         print("Неправильный ввод, попробуйте снова")

# def show_n():
#     text = ""
#     for i in range(-n, n+1):
#         text = text + str(i) + " "
#     print(text)
        
# show_n()

# Напишите программу которая будет принимать на вход дробь и показывать первую цифру дробного числа

# while True:
#     try:
#         fnumber = float(input("Введите дробное число: "))
#         break
#     except:
#         print("Неправильный ввод, попробуйте снова")
        
# def get_num(num):
#     if num - int(num) == 0:
#         print("Нет знаков после запятой")
#     else:
#         num = (num - int(num)) * 10
#         print(f"Первая цифра после запятой: '{int(num)}'")

# get_num(fnumber)

# Напишите программу которая принимает на вход число которое проверяет, кратно ли оно 5, 10, 15 но не 30

# while True:
#     try:
#         number = int(input("Введите число: "))
#         break
#     except:
#         print("Неправильный ввод, попробуйте снова")
        
# def numberr(num):
#     if (num % 5 == 0 or num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
#         print(f"Число '{num}' кратно 5 или 10 или 15 но не 30")
#     else:
#         print(f"Число '{num}' не соблюдает данные условия")
        
# numberr(number)