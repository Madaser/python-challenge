import os
import csv

sum=0
csvpath=os.path.join('..', 'budget_data.csv')
total= 0
rows=[]

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

 
    for row in csvreader:
        total=total+len(row)
        sum=sum+int(row[1])
        rows.append(row)
    Months=len(rows)
    Last_Value=int(row[1])
    
    extrarows=[]
    extracolumns=[]
    for i in range(len(rows)):
        extrarows.append((rows[i][1]))
        extracolumns.append((rows[i][0]))
    
    First_Value=int(extrarows[0])
    Average=(Last_Value-First_Value)/Months
    

    g=0
    best="month"
    update="newm"
    listnumber=range(len(extrarows))
    for i in (range(len(listnumber)-1)):
        if((int(extrarows[i+1])-int(extrarows[i])>0)):
            m=(int(extrarows[i+1])-int(extrarows[i]))
            best=extracolumns[i+1]
            if(g>m):
                m=g
                best=update
            else:
                m=m
                best=best    
        else:
            g=m
            update=best
    
    

    b=0
    n=0
    besty="month"
    updatey="newm"
    for i in (range(len(listnumber)-1)):
        if((int(extrarows[i+1])-int(extrarows[i])<0)):    
            b=(int(extrarows[i+1])-int(extrarows[i]))
            besty=extracolumns[i+1]
            if(n<b):
                b=n
                besty=updatey
            else:
                b=b
                besty=besty
        else:
            n=b
            updatey=besty
    
            


    print(f'Total Months: {Months}')
    print(f'Total Profits/Losses: {sum}')
    print(f'Average Change: {Average}')
    print(f'Greatest increase in profits: {best} ({m})')
    print(f'Greatest decrease in profits: {besty} ({n})')

    

    output_path = os.path.join("..", "new.txt")
    with open(output_path, 'w', newline='') as csvfile:

        csvwriter = csv.writer(csvfile, delimiter=',')

        csvwriter.writerow([f'Total Months: {Months}'])
        csvwriter.writerow([f'Total Profits/Losses: {sum}'])
        csvwriter.writerow([f'Average Change: {Average}'])
        csvwriter.writerow([f'Greatest increase in profits: {best} ({m})'])
        csvwriter.writerow([f'Greatest decrease in profits: {besty} ({n})'])
    
        
        



        
        



