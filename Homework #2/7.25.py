"""Ricky Tran - 1832920"""
def exact_change(user_total):
    num_dollars = 0
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0
    if user_total <= 0:
        print('no change')
    else:
        while user_total >= 100:
            num_dollars += 1
            user_total -= 100
        while user_total >= 25:
            num_quarters += 1
            user_total -= 25
        while user_total >= 10:
            num_dimes += 1
            user_total -= 10
        while user_total >= 5:
            num_nickels += 1
            user_total -= 5
        while user_total >= 1:
            num_pennies += 1
            user_total -= 1

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if num_dollars == 1:
        print('1 dollar')
    elif num_dollars >= 2:
        print(num_dollars, 'dollars')
    if num_quarters == 1:
        print('1 quarter')
    elif num_quarters >= 2:
        print(num_quarters, 'quarters')
    if num_dimes == 1:
        print('1 dime')
    elif num_dimes >= 2:
        print(num_dimes, 'dimes')
    if num_nickels == 1:
        print('1 nickel')
    elif num_nickels >= 2:
        print(num_nickels, 'nickels')
    if num_pennies == 1:
        print('1 penny')
    elif num_pennies >= 2:
        print(num_pennies, 'pennies')
