from functools import reduce

factorial = {}
for i in range(10):
    fact = 1
    for j in range(2, i+1):
        fact *= j

    factorial[i] = fact

upper_bound = 50000 # theoretical upper bound is 9! * 7, though this gets everything

s = 0
for arr,n in [([int(x) for x in str(y)],y) for y in range(3, upper_bound)]:
    if (n < 10 and n == factorial[n]) or n == sum([factorial[x] for x in arr]):
        print(n)
        s += n

print(s)
