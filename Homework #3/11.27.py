""""Ricky Tran - 1832920"""

p1jn = int(input('Enter player 1\'s jersey number:\n'))
p1r = int(input('Enter player 1\'s rating:\n'))
print()
p2jn = int(input('Enter player 2\'s jersey number:\n'))
p2r = int(input('Enter player 2\'s rating:\n'))
print()
p3jn = int(input('Enter player 3\'s jersey number:\n'))
p3r = int(input('Enter player 3\'s rating:\n'))
print()
p4jn = int(input('Enter player 4\'s jersey number:\n'))
p4r = int(input('Enter player 4\'s rating:\n'))
print()
p5jn = int(input('Enter player 5\'s jersey number:\n'))
p5r = int(input('Enter player 5\'s rating:\n'))
print()

roster = {}

roster[p1jn] = p1r
roster[p2jn] = p2r
roster[p3jn] = p3r
roster[p4jn] = p4r
roster[p5jn] = p5r

print('ROSTER')
for jersey, rating in sorted(roster.items()):
        print('Jersey number: {}, Rating: {}'.format(jersey, rating))

menu = ('\nMENU\n'
        'a - Add player\n'
        'd - Remove player\n'
        'u - Update player rating\n'
        'r - Output players above a rating\n'
        'o - Output roster\n'
        'q - Quit\n')


print(menu, end='\n')
option = ''
while (option != 'q'):
        option = input('Choose an option:\n')
        if option == 'o':
                print('ROSTER')
                for jersey, rating in sorted(roster.items()):
                        print('Jersey number: {}, Rating: {}'.format(jersey, rating))
                print(menu, end='\n')
        if option == 'a':
                npjn = int(input('Enter a new player\'s jersey number:\n'))
                npr = int(input('Enter a new player\'s rating:\n'))
                nroster = {}
                nroster[npjn] = npr
                roster.update(nroster)
                nroster.clear()
                print(menu, end='\n')
        if option == 'd':
                dp = int(input('Enter a jersey number:\n'))
                roster.pop(dp)
                print(menu, end='\n')
        if option == 'r':
                ar = int(input('Enter a rating:\n'))
                print('ABOVE', ar)
                for jersey, rating in sorted(roster.items()):
                        if rating > ar:
                                print('Jersey number: {}, Rating: {}'.format(jersey, rating))
                print(menu, end='\n')
        if option == 'u':
                ujr = int(input('Enter a jersey number:\n'))
                ur = int(input('Enter a new rating for player:\n'))
                roster[ujr] = ur
                print(menu, end='\n')