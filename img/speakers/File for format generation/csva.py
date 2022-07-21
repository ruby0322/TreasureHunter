import csv
myfil = open('staff_list.csv', newline='')
myfile = csv.reader(myfil)
rows = []
for row in myfile:
    rows.append(row)
for row in rows:
    print(str(row) + ',')
