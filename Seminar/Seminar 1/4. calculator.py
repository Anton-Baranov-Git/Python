""" задача 4 HARD необязательная Напишите простой калькулятор, который считывает с
пользовательского ввода три строки: первое число, второе число и операцию, после чего
применяет операцию к введённым числам (первое число" "операция" "второе число) и
выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку 'Деление на 0!'.

Обратите внимание, что на вход программе приходят вещественные числа."""


number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

def ActionNumber(num1, num2):
    while True:
        action = input("Какое действие будем производить: ")
        if action == "+":
            print(f'{num1} + {num2} = {num1 + num2}')
            break
        elif action == "-":
            print(f'{num1} - {num2} = {num1 - num2}')
            break
        elif action == "/":
            if number2 == 0:
                print("На нуль делить нельзя, попробуйте снова")
            else:
                print(f'{num1} / {num2} = {num1 / num2}')
                break
        elif action == "*" or action == "x":
            print(f'{num1} * {num2} = {num1 * num2}')
            break
        elif action == "mod" or action == "//":
            if number2 == 0:
                print("На нуль делить нельзя, попробуйте снова")
            else:
                print(f'{num1} // {num2} = {num1 // num2}')
                break

        elif action == "pow" or action == "**":
            print(f'{num1} ** {num2} = {num1 ** num2}')
            break
        elif action == "div" or action == "%":
            print(f'{num1} % {num2} = {num1 % num2}')
        else:
            print("Ввели неверное значение")


ActionNumber(number1, number2)
