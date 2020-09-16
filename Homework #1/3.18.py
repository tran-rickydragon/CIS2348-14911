height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))

area = height * width

print('Wall area:', area, 'square feet')

paint = float(area / 350)

can = int(paint + 1)

print('Paint needed: {p:.2f} gallons'.format(p=paint))

print('Cans needed:', can, 'can(s)')

prices = {'red': '35', 'blue': '25', 'green': '23'}
print()
color = input("Choose a color to paint the wall:\n")

color_mul = (int(prices[color]) * can)
price = '$' + str(color_mul)

print('Cost of purchasing', color, 'paint:', price)