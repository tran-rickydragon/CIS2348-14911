"""Ricky Tran - 1832920"""

"""start off with an empty date list"""
dates = []

"""List of months for verifying correct format"""

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December']
"""Dictionary of months with corresponding number"""

months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
          'September': 9, 'October': 10, 'November': 11, 'December': 12}

"""Loop for verifying if the input is the correct format and then storing it in the dates list"""
date = 0
while date != '-1':
    date = input()
    form = date.split(' ')
    if form[0] in month:
        if ',' in form[1]:
            if len(form[2]) == 4:
                dates.append(date)

"""Loop for printing dates from the dates list with the new format"""
i = 0
j = int(len(dates))

while i < j:
    x = dates[i].split(' ')
    a = x[0]
    b = x[1]
    c = x[2]
    a = months[a]
    b = b.replace(',', '')
    i += 1
    new_format = '{}/{}/{}'
    print(new_format.format(a, b, c))
