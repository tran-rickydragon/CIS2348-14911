#Ricky Tran - 1832920

dates = []

date = 0

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

while date != '-1':
    date = input()
    form = date.split(' ')
    if form[0] in month:
        if ',' in form[1]:
            if len(form[2]) == 4:
                dates.append(date)

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




