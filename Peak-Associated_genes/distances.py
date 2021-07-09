#!/bin/python
#finds the distance between peak summits and the nearest translation start site
#usage = python distances.py -s <strand file name> -b <peak file name in bed format> >> <outputfile>

#to read the files
import csv
#to read in the arguments
import argparse

#argparse lines in every script
parser = argparse.ArgumentParser(description='find distances between translation start sites and peaks')
parser.add_argument("-s","--strands",help="strand file that is just strand and gene ids separated by a tab")
parser.add_argument("-b","--bed",help="bed file that has peak summits and the upstream locations they are in")
args = parser.parse_args()

#read in the files with each line as an entry in a list
with open(args.bed) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter='\t')
    b = list(reader)
with open(args.strands) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter='\t')
    s = list(reader)

#for every line in the peak file
for i in b:
    #define a variable that is just the gene ID
    gene = i[8].split('_')[0]
    #loop through the lines of the strand file
    for j in s:
        #if the gene ID of interest is in the strand line you're on
        if gene == j[1]:
            #if the entry for that gene is on the plus strand
            if j[0] == "+":
                #define a variable that is the summit location substracted from the translation start site
                distance = int(i[7])-int(i[2])
                #print a line that is the gene id and the distance separated by a tab
                #this will be redirected to a file
                print(str(gene) + '\t' + str(distance))
            if j[0] == "-":
                distance = int(i[1])-int(i[6])
                print(str(gene) + '\t' + str(distance))
