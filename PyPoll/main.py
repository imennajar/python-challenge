#Import the library csv 
import csv

#Import the library os 
import os

#Declare the path of the csv file from where we will read information
csvpath= os.path.join("PyPoll/resources","election_data.csv")

#Declare the path of the text file where we will write the results
output_path=os.path.join("PyPoll/analysis","result.txt")

#Print the header on the terminal
print('Election Results')
print('---------------------------------------------------------','\n')

#Declare 4 lists: 
#a:will contain, in order as the file, condidat's name
a=[]


#b:will contain condidat's name without redundancy
b=[]

#c: will contain the number of vote for each condidate
c=[]

#open the csv file to read
with open (csvpath) as csvfile:
    
    #assign each element in the list to csvreader
    csvreader= csv.reader(csvfile, delimiter =",")
    
    #skeep the header 
    csv_header=next(csvreader)
    
    
    #loop in the file
    for row in csvreader:
        
        #assign the value of names to the list a 
        a.append(row[2]) 
        
    #print the total of vote
    print('Total of votes: ',len(a),'\n')
    print('---------------------------------------------------------','\n')
    
    #sort the list a 
    a.sort()
    
    #fill the list b with names without redundancy
    b.append(a[0])
    
    for i in range (len(a)-1):
        
        if a[i]!=a[i+1]:
            b.append(a[i+1])
            
    #count the number of vote of each condidate  and save it in the list c        
    for i in range (len(b)):   
        l=0
        for j in range (len(a)): 
           if a[j]==b[i]:
               l=l+1
        c.append(l)
    
    #print the name of each condidat with the percentage of their votes and the total of their votes 
    for i in range (len(c)):
        print(b[i],':', round(c[i]/len(a)*100,3),'% (',c[i],')','\n')
    
    print('---------------------------------------------------------','\n')
    
    #look for the maximum of the number of vote and the name of that condidat 
    max=c[0]
    p=0
    for i in range(len(c)):
        if c[i]>max:
            max=c[i]
            p=i
    
    #print the result
    print('Winner:',b[p],'\n')
    
    print('---------------------------------------------------------','\n')        
            
#open the file text to write our result    
with open(output_path,'w') as f:
    #put each result in a variable and add it to the file
    ch='Election Results'+'\n'+'\n'
    f.write(ch)
    ch='------------------------------'+'\n'+'\n'
    f.write(ch)
    ch='Total Votes: '+str(len(a))+'\n'+'\n'
    f.write(ch)
    ch= '---------------------------'+'\n'+'\n'
    f.write(ch)
    for i in range (len(b)):
        ch= (str(b[i])+':'+ str(round(c[i]/len(a)*100,3))+'% ('+str(c[i])+')'+'\n'+'\n')
        f.write(ch)
    ch= '---------------------------'+'\n'+'\n'
    f.write(ch)
    ch=('Winner:'+ str(b[p]))+'\n'+'\n'
    f.write(ch)
    ch= '---------------------------'+'\n'+'\n'
    f.write(ch)
        