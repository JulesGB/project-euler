from itertools import permutations
from functools import reduce

def is_prime(n):
    # assume already checked for multiples of 2 and 3
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6

    return True

# only have to look for 7-digit pandigital numbers since
# 8/9-digit pandigital nums are always divisible by 3 (non-prime)
for perm in permutations(range(7,0,-1)):

    if perm[-1] % 2 == 0 or sum(perm) % 3 == 0:
        continue

    n = reduce(lambda x,y : 10*x + y, perm)

    if is_prime(n):
        print(n)
        break
