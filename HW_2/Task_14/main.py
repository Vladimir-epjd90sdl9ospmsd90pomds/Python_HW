#  Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

num = int(input("Введите число: "))
degree = 0
while 2 ** degree <= num:
    print(2 ** degree, end = " ")
    degree += 1