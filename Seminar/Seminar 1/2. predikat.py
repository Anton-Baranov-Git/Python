# задача 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def input_num(x):
    xyz = ["X", "Y", "Z"]
    mas = []
    for i in range(x):
        while True:
            try:
                mas.append(int(input(f"Введите значение {xyz[i]}: ")))
                break
            except:
                print("Неправильный ввод, попробуйте снова")
            
    return mas

def Predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

number = input_num(3)

if Predicate(number) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")