from functools import reduce

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6

    return True

primes = set()
composites = set()

upper_bound = 3947
for n in range(2, upper_bound):
    if n not in composites and is_prime(n):
        primes.add(n)
        
        i = 2
        while n*i < upper_bound:
            composites.add(n*i)
            i += 1

primes = sorted(list(primes))

# brute force approach: O(n^2), requires manual upper_bound testing

# a better approach that doesn't require any manual upper bounds testing would be
# to generate all primes up to 10**6, and then use binary search to narrow down

prime_sums = {0 : 0}
for i in range(1, len(primes)):
    prime_sums[i] = prime_sums[i-1] + primes[i]

max_primes = 0
prime_sum = -1

"""
i = 0
while i < len(primes) and len(primes) - i > max_primes:
    for j in range(i+1, len(primes)+1):
        if j-i > max_primes:
            curr_sum = reduce(lambda x,y : x+y, primes[i:j])

            if is_prime(curr_sum):
                max_primes = j - i
                prime_sum = curr_sum

    i += 1
"""
            
print(max_primes)
print(prime_sum)
