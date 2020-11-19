"""
rect_count = 1
x,y = 1,1

while rect_count < 2 * 10**6:
    rect_count = 0

    for rx in range(1, x+1):
        for ry in range(1, y+1):
            rect_count += (x-rx+1) * (y-ry+1)
"""

target = 2 * 10**6

closest = 0
cx, cy = -1, -1

upper_bound = 1000
for x in range(1, upper_bound):
    for y in range(x, upper_bound):
        # simplification of summation(i=1, x, summation(j=1, y,((x-i+1)(y-j+1))))
        rect_count = (x**2 * y**2 + x**2 * y + x * y**2 + x * y) / 4

        if abs(rect_count - target) < abs(closest - target):
            closest = rect_count
            cx, cy = x, y

print(x,y)
print(closest)
