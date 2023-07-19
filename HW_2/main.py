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
