import os
import csv

sum=0
csvpath=os.path.join('..', 'budget_data.csv')
total= 0
sum=0
rows=[]

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

 
    for row in csvreader:
        print(row)
        
        total=total+len(row)
        sum=sum+int(row[1])
        rows.append(row)
    print(total/2)
    print(sum)
    Last_Value=int(row[1])
    print(Last_Value)
        



