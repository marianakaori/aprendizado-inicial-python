from math import sqrt

x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

dist = sqrt((x2 - x1)**2 + (y2 - y1)** 2)

template = '{:.1f}'
print(template.format(dist))