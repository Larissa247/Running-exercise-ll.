# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:46:51 2020

@author: Larissa
"""

#Create a new dictionary with amino acids as key and value as amount starting at 0

aa_dict = {'A':0,'R':0,'N':0,'D':0, 'C':0, 'Q':0,\
          'E':0,'H':0,'I':0,'L':0,'K':0,'M':0,'F':0,\
        'P':0,'S':0,'T':0,'W':0,'Y':0,'V':0,'X':0}
        

#Open input file (from user) and convert to uppercase letters:
with open('converted_aa_seq_edit.txt','r') as aa_file:
        
    for line in aa_file:                    #for line in the input file
        if not '>' in line:                 #only aa-sequences are considered (no headers)
            line = line.upper()             #conversion to uppercase letters
                
            for letter in line:               #loop through line and regard each letter
                if letter in aa_dict:         #if letter occurs in the dictionary
                    aa_dict[letter] += 1      #dictionary[of key] update the value of a dictionary
                        
                else:                         #else: if letter not found in dictionary
                    aa_dict['X'] += 1         #increase count of key 'X'                    

                                                            #Conversion of dictionary to list for right formatting:     
with open('aa_abundance_2.txt','a') as output_file:         #open output file
        
    aa_list = list(aa_dict)                                 #create list
    for letter in aa_list:                                  #for 'key' letter in the list
        number = aa_dict[letter]                            #define number as value of the dictionary
        output_file.write(f"{letter} {number}" + '\n')      #add key and value of dictionary to output_file
                                                            #add newline
                                                            
                                                            
                                                            