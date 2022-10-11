# задача 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

def input_number(): # создаем метод ввода
    while True:
        try:
            num = int(input("Введите число от 1 до 7: "))
            if num < 1 or num > 7:
                print('Ошибка ввода, попробуйте еще раз')
                continue
            return num
        except:
            print('Ошибка ввода, попробуйте еще раз')


def show_day_week(number): # показываем ответ
    if number > 5:
        print("Данный день, является выходным")
    else:
        print("Данный день, не является выходным")
        
                
show_day_week(input_number())