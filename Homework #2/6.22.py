"""Ricky Tran - 1832920"""
a = int(input(''))
b = int(input(''))
c = int(input(''))

d = int(input(''))
e = int(input(''))
f = int(input(''))

px = 'no'

for x in range(-10, 11):
    for y in range(-10, 11):
        g = a * x + b * y - c
        h = d * x + e * y - f
        if g == h and g == 0:
            px = x
            py = y

if px != 'no':
    print(px, py)
else:
    print('No solution')
