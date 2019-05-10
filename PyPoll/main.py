import os
import csv

csvpath=os.path.join('..','election_data.csv')

rows=[]
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    header=next(csvreader)

    for row in csvreader:
        rows.append(row)
    m=0
    m=len(rows)
    

sum=0
sum1=0
sum2=0
sum3=0
extrarows=[]
extracolumns=[]
for i in range(len(rows)):
    extrarows.append((rows[i][2]))
    extracolumns.append((rows[i][0]))
    if(extrarows[i]=="Khan"):
        sum=sum+1
    elif(extrarows[i]=="Correy"):
        sum1=sum1+1
    elif(extrarows[i]=="Li"):
        sum2=sum2+1
    elif(extrarows[i]=="O'Tooley"):
        sum3=sum3+1

Winner='s'
if((sum > sum1) & (sum>sum2) & (sum>sum3)):
    Winner='Khan'
elif((sum1>sum) & (sum1>sum2) & (sum1>sum3)):
    Winner='Corey'
elif((sum2>sum) & (sum2>sum1) & (sum2>sum3)):
    Winner='Li'
elif((sum3>sum) & (sum3>sum1) & (sum3>sum2)):
    Winner='O-Tooley'


x=(sum/m)*100
x1=round(x,3)
y=(sum1/m)*100
y1=round(y,3)
z=(sum2/m)*100
z1=round(z,3)
zz=(sum3/m)*100
zz1=round(zz,3)

print(f'Election Results')
print(f'------------------------')
print(f'Total Votes: {m}')
print(f'------------------------')
print(f'Khan: {x1}% ({sum})')
print(f'Correy: {y1}% ({sum1})')
print(f'Li: {z1}% ({sum2})')
print(f'O-Tooley: {zz1}% ({sum3})')
print(f'------------------------')
print(f'Winner: {Winner}')
print(f'------------------------')


output_path = os.path.join("..", "PyPoll.txt")
with open(output_path, 'w', newline='') as csvfile:

        csvwriter = csv.writer(csvfile, delimiter=',')

        csvwriter.writerow([f'Election Results'])
        csvwriter.writerow([f'------------------------'])
        csvwriter.writerow([f'Total Votes: {m}'])
        csvwriter.writerow([f'------------------------'])
        csvwriter.writerow([f'Khan: {x1}% ({sum})'])
        csvwriter.writerow([f'Correy: {y1}% ({sum1})'])
        csvwriter.writerow([f'Li: {z1}% ({sum2})'])
        csvwriter.writerow([f'O-Tooley: {zz1}% ({sum3})'])
        csvwriter.writerow([f'------------------------'])
        csvwriter.writerow([f'Winner: {Winner}'])
        csvwriter.writerow([f'------------------------'])



