# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 09:40:57 2020

@author: Larissa
"""

'''We want to calculate how well two DNA sequences align to each other. 
If we have a match between two nucleotides in a given position it will be scored +1. 
If we have a transition, a<->g or c<->t, the penalty will be -1 and if it is a transversion (any other substitution) the penalty will be -2. 
A gap gives the score -1. A figure showing transitions/transversions is found here:'''


#Unzip and retrieve the data files
import tarfile
my_tar = tarfile.open('Running Exercise 2-1.tgz')
my_tar.extractall('./data') #to specify which folder to extract to
my_tar.close()

my_tar = tarfile.open('Running Exercise 2-2.tgz')
my_tar.extractall('./data') #to specify which folder to extract to
my_tar.close()

#Solution part 1
#Create function:
    #def alignment_score(x):
        
        
        
#Opening and reading file

#Use the zip() function in python that takes two separate strings as tuples
#they can be compared pairwisely to each other

#list_ids = []
#list_DNA = []

#for line in file:
    #if not '>':
        #if 'ATGC-':     #makes sure only aligned DNA sequences are added
            #list_DNA.append(line)
        
    #else:
        #list_ids.append(line)
        
        
# pair = zip(list_DNA[0], list_DNA[1]) #would compare element 1 and 2 of list

#def score_function():
    #for x,y in pair: #a,b relates to a=list_DNA[0], b=list_DNA[1]    

    #if x == y:
        #if x,y not '-':
            #score += 1
        #if x,y '-':
            #score += 0
            
    
    #if x != y:
        #if (x or y) == '-':
            #score -= 1
            
        #if (x in 'AG' and y in 'CT') or (x in 'CT' and y in 'AG'):
            #checks if x is a substring of 'AG'
            #score -= 1
            
        #else:              #this will account for transversion
            #score -= 2

    #return score

#Create a nested for loop that iterates through the ids:
for i in list_DNA:
    i = 0
    for x,y in zip(list_DNA[i],list_DNA[i+1]) as compare: #nested loop, and zip()
    result = score_function(compare) #call the function
    
    #put result/score of function into outputfile:
    output_file.append('list_id[i] + '-' + list_id[i+1] + ': Score=' + result')
   
    i = i +1
                
        
        

       
#Use score_function()
#for list_DNA[0:] and list_DNA[1:]

            
#Print the score and the compared ids in output_file

            

#for line in file:
    #if not '>':
        #character = line.split() #split at each occurence, character is a list
        #
        

#for value in the dictionary:
    
    
    #if 




#Reading input file
with open('score.fna', 'r') as score_file:
       
    #read the lines 
    lines = score_file.readlines()
    
    #create a dictionary and add ids as keys and sequence as values 
    
    for lines in score_file: #loops through lines
        info = lines.split('\t') #
        
    
        
        

#Reading input files

    
    #QC on user input
        #Does the file exist?
        
        #
        
        #
    
    #loading the files
    
        #QC


#Solution to part I

#Call function that manages input from user
read_file ('d:\file')

#QC: check alingment



#Calculate score

#Prepare output to write to files

#Writing output to file
