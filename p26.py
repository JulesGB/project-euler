def mult_order(n):
    i = 1
    while i < n-1 and 10**i % n != 1:
        i += 1

    return i

max_period = 1
d = 3
max_d = d

while d < 1000:
    if d % 2 == 0 or d % 5 == 0:
        d += 1
        continue
    else:
        d_period = mult_order(d)
        
    if d_period > max_period:
        max_period = d_period
        max_d = d
    d += 1

print(max_d)
