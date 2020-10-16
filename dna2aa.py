# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:39:06 2020

@author: Larissa
"""
''' 
Description: 
    This program will 

List of user defined functions (if any):

List of modules used that are not explained in the course material:
    sys - module for using system specific parameters and functions. In this case for getting command line parameters

Procedure:
    1.
    2.
    3.
    4

Usage:
    


 '''

#Create a dictionary key:codons, stop codon; value:amino acid, *

codon_dict = {'AAA':'K','AAT':'N','AAC':'N','AAG':'K',\
              'ATA':'I','ATT':'I','ATC':'I','ATG':'M',\
            'ACA':'T','ACT':'T','ACC':'T','ACG':'T',\
            'AGA':'R','AGT':'S','AGC':'S','AGG':'R',\
            'TAA':'*','TAT':'Y','TAC':'Y','TAG':'*',\
            'TTA':'L','TTT':'F','TTC':'F','TTG':'L',\
            'TCA':'S','TCT':'S','TCC':'S','TCG':'S',\
            'TGA':'*','TGT':'C','TGC':'C','TGG':'W',\
            'CAA':'Q','CAT':'H','CAC':'H','CAG':'Q',\
            'CTA':'L','CTT':'L','CTC':'L','CTG':'L',\
            'CCA':'P','CCT':'P','CCC':'P','CCG':'P',\
            'CGA':'R','CGT':'R','CGC':'R','CGG':'R',\
            'GAA':'Z','GAT':'D','GAC':'D','GAG':'Z',\
            'GTA':'V','GTT':'V','GTC':'V','GTG':'V',\
            'GCA':'A','GCT':'A','GCC':'A','GCG':'A',\
            'GGA':'G','GGT':'G','GGC':'G','GGG':'G'}
        
    
#Open and read input file:
         
with open('regions.fna', 'r') as input_file,\           #opens input file
    open('converted_aa_seq_2.txt', 'a') as aa_seq:      #opens newly created output file in 'a'-mode
                                                        #refering to it as aa_seq
                                                    #Take header from fasta_file:
    for line in input_file:                         #goes through lines in input_file
        if '>' in line:                             #if the line contains >
            header = line[1:]                       #take line but only up from first object (cuts off >);
                                                    #and strips off any trailing characters
            aa_seq.write('\n' +">rf 1 "+ header)    #concatenating newline, >rf1 and headerline
                
                                                                    #Put DNA into triplets:
    if not '>' in line:                                             #if no > in line
        triplets = [line[i:i+3] for i in range(0, len(line), 3)]    #puts line into triplets
    
                                                            #Loop through triplet, match dictionary value:
            for item in triplets:                           #loop through items in triplets
                if item in codon_dict:                      #yeees! Has added it!!
                    amino_acid = codon_dict[item]           #gets the corresponding value of the key in dictionary
                    aa_seq.write(amino_acid)                #appends amino_acid to output file aa_seq
                                                            #after having inserted a new line
                                                                                                      

#the aa_seq has been created and added to output file!! Yay :-) 
#what else to do: what to do with input files that do not contain 'ACTG'
    

