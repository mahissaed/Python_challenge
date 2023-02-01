# imports 
import csv
import os
import datetime
# constants
CSV_PATH = os.path.join("Resources", "budget_data.csv")

# read data from the file 
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file)
    months = []

    #  calucate information 
    for row in csv_reader: 
      try:
            date = datetime.datetime.strptime(row[0], '%b-%d')
            months.append(date.month)
      except ValueError:
        print(f'Error parsing date {row[0]}')

    total_months = len(months)
    print('total number of months;', total_months)

# output (print and file)
import csv

with open(CSV_PATH) as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    total = 0
    for row in reader:
        total += int(row[1])
    print('Net total:', total)



import csv 

with open(CSV_PATH) as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader) #toskipheader
    prev_value = int(next(reader)[1])
    changes = []
    for row in reader:
        curr_value = int(row[1])
        curr_value - prev_value
        change = curr_value - prev_value
        changes.append(change)
    avg_change = sum(changes) / len(changes)
    print('Average change:', avg_change)
    
    
    
    
import csv

with open(CSV_PATH) as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader) # skip header
    prev_value = int(next(reader)[1]) # get the first value
    max_increase = (header[0], 0)
    for row in reader:
        curr_value = int(row[1])
        increase = curr_value - prev_value
        if increase > max_increase[1]:
            max_increase = (row[0], increase)
        prev_value = curr_value
    print('Greatest increase in profits:', max_increase)


        
    
import csv

with open(CSV_PATH) as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader) # skip header
    prev_value = int(next(reader)[1]) # get the first value
    max_decrease = (header[0], 0)
    for row in reader:
        curr_value = int(row[1])
        decrease = prev_value - curr_value
        if decrease > max_decrease[1]:
            max_decrease = (row[0], decrease)
        prev_value = curr_value
    print('Greatest decrease in profits:', max_decrease)