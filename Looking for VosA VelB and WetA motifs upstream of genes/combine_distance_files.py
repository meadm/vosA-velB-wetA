#!/bin/python
#combines the different distance files
#usage = python distances.py -w <wetA distance file> -o <vosA distance file> -e <velB distance file> -u <file of unique but concatenated upstream genes> >> <outputfile>

#to read the files
import csv
#to read in the arguments
import argparse
import re

#argparse lines in every script
parser = argparse.ArgumentParser(description='combine three distance files')
parser.add_argument("-w","--weta",help="wetA distance file")
parser.add_argument("-o","--vosa",help="vosA distance file")
parser.add_argument("-e","--velb",help="velB distance file")
parser.add_argument("-output",help="output file name")
args = parser.parse_args()

#read in the files with each line as an entry in a list
with open(args.weta) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter='\t')
    weta = list(reader)
with open(args.vosa) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter='\t')
    vosa = list(reader)
with open(args.velb) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter='\t')
    velb = list(reader)

newList=[]

for i in vosa:
    newList.append(i)
    InVelB = False
    for j in velb:
        if i[0] == j[0]:
            InVelB = True
            newList[newList.index(i)].append(j[1])
    if not InVelB:
        newList[newList.index(i)].append('-')
    InWetA = False
    for k in weta:
        if i[0] == k[0]:
            InWetA = True
            newList[newList.index(i)].append(k[1])
    if not InWetA:
        newList[newList.index(i)].append('-')

for j in velb:
    InNewList = False
    for l in newList:
        if j[0] == l[0]:
            InNewList = True
    if not InNewList:
        newEntry = [j[0], '-', j[1]]
        newList.append(newEntry)
        InWetA = False
        for k in weta:
            if j[0] == k[0]:
                InWetA = True
                newList[newList.index(newEntry)].append(k[1])
        if not InWetA:
            newList[newList.index(newEntry)].append('-')

for k in weta:
    InNewList = False
    for l in newList:
        if k[0] == l[0]:
            InNewList = True
    if not InNewList:
        newEntry = [k[0], '-', '-', k[1]]
        newList.append(newEntry)

with open(args.output, 'w') as f:
    f.writelines('\t'.join(i) + '\n' for i in newList)
