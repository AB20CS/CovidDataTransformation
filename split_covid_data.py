import csv

o = open('covid_merged_data.csv')
f1 = open('covid_split1.csv', 'w', newline='')
f2 = open('covid_split2.csv', 'w', newline='')

csv_o = csv.reader(o)
csv_f1 = csv.writer(f1)
csv_f2 = csv.writer(f2)

i = 0
for row in csv_o:
    if i % 2 == 0:
        csv_f1.writerow(row)
    if i == 1:  # to write the column headers in the second file (does not have column headers to begin with)
        csv_f2.writerow(['PHU',
                         'Mean % of Students from Low-Income Households',
                         'Mean % of Students Whose Parents Have Some University Education',
                         'Age', 'Gender', 'Case Acquisition', 'Outcome'])
    elif i % 2 == 1:
        csv_f2.writerow(row)
    i += 1

o.close()
f1.close()
f2.close()
