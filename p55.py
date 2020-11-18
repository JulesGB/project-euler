def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False

    return True

count = 0
for n in range(10000):
    if is_lychrel(n):
        count += 1

print(count)
