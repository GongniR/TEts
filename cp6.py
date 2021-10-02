array = [int(i) for i in input('Введите значения массива через пробел: ').split()] # короче, это генератор, это самый лучший способ ввода массива
delta = int(input('Введите смещение DELTA: '))

def get_min(array):
    min_item = 99999 # супер большое число
    for item in array:
        if item < min_item:
            min_item = item
    return min_item


min_item = get_min(array)
count = 0
for item in array:
    if (item - min_item) == delta:
        count += 1

print("минимальный элемента массива: ", min_item, " Кол-во чисел отличающихся на DELTA: ", count)