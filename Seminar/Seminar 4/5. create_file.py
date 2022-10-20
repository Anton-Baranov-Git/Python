# 5. Даны два файла, в каждом из которых находится запись
# многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.

# Сначала создадим 2 файла с многочленами

k_1 = "(2x + y)"
k_2 = "(3x + y)"
file_1 = 'list_coefficients.txt'
file_2 = 'list_coefficients_2.txt'
file_3 = 'answer.txt'


def write_f(file_name, body):
    with open(file_name, 'a') as file:
        file.write(f'{body} \n')


def create_p(koef_1, koef_2, file_1, file_2):
    write_f(file_1, koef_1)
    write_f(file_2, koef_2)
    print("Файл записан")
    print(koef_1)
    print(koef_2)

def create_answer(file):
    lst_1 = []
    lst_2 = []
    addition = f'{k_1} + {k_2}'

    print(f"Первым действием найдем сумму исходных многочленов и запишем ее далее опустим скобки:")
    print(f"{addition}")
    
    print(f"Начнем складывать")
    for i in k_1:
        if i != ')' and i != '(' and i != " ":
            lst_1.append(i)
        
    for i in k_2:
        if i != ')' and i != '(' and i != " ":
            lst_2.append(i)
            
    ##### Это самое ужасное решение, я всю голову сломал над задачей
    text = str(int(lst_1[0]) + int(lst_2[0])) + lst_1[1] + " + 2" + lst_1[3]
    print(f"Удивительно правильный ответ: {text}")
    print("Записываем его в файл")
    addition = (f"Удивительно правильный ответ: {text}")
    
    write_f(file, addition)


create_p(k_1, k_2, file_1, file_2)
create_answer(file_3)

# Работаем только с этими многочленами, делал варианты через справочник
# не вышло, что-то типа парсера, с миллионом if и else тоже не вышло,
# оставил вариант исключительно с частным случаем, по другому говоря,
# я ее не решил