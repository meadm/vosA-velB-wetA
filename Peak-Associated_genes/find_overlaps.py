#!/bin/python
#given three files that only contain single columns of gene ids, identify every overlapping group and print the results to individual files
#ex gene A is in list 1 and list 2 but not in list 3. put it in a file called list1_list2.txt

#to read the file
import csv
#for giving a file name
import argparse


#argparse lines in every script
parser = argparse.ArgumentParser(description='Find genes of all potential overlaps and specificities')
#nargs="+" tells argparse that there can be multiple inputs for that argument - ie multiple files
#NOTE, files must be in the order of WetA, VelB, VosA
parser.add_argument("-f", "--files", nargs="+", help="files to be parsed")
args = parser.parse_args()

#0 = WetA
#1 = VelB
#2 = VosA

# read in the files with each line as an entry in a list
wetA=[]
for line in open(args.files[0]):
    wetA.append(line.strip('\n'))

velB=[]
for line in open(args.files[1]):
    velB.append(line.strip('\n'))

vosA=[]
for line in open(args.files[2]):
    vosA.append(line.strip('\n'))

##########Start WetA#########
#wetA and vosA but NOT velB
#get ready to write a text file
with open('wetA_vosA.txt', 'w') as f:
    writer = csv.writer(f)
    for i in wetA:
        for j in vosA:
            if i == j:
                check = True
                for k in velB:
                    if i == k:
                        check = False
                if check:
                    #brackets "[]" are important
                    writer.writerow([i])

#wetA and velB but NOT vosA
with open('wetA_velB.txt', 'w') as f:
    writer = csv.writer(f)
    for i in wetA:
        for k in velB:
            if i == k:
                check = True
                for j in vosA:
                    if i == j:
                        check = False
                if check:
                    writer.writerow([i])

#in all three
with open('wetA_vosA_velB.txt', 'w') as f:
    writer = csv.writer(f)
    for i in wetA:
        for j in vosA:
            if i == j:
                for k in velB:
                    if i == k:
                        writer.writerow([i])

#wetA ONLY
with open('wetA_only.txt', 'w') as f:
    writer = csv.writer(f)
    for i in wetA:
        firstCheck = True
        for j in vosA:
            if i == j:
                firstCheck = False
        secondCheck = True
        for k in velB:
            if i == k:
                secondCheck = False
        if secondCheck and firstCheck:
            writer.writerow([i])
##########End WetA#########

##########Start VelB#######
#VelB and VosA but not WetA
with open('velB_vosA.txt', 'w') as f:
    writer = csv.writer(f)
    for i in velB:
        for j in vosA:
            if i == j:
                check = True
                for k in wetA:
                    if i == k:
                        check = False
                if check:
                    writer.writerow([i])

#VelB ONLY
with open('velB_only.txt', 'w') as f:
    writer = csv.writer(f)
    for i in velB:
        firstCheck = True
        for j in vosA:
            if i == j:
                firstCheck = False
        secondCheck = True
        for k in wetA:
            if i == k:
                secondCheck = False
        if secondCheck and firstCheck:
            writer.writerow([i])
##########End VelB#########

##########Start VosA#######
#VosA Only
with open('vosA_only.txt', 'w') as f:
    writer = csv.writer(f)
    for i in vosA:
        firstCheck = True
        for j in velB:
            if i == j:
                firstCheck = False
        secondCheck = True
        for k in wetA:
            if i == k:
                secondCheck = False
        if secondCheck and firstCheck:
            writer.writerow([i])
