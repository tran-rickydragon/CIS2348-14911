"""Ricky Tran - 1832920"""
password = str(input(''))

for x in password:
    if x == 'i':
        password = password.replace('i', '!')
    elif x == 'a':
        password = password.replace('a', '@')
    elif x == 'm':
        password = password.replace('m', 'M')
    elif x == 'B':
        password = password.replace('B', '8')
    elif x == 'o':
        password = password.replace('o', '.')
    else:
        password = password

print('{x}q*s'.format(x=password))
