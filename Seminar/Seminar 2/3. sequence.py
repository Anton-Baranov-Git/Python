# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

def input_num():
    while True:
        try:
            n = int(input("Введите число: "))
            return n
        except:
            print("Неправильный ввод, попробуйте снова")
            
            
def sequence_number(n):
    lst = []
    for i in range(1, n + 1):
        num = ((1 + 1 / i) ** i)
        lst.append(round(num,2))
    return lst
    
print(sequence_number(input_num()))

