# python-challenge
# How to use Python to read information from a CSV file, manipulate it, and return results into a text file: :cd:

In this project we have two parts: 
- Analyze the financial records of a company
- Modernize the vote-counting process of a small, rural town

# What we will learn from this project:

    - How to import modules like csv
    - How to use the right instructions and data structures
    - How to export a text file with the results
    
# Instructions:
## PyBank
    - Open and read an existing dataset about Profits/Losses from a CSV file
    - Calculate the total number of months included in the dataset
    - Calculate the net total amount of "Profit/Losses" over the entire period
    - Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
    - Look for the greatest increase in profits (date and amount) over the entire period
    - Look for the greatest decrease in profits (date and amount) over the entire period
    - Print all the results on the terminal
    - Write all the outputs resulting from analysis in a text file
    
## PyPoll
    - Open and read an existing dataset about votes from a CSV file
    - Calculate the total number of votes cast
    - Create a complete list of candidates who received votes
    - Calculate the percentage of votes each candidate won
    - Calculate the total number of votes each candidate won
    - Look for the winner of the election based on popular vote
    - Print all the results on the terminal
    - Write all the outputs resulting from analysis in a text file

#  Program:

## PyBank:

### Resources: budget_data.csv
![screenshot for resources](/budget_data.png)

### Analysis: budget_data.txt
![screenshot for resources](/budget_data.txt.png)

### Python script: main.py
```
#loop in the file
    for row in csvreader:
       
        # net total amount
        net_amount = net_amount + float(row[1])
        
        #assign the value of each profit/losses and its date respectively to the lists a and c
        a.append(float(row[1]))  
        c.append(row[0])
    
    #assign the changes of each profit/losses and their dates respectively in list b and d
    for j in range (len(a)-1):
        
        x=((a[j+1]-a[j]))
        y=c[j+1]
        b.append((x))
        d.append(y)
        
    #calculate the average of the changes
    avg= sum(b)/len(b)

    max=max(b)
    min=min(b)
    pmax=b.index(max)
    pmin=b.index(min)
```

## PyBank:

### Resources: budget_data.csv
![screenshot for resources](/election_data.png)

### Analysis: budget_data.txt
![screenshot for resources](/election_data.txt.png)

### Python script: main.py
```
#loop in the file
    for row in csvreader:
        
        #assign the value of names to the list a 
        a.append(row[2])  
    #sort the list a 
    a.sort()
    
    #fill the list b with condidate names without redundancy
    b.append(a[0])
    
    for i in range (len(a)-1):
        
        if a[i]!=a[i+1]:
            b.append(a[i+1])
            
    #count the number of votes for each candidate and save it in the list c        
    for i in range (len(b)):   
        l=0
        for j in range (len(a)): 
           if a[j]==b[i]:
               l=l+1
        c.append(l)
    
    #print the name of each candidate with the percentage of their votes and the total of their votes 
    for i in range (len(c)):
        print(b[i],':', round(c[i]/len(a)*100,3),'% (',c[i],')','\n')
    
    x=max(c)
    p=c.index(x)
```   
# Tip:🪄
  
Python offers huge libraries with multiple predefined functions and methods to facilitate programming. Here are some examples:
- len: Returns the length of a list
- sum: Returns the total of all elements in a list instead of a whole loop
- min and max: Return the minimum and the maximum values in a list
- index: Returns the value of an index in a list

--> Code to look for the maximum and its index in a list with loops:😒
```
    max=0
    pmax=0
    #look for the max in a list
    for j in range (len(b)):
        if b[j]> max:
            max=b[j]
            pmax=j  
   
    #look for the index of the max in a list
    h = 0
    stop= False
    while(stop==False) or (h>=len(b)):
        if h == pmax: 
            stop=True
        else: h=h+1
```
 --> Code to look for the maximum and its index in a list with the function max and the method index: 😊
 ```
     max=max(b)
     pmax=b.index(max)
 ```
- Sort(): Forget about sorting algorithms and how complicated they are! one simple call and your list is sorted! 😍
