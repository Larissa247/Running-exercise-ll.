# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:51:47 2020

@author: Larissa
"""

barcode_list = ['TATCCTCT','GTAAGGAG','TCTCTCCG']       #create list containing barcodes
                                                        #open input file as in_f:
with open('barcode.fastq','r') as in_f,\
    open('trimmed_barcodes.txt', 'a') as out_f,\
    open('no_barcode_match.txt', 'a') as no_match:      #output file for barcode-matching sequences = out_f
                                                        #output file for non-matching sequences = no_match                                                                
                    
    for lines in in_f:
        if lines[0:8] in barcode_list:          #if these barcodes occur in first 8 letters of the line
            stripped_line = lines[8:]           #take the line but without the first 8 elements
            out_f.write(stripped_line)          #and add the stripped line to output file
                
        if lines[0:8] not in barcode_list:
            if ('A' and 'C' and 'G' and 'T') in lines:    
                no_match.write(lines)