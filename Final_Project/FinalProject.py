""""Ricky Tran - 1832920"""

import csv

from collections import defaultdict

from datetime import datetime

# dictionaries for the different categories of each item
item_id = {}
manufacturer = {}
type = {}
damage = {}
price = {}
date = {}

# opening input files and putting the information in the appropriate dictionaries

with open('ManufacturerList.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        item_id[row[0]] = None
        manufacturer[row[0]] = row[1].replace(' ', '')
        type[row[0]] = row[2]
        damage[row[0]] = row[3]

with open('PriceList.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        price[row[0]] = row[1]

with open('ServiceDatesList.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        date[row[0]] = row[1]

# using the defaultdict function to put all the dictionaries into a bigger dictionary with the item ID as the key

fulldict = defaultdict(list)
for a in (item_id, manufacturer, type, price, date, damage):
    for key, value in a.items():
        fulldict[key].append(value)

# turn the dictionary to a list

fulllist = []

for b, c in fulldict.items():
    del c[0]
    fulllist.append([b] + c)

# creating the FullInventory file

with open('FullInventory.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    sort = sorted(fulllist, key=lambda row: row[1], reverse=False)
    for row in sort:
        csv_writer.writerow(row)

# list of each item type

phoneInventory = []
laptopInventory = []
towerInventory = []

# putting items in their corresponding item type list

with open('FullInventory.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        if row[2] == 'phone':
            phoneInventory.append(row)
        if row[2] == 'laptop':
            laptopInventory.append(row)
        if row[2] == 'tower':
            towerInventory.append(row)

# sorting each list by item ID

phoneInventory = sorted(phoneInventory)
laptopInventory = sorted(laptopInventory)
towerInventory = sorted(towerInventory)

# creating csv of each item type and deleting item type from the list

with open('PhoneInventory.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    for row in phoneInventory:
        del row[2]
        csv_writer.writerow(row)

with open('LaptopInventory.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    for row in laptopInventory:
        del row[2]
        csv_writer.writerow(row)

with open('TowerInventory.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    for row in towerInventory:
        del row[2]
        csv_writer.writerow(row)

# making a file for items past the service date

today = datetime.today()
PastService = []

with open('FullInventory.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        item_date = datetime.strptime(row[4], '%m/%d/%Y')
        if item_date < today:
            PastService.append(row)

SortedPastService = sorted(PastService, key=lambda row: datetime.strptime(row[4], '%m/%d/%Y'), reverse=False)

with open('PastServiceDateInventory.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    for row in SortedPastService:
        csv_writer.writerow(row)

# making a file for damaged items

damagedInventory = []

with open('FullInventory.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        if row[5] == 'damaged':
            damagedInventory.append(row)

SortedDamagedInventory = sorted(fulllist, key=lambda row: row[3], reverse=False)

with open('DamagedInventory.csv.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    for row in SortedDamagedInventory:
        csv_writer.writerow(row)

# creating an inventory of items that are not past service date and not damaged that we can use

CurrentInventory = []

with open('FullInventory.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        item_date = datetime.strptime(row[4], '%m/%d/%Y')
        if item_date > today:
            if row[5] != 'damaged':
                del row[5]
                del row[4]
                row[3] = int(row[3])
                CurrentInventory.append(row)

# function for finding the closest number from a list to a certain number


def closest(lst, k):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - k))]


M_input = str(input('Please enter the manufacturer:\n'))

T_input = str(input('Please enter the item type:\n'))

# list for storing results based on inputs

result = []
alsoResult = []
alsoResultP = []

while M_input != 'q':
    M_input = M_input.capitalize()
    T_input = T_input.lower()
    # adding items to lists based on the inputs
    for i in range(0, len(CurrentInventory)):
        # adding matching items to input into result
        if M_input in CurrentInventory[i] and T_input in CurrentInventory[i]:
            result.append(CurrentInventory[i])
        # adding items with the same type but different manufacturer into alsoResult
        if M_input not in CurrentInventory[i] and T_input in CurrentInventory[i]:
            alsoResult.append(CurrentInventory[i])
            # adding the item's price to alsoResultP
            alsoResultP.append(int(CurrentInventory[i][3]))
    if len(result) != 0:
        sortedResult = sorted(result, key=lambda row: row[3], reverse=True)
        # print result
        print()
        print('Your item is: {} {} {} ${}'.format(sortedResult[0][0], sortedResult[0][1],
                                                  sortedResult[0][2], sortedResult[0][3]))
        print()
        # finding item with the closest price
        ogP = int(sortedResult[0][3])
        also = closest(alsoResultP, ogP)
        # print also result
        for i in range(0, len(alsoResult)):
            if alsoResult[i][3] == also:
                print('You may also consider: {} {} {} ${}'.format(alsoResult[i][0], alsoResult[i][1],
                                                                   alsoResult[i][2], alsoResult[i][3]))
                print()
    else:
        print()
        print('No such item in inventory')
        print()
    # clearing each list for next use if user does not quit
    result.clear()
    alsoResult.clear()
    alsoResultP.clear()
    print('Please enter "q" to quit')
    print()
    M_input = str(input('Please enter the manufacturer:\n'))
    if M_input == 'q':
        break
    T_input = str(input('Please enter the item type:\n'))
