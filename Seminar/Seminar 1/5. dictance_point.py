# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.

while True:
    try:
        X1 = float(input("Введите первую кординату X: "))
        X2 = float(input("Введите вторую кординату X: "))
        Y1 = float(input("Введите первую кординату Y: "))
        Y2 = float(input("Введите вторую кординату Y: "))
        break
    except:
        print("Неправильный ввод, попробуйте снова")


def get_distance(x_1, x_2, y_1, y_2):
    distance = (((y_1 - x_1) ** 2) + ((y_2 - x_2) ** 2)) ** (0.5) 
    distance = int(distance * 100)
    distance = float(distance / 100)
    print(distance)
    
get_distance(X1, X2, Y1, Y2)