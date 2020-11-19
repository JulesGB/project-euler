def spiral_diag_sum(n):
    s = 1
    current = 1
    for i in range(n // 2):
        for j in range(4):
            current += 2 * i + 2
            s += current

    return s

print("sum:", spiral_diag_sum(1001))
