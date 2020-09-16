lemon_juice = int(input("Enter amount of lemon juice (in cups):\n"))
water = int(input("Enter amount of water (in cups):\n"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = int(input("How many servings does this make?\n"))

print()
print('Lemonade ingredients - yields {s:.2f} servings'.format(s = servings))
print('{lm:.2f} cup(s) lemon juice'.format(lm = lemon_juice))
print('{w:.2f} cup(s) water'.format(w = water))
print('{an:.2f} cup(s) agave nectar'.format(an = agave_nectar))

print()
desired = int(input('How many servings would you like to make?\n'))
multi = desired / servings

desired_lm = lemon_juice * multi
desired_w = water * multi
desired_an = agave_nectar * multi

print()
print('Lemonade ingredients - yields {d:.2f} servings'.format(d = desired))
print('{lm2:.2f} cup(s) lemon juice'.format(lm2 = desired_lm))
print('{w2:.2f} cup(s) water'.format(w2 = desired_w))
print('{an2:.2f} cup(s) agave nectar'.format(an2 = desired_an))

gallons_lm = desired_lm / 16
gallons_w = desired_w / 16
gallons_an = desired_an / 16

print()
print('Lemonade ingredients - yields {d:.2f} servings'.format(d = desired))
print('{lm3:.2f} gallon(s) lemon juice'.format(lm3 = gallons_lm))
print('{w3:.2f} gallon(s) water'.format(w3 = gallons_w))
print('{an3:.2f} gallon(s) agave nectar'.format(an3 = gallons_an))