#!/bin/python
#takes a distance file and puts all the duplicate genes on the same line

#to read the file
import csv
#for giving a file name
import argparse


#argparse lines in every script
parser = argparse.ArgumentParser(description='Take a distance file and put all the duplicate genes on the same line with the distances separated by commas')
parser.add_argument("-f", "--file", help="files to be parsed")
args = parser.parse_args()

#load file as a list of lists - each line is a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter='\t')
    file = list(reader)

#newList will contain the output to be printed
newList=[]

#for every line (distance entry) in the file
for i in file:
    #assume that it is a unique gene and not yet in newList
    unique = True
    #loop through every entry in newList
    for j in newList:
        #if the gene from the file is already in newList
        if i[0] == j[0]:
            unique = False
            #change the entry for that gene to the orignal distance concatenated wiht a comma and the new, second distance
            j[1]=j[1] + ',' + i[1]
    #if the gene from the file is unique, add it to newList
    if unique:
        newList.append(i)

#print newList to a file named "test.txt"
with open('test.txt', 'w') as f:
    f.writelines('\t'.join(i) + '\n' for i in newList)
