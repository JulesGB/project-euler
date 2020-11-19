# sqrt(d) has period 1 for d = n^2 + 1
# Samuel S. Wagstaff, Jr. The Joy of Factoring. Theorem 6.15.

def get_period(n):
    if (n-1)**0.5 % 1 == 0:
        return 1
    
    m = [0]
    d = [1]
    a = [int(n**0.5)]

    i = 0
    while i < 2*n + 1:
        # would be more efficient to store these as a set of tuples, but this is easier and works for these bounds
        m.append(d[i] * a[i] - m[i])
        d.append((n - m[i+1]**2) / d[i])
        a.append(int((a[0] + m[i+1]) / d[i+1]))

        i += 1

        for j in range(i):
            if m[-1] == m[j] and d[-1] == d[j] and a[-1] == a[j]:
                return len(a) - 2
    

odd_period_count = 0
for n in range(2, 10001):
    if n**0.5 % 1 == 0:
        continue

    if get_period(n) % 2 == 1:
        odd_period_count += 1

print("Odd period count <= 10,000:", odd_period_count)
    
