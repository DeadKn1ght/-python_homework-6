# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a1 = int(input('Input first element of your array :'))
d = int(input('Input difference of elements in your array :'))
n = int(input('Input lenght of your array :'))
list_1 = []
for i in range(n):
    list_1.append(a1 + i * d)

print(f'Your arrays is : {list_1}')
