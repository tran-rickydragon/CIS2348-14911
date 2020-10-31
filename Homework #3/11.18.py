""""Ricky Tran - 1832920"""

integers = input().split(' ')

numbers = []

for num in integers:
    num = int(num)
    numbers.append(num)

positive = []

for num in numbers:
    if num >= 0:
        positive.append(num)

positive.sort()

for num in positive:
    print(num, end=' ')