from itertools import product
from functools import reduce

def is_prime(n):
    # assume already checked for multiples of 2 and 3
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6

    return True

count = 4 # four single digit primes
for digits in range(2,7):
    for perm in product([1,3,7,9], repeat=digits):
        if sum(perm) % 3 == 0:
            continue

        i = 0
        circular = True
        while i < digits:
            n = reduce(lambda x,y : 10*x + y, perm[i:]+perm[:i])
            if not is_prime(n):
                circular = False
                break
            i += 1

        if circular:
            count += 1
            print(perm)

print(count)
