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

#Inisialize the number of month at 0 before start counting the number
nbr_m=0

#Inisialize the net total amount of "Profit/Losses" before start counting the sum
net_amount= 0

#Declare 4 lists: 
#a:will contain, in order as the file, each value of profit/losses with size =n 
a=[]
n=0

#b:will contain the changes in Profit/Losses with size k
b=[]
k=0

#c: will contain, in order as the file, each date with size =n 
c=[]
#d:will contain the date of changes with size k
d=[]

#open the csv file to read
with open (csvpath) as csvfile:
    
    #the delimiter of each row is ,
    csvreader= csv.reader(csvfile, delimiter =",")
    
    #skeep the header 
    csv_header=next(csvreader)
    #loop in the file
    for row in csvreader:
        #number of months
        nbr_m = nbr_m + 1
       
        # net total amount
        net_amount = net_amount + float(row[1])
        
        #assign the value of each profit/lost and their date respectively to the lists a and c
        a.append(float(row[1]))  
        c.append(row[0])
       #incremented n to save the size of our lists
        n=n+1
    #print the total of months    
    print('Total Months: ',nbr_m,'\n')
    
    #print net amount
    print ('Total: ', round(net_amount),'\n')
    
    #assign the changes of each profit/loses and their dates respectively in list b and d
    for j in range (n-1):
        
        x=((a[j+1]-a[j]))
        y=c[j+1]
        b.append((x))
        d.append(y)
        #incremented n to save the size of our lists
        k=k+1
    
    #initialise the sum of the list of the changes to 0
    s=0
    #loop in all the list b to calculate the sum of the changes
    for i in range (k):
      s=s+b[i]  
    #calculate the average of the changes
    avg= s/(k)
    #print the average
    print('Average change ',round(avg,2),'\n')
    # look for the greatest change's increase and the greatest chage's decrease and their dates    
    max=0
    pmax=0
    min=0
    pmin=0
    #loops to look for the max and the min and their positions in the list b
    
    for i in range (k):
        if b[i]< min:
            min=b[i]
            pmin=i
    for j in range (k):
        if b[j]> max:
            max=b[j]
            pmax=j  
   
   
    #look for the dates with the min and max position in the list d and print the greatest decrese with its date and the greatest increase with its date
    h = 0
    stop= False
    while(stop==False) or (h>=k):
        if h == pmax: 
            stop=True
        else: h=h+1
    
    print('Greatest Increase in Profits',d[h],'($',round(max),')','\n')
               
    h = 0
    stop= False
    while(stop==False) or (h>=k):
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
    ch='Total Months: '+str(nbr_m)+'\n'+'\n'
    f.write(ch)
    ch= 'Total: '+str (round(net_amount))+'\n'+'\n'
    f.write(ch)
    ch= 'Average change: '+str(round(avg,2))+'\n'+'\n'
    f.write(ch)
    ch= 'Greatest increase: '+str(round(max))+'\n'+'\n'
    f.write(ch)
    ch= 'Greatest decrease: '+str(round(min))+'\n'+'\n'
    f.write(ch)
    
