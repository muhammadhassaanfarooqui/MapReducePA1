#!/usr/bin/env python
# map function for matrix multiply
#Input file assumed to have lines of the form "A,i,j,x", where i is the row index, j is the column index, and x is the value in row i, column j of A. Entries of A are followed by lines of the form "B,i,j,x" for the matrix B. 
#It is assumed that the matrix dimensions are such that the product A*B exists. 

#Input arguments:
#m should be set to the number of rows in A, p should be set to the number of columns in B.
 
import sys
import string
import os

#(os.environ['mapreduce_map_input_file'].contains("parking"))

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    lineArr = line.strip().split(',')
    plateID = lineArr[14];
    regState = lineArr[16];
    print plateID + ', ' + regState + '\t' + '1'
        
