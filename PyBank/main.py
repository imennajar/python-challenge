#Import the library csv 
import csv

#Import the library os 
import os

#Declare the path of the csv file from where we will read information
csvpath= os.path.join("PyBank/resources","budget_data.csv")

#Declare the path of the text file where we will write the results
output_path=os.path.join("PyBank/analysis","budget_data.txt")

#Print the header on the terminal
print('\n','Financial Analysis','\n','\n')
print('--------------------------------------------------','\n','\n')

#Initialize the net total amount of "Profit/Losses"
net_amount= 0

#Declare 4 lists: 
#a:will contain, in the same order as the file, each value of profit/losses
a=[]

#b:will contain the changes in Profit/Losses
b=[]

#c: will contain, in the same order as the file, each date
c=[]

#d:will contain the date of changes
d=[]

#open the csv file to read
with open (csvpath) as csvfile:
    
    #assign each element in the list to csvreader
    csvreader= csv.reader(csvfile, delimiter =",")
    
    #skip the header 
    csv_header=next(csvreader)
    
    #loop in the file
    for row in csvreader:
       
        # net total amount
        net_amount = net_amount + float(row[1])
        
        #assign the value of each profit/loss and their date respectively to the lists a and c
        a.append(float(row[1]))  
        c.append(row[0])
    
    #print the total of months    
    print('Total Months: ', len(a),'\n','\n')
    
    #print net amount
    print ('Total: ','$',round(net_amount),'\n','\n')
    
    #assign the changes of each profit/loss and their dates respectively in list b and d
    for j in range (len(a)-1):
        
        x=((a[j+1]-a[j]))
        y=c[j+1]
        b.append((x))
        d.append(y)
        
    #calculate the average of the changes
    avg= sum(b)/len(b)
    
    #print the average
    print('Average change: $',round(avg,2),'\n','\n')
    
    max=max(b)
    
    min=min(b)
    
    pmax=b.index(max)
    
    pmin=b.index(min)
    
    print('Greatest Increase in Profits: ',d[pmax],'($',round(max),')','\n','\n')
                
    print('Greatest Decrease in Profits: ',d[pmin],'($',round(min),')','\n','\n')  
    
#open the file text to write our result    
with open(output_path,'w') as f:
    
    #put each result in a variable and add it to the file
    ch='\n'+'Financial Analysis'+'\n'+'\n'
    f.write(ch)
    ch='-----------------------------------'+'\n'+'\n'
    f.write(ch)
    ch='Total Months: '+str(len(a))+'\n'+'\n'
    f.write(ch)
    ch= 'Total: $'+str (round(net_amount))+'\n'+'\n'
    f.write(ch)
    ch= 'Average change: $'+str(round(avg,2))+'\n'+'\n'
    f.write(ch)
    ch= 'Greatest Increase in Profits: '+d[pmax]+' ($'+str(round(max))+')'+'\n'+'\n'
    f.write(ch)
    ch= 'Greatest Decrease in Profits: '+d[pmin]+' ($'+str(round(min))+')'+'\n'+'\n'
    f.write(ch)
    
