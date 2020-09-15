
current_month = int(input("Please enter the current month"))
current_day = int(input("Please enter the current day"))
current_year = int(input("Please enter the current year"))

birth_month = int(input("Please enter your birth month"))
birth_day = int(input("Please enter your birth day"))
birth_year = int(input("Please enter your birth year"))

age = current_year - birth_year

if current_month < birth_month:
    age = age - 1

if current_month == birth_month:
    if current_day < birth_day:
        age = age - 1
print('Current day')
print('Month:', current_month)
print('Day:', current_day)
print('Year:', current_year)
print('Birthday')
print('Month:', birth_month)
print('Day:', birth_day)
print('Year:', birth_year)
print('You are', age, 'years old')

if current_month == birth_month:
    if current_day == birth_day:
        print('Happy Birthday!')
