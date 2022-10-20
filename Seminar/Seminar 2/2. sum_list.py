# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def input_num():
    while True:
        try:
            n = int(input("Введите число: "))
            return n
        except:
            print("Неправильный ввод, попробуйте снова")
        
        
def sum_list(num):
    lst = []
    res = 1
    for i in range(1,num + 1):
        res = res * i
        lst.append(res)
    return lst
        
        
    
print(sum_list(input_num()))