# conducts data transformation for COVID-19 data

import csv
import pandas as pd

c = open('covid_data.csv')
t = open('covid_transformed.csv', 'w', newline='')

csv_c = csv.reader(c)

transformed_data = []  # list to hold transformed data temporarily

next(csv_c)  # in order to begin iterating from second row (avoids reading the CSV headers)
for row in csv_c:
    phu = row[5]
    age = row[0]
    gender = row[1]
    case_acq = row[2]
    outcome = row[3]

    if gender == "":
        transformed_data.append([phu, age, "UNKNOWN", case_acq, outcome])
    else:
        transformed_data.append([phu, age, gender, case_acq, outcome])

df = pd.DataFrame(transformed_data)  # convert transformed data list into DataFrame
df.columns = ['PHU',
              'Age',
              'Gender',
              'Case Acquisition',
              'Outcome']

df.to_csv("covid_transformed.csv", index=False)  # convert DataFrame into CSV

c.close()
t.close()
