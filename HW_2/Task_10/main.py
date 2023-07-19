# : На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.


from random import randint

quantityOfCoins = int(input("Введите количество монет: "))
eagles = 0
tails = 0
for _ in range(quantityOfCoins):
    genCoin = randint(0,1)
    if genCoin==1: eagles +=1
    else: tails +=1
    print(genCoin, end=",")
if eagles>tails: print(f'\n {tails}')
else: print(f'\n {eagles}')
