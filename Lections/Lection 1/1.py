# print("Hello Мир")

# Переменные (int, float, boolean, str, list, None и другие)

# value = None
# a = 123
# b = 1.23
# s = 'Hello "Мир"'

# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(value)
# print(type(value))
# print(s)
# print(type(s)) # Комментарии

# print(a,'-',b,'-', s)
# print('{0} - {0} - {0}'.format(a,b,s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)
# print(f + f)
# array = ['1', '2', '3', '4','5', 'hello word', True]
# print(array)

# a = int(input('Введите а: '))
# b = int(input('Введите b: '))
# print(a, '+', b, '=', a + b)
# print('{} + {} = {}'.format(a, b, a + b))
# print(f'{a} + {b} = {a + b}')

# a = float(input('Введите а: '))
# b = float(input('Введите b: '))
# print(a, '+', b, '=', a + b)
# print('{} + {} = {}'.format(a, b, a + b))
# print(f'{a} + {b} = {a + b}')

# Арифметические операции +, -, *, /, //,**, %

# a = 1.3
# b = 3
# print(round(a * b))

# a = 5
# a += 5
# print(a)

# c = 1
# b = 4
# e = 123

# a = 5 < 9 < 3 < 19
# print(a)

# print(c < b < e)


# f = 1 > 2 or 4 < 6

# print(f)

# f = [1, 2, 3, 4, 5, 6]
# print(" " in f)
# is_odd = not f[0] % 2 == 0
# print(is_odd)


# a = int(input("Введите число а: "))
# b = int(input("Введите число b: "))

# def get_max_number():
#     return a > b

# if get_max_number() == 1:
#     print(f"{a} больше, чем {b}")
# else:
#     print(f"{b} больше, чем {a}")


# original_number = int(input("Введите число: "))
# inverter_number = 0

# while original_number != 0:
#     inverter_number = inverter_number * 10 + (original_number % 10)
#     original_number //= 10
# else:
#     print("Пожалуй")
#     print("хватит")

# print(inverter_number)

# text = ""
# for i in range(7):
#     text = text + str(i) + ", "
    
# print(text)



# text = "съешь ещё этих мягких французских булок"

# # print(len(text))
# # print("ещё" in text)
# # print(text.isdigit())
# # print(text.islower())
# # print(text.replace('ещё', 'ЕЩЁ'))

# print(text[0])
# print(text[::-1])

# def f(x):
#     if type(x) == 1:
#         return "Целое"
#     elif type(x) == 1.0:
#         return 23
#     else:
#         return
    
# arg = 2.9
# print(f(arg))