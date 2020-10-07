"""Ricky Tran - 1832920"""

"""List of months for verifying correct format"""

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December']
"""Dictionary of months with corresponding number"""

months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
          'September': 9, 'October': 10, 'November': 11, 'December': 12}
input_dates = open(r'C:\Users\ricky\OneDrive\Desktop\School\20\Fall_20\CIS2348\inputDates.txt')

"""Modified the loop so that the input is taken from the file"""

for date in input_dates:
    x = date.split(' ')
    if x[0] in month:
        if ',' in date:
                a = x[0]
                b = x[1]
                c = x[2]
                a = months[a]
                b = b.replace(',', '')
                new_format = '{}/{}/{}'
                print(new_format.format(a, b, c))
