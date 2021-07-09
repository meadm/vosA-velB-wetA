#!/bin/python
#pulls gene ids from a BED format file that is the result of a "bedtools intersect" command and prints the gene IDs to standard output

#to read the file
import csv
#for giving a file name
import argparse
#for parsing the lines
import re

#argparse lines in every script
parser = argparse.ArgumentParser(description='Pull gene IDs associated with Exons and Introns')
parser.add_argument("-b","--bed",help="intersection BED file to be parsed")
args = parser.parse_args()

#read in the file with each line as an entry in a list
with open(args.bed) as mainfilehandle:
    reader = csv.reader(mainfilehandle)
    l = list(reader)

#the gene list will eventually contain all the gene ids plus whatever extraneous identifiers they might have like "-T"
gene=[]

#for every entry (line) in the list, split the line based on the delimiters of "ID=" and ";"
#add the gene ids and extras to the list called "gene"
for entry in l:
    split=re.split('ID=|;',entry[0])
    gene.append(split[1])

#if there is a dash in the gene ids, don't worry about it and move on to the next line
#every gene has an clean entry and an entry with "-T" or something similar
for i in gene:
    if not '-' in i:
        print(i)
