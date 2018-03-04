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
    print line
    if (line[0] == 'P'):
        line = line[1:]
        # print line
        arr = line.strip().split(',')
        summ = arr[0]
        pid = arr[1]
        issueDate = arr[4]
        vCode = arr[5]
        precinct = arr[14]
        print(summ + "\t" + "P, " + pid + ", " + issueDate + ", " + vCode + ", " + precinct)
    else:
        arr = line.strip().split(',')
        summ = arr[3]
        print (summ + "\t" + "O")
        
