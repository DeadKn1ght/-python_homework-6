# Задача 32: Определить индексы элементов массива
# (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше
# заданного максимума)
array = []
lenght = int(input('Input array lenght :'))
print('Input your array elements :')
for i in range(lenght):
    array.append(int(input()))

print(f'Your array is : {array}')

min = int(input('Input diapason minimun :'))
max = int(input('Input diapason maximun :'))
print('The indexes of elements in your array in this diaposon are :')
for i in range(len(array)):
    if min <= array[i] <= max:
        print(i)
