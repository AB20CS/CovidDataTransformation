# conducts data transformation for student demographics data (collected from EQAO exams)

import csv
import pandas as pd

e = open('eqao_data_phu.csv')
d = open('eqao_aggregated_data.csv', 'w', newline='')
x = open('exception_data.csv', 'w', newline='')

csv_e = csv.reader(e)  # open original data set for reading
csv_d = csv.writer(d)  # open CSV file for writing transformed data
csv_x = csv.writer(x)  # open CSV file for writing exception data

transformed_data = []  # list to hold transformed data temporarily

for row in csv_e:
    # Public Health Unit = row[1]
    phu = row[1]
    # type of school (e.g., public, Catholic) = row[8]
    school_type = row[8]
    # school level = row[10]
    school_level = row[10]
    # low-income households = row[47]
    low_income = row[47]
    # parent university education = row[48]
    parents_uni = row[48]

    if "NA" in low_income:
        csv_x.writerow([phu, school_type, school_level, low_income, parents_uni])
    elif "SP" in low_income:
        csv_x.writerow([phu, school_type, school_level, low_income, parents_uni])
    elif "NA" in parents_uni:
        csv_x.writerow([phu, school_type, school_level, low_income, parents_uni])
    elif "SP" in parents_uni:
        csv_x.writerow([phu, school_type, school_level, low_income, parents_uni])
    elif ("Hospital" or "Provincial" or "Separate") in school_type:
        csv_x.writerow([phu, school_type, school_level, low_income, parents_uni])
    elif "PHU" in row[1]:  # to write column headers in exception file
        csv_x.writerow([phu, school_type, school_level, low_income, parents_uni])
    else:
        transformed_data.append([phu, school_type, school_level, float(low_income), float(parents_uni)])

# convert transformed data list into DataFrame
df = pd.DataFrame(transformed_data)
df.columns = ['PHU',
              'School Type',
              'School Level',
              'Percentage of Children Who Live in Low-Income Households',
              'Percentage of Students Whose Parents Have Some University Education']

# group DataFrame based on PHU -> PHU becomes index
grouped_phu = df.groupby('PHU').agg(
    {'Percentage of Children Who Live in Low-Income Households': 'mean',
     'Percentage of Students Whose Parents Have Some University Education': 'mean'})

# name columns
grouped_phu.columns = ['Mean % of Students from Low-Income Households',
                       'Mean % of Students Whose Parents Have Some University Education']

grouped_phu.to_csv("eqao_aggregated_data.csv")  # converting DataFrame to CSV

e.close()
d.close()
x.close()
