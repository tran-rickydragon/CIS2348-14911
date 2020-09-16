print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print()

service = {'Oil change': '35', 'Tire rotation': '19', 'Car wash': '7', 'Car wax': '12', '-': '0'}
first = (input('Select first service:\n'))
second = (input('Select second service:\n'))

cost1 = '$' + service[first]
cost2 = '$' + service[second]

total = int(service[first]) + int(service[second])
total = '$' + str(total)

print()
print('Davy\'s auto shop invoice')
print()
if first == '-':
    print('Service 1: No service')
else:
    print('Service 1:', first + ',', cost1)
if second == '-':
    print('Service 2: No service')
else:
    print('Service 2:', second + ',', cost2)

print()
print('Total:', total)
