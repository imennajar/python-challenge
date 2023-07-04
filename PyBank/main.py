#Import the library csv 
import csv

#Import the library os 
import os

#Declare the path of the csv file from where we will read information
csvpath= os.path.join("PyBank/resources","budget_data.csv")

#Declare the path of the text file where we will write the results
output_path=os.path.join("PyBank/analysis","result.txt")

#Print the header on the terminal
print('Financial Analysis')
print('--------------------------------------------------','\n')

#Inisialize the net total amount of "Profit/Losses" before start counting 
net_amount= 0

#Declare 4 lists: 
#a:will contain, in order as the file, each value of profit/losses
a=[]

#b:will contain the changes in Profit/Losses
b=[]

#c: will contain, in order as the file, each date
c=[]

#d:will contain the date of changes
d=[]

#open the csv file to read
with open (csvpath) as csvfile:
    
    #assign each element in the list to csvreader
    csvreader= csv.reader(csvfile, delimiter =",")
    
    #skeep the header 
    csv_header=next(csvreader)
    
    #loop in the file
    for row in csvreader:
       
        # net total amount
        net_amount = net_amount + float(row[1])
        
        #assign the value of each profit/lost and their date respectively to the lists a and c
        a.append(float(row[1]))  
        c.append(row[0])
    
    #print the total of months    
    print('Total Months: ',len(a),'\n')
    
    #print net amount
    print ('Total: ', round(net_amount),'\n')
    
    #assign the changes of each profit/loses and their dates respectively in list b and d
    for j in range (len(a)-1):
        
        x=((a[j+1]-a[j]))
        y=c[j+1]
        b.append((x))
        d.append(y)
        
    #calculate the average of the changes
    avg= sum(b)/len(b)
    
    #print the average
    print('Average change ',round(avg,2),'\n')
    
    # look for the greatest change's increase and the greatest chage's decrease and their dates    
    max=0
    pmax=0
    min=0
    pmin=0
    
    #loops to look for the max and the min and their positions in the list b
    
    for i in range (len(b)):
        if b[i]< min:
            min=b[i]
            pmin=i
            
    for j in range (len(b)):
        if b[j]> max:
            max=b[j]
            pmax=j  
   
   
    #look for the dates with the min and max position in the list d and print the greatest decrese with its date and the greatest increase with its date
    h = 0
    stop= False
    while(stop==False) or (h>=len(b)):
        if h == pmax: 
            stop=True
        else: h=h+1
    
    print('Greatest Increase in Profits',d[h],'($',round(max),')','\n')
               
    h = 0
    stop= False
    while(stop==False) or (h>=len(b)):
        if h == pmin: 
            stop=True
        else: h=h+1
    
    print('Greatest Decrease in Profits',d[h],'($',round(min),')','\n')  
    
#open the file text to write our result    
with open(output_path,'w') as f:
    
    #put each result in a variable and add it to the file
    ch='Financial Analysis'+'\n'
    f.write(ch)
    ch='-----------------------------------'+'\n'+'\n'
    f.write(ch)
    ch='Total Months: '+str(len(a))+'\n'+'\n'
    f.write(ch)
    ch= 'Total: '+str (round(net_amount))+'\n'+'\n'
    f.write(ch)
    ch= 'Average change: '+str(round(avg,2))+'\n'+'\n'
    f.write(ch)
    ch= 'Greatest increase: '+str(round(max))+'\n'+'\n'
    f.write(ch)
    ch= 'Greatest decrease: '+str(round(min))+'\n'+'\n'
    f.write(ch)
    
