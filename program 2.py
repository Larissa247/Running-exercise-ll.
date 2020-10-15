# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:50:55 2020

@author: Larissa
"""

#user input: choose one of the 4 options: 1,2,3,4


#If 1 --> convert DNA to amino acids

#create a dictionary key:codons; value:amino acid (TAG:*)
  
    #open and read file:
    #for line in file:
        #if '>' in line:
            #line = line[1:]
            #outputfile.append(">rf 1 "+ line) #concatenating >rf1 and header line
         
        #if not '>' in line:
            #look for the keys in the sequence, get value amino acid (for loop)
            #get the value only if sequence contains 'ACTG'
        
            #an output will be created
            #add this to outputfile (extend/append)
        
        
            #else: print('not supported')
           

#IF 2 --> counting absolute aa abundance

#open the outputfile (just created) or another new file (from user)

#create a new dictionary with amino acids as key and value as amount starting at 0
    
#for line in file:
    #if not '>' in line:
        #if key in line:
            #count += 1
            #value for that key = count
            
        #if not amino acid:
            #put in key:X
            
       #make list of dict:
           #for key in list
           #value = dictionary[key]
           #f"{key} {value}" 
       
#print(dictionary) in outputfile2


# IF 3 --> Match barcodes TATCCTCT, GTAAGGAG, and TCTCTCCG with DNA in input file

#create new outputfile3 (should contain matches) and 4 (not-matched)

#outputfile3/4.append(">"
#count = 0

#for lines in inputfile 3:  
    #if match:
        #count += 1
        #outputfile3.append(">" + count +'\n'+ matched_line)
        
    #else:
        #count += 1
        #outputfile4.append(">" + count +'\n'+ matched_line)
        

#IF 4 --> run program 1
        

   
    

    
    