from functools import reduce

champ = ""

for i in range(187000):
    champ += str(i)


print(reduce(lambda x,y : x*y, [int(champ[10**i]) for i in range(7)]))
