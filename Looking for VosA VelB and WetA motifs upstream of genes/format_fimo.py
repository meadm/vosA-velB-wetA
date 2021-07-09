#!/bin/python
#finds the distance between peak summits and the nearest translation start site
#NOTE: this script only works when using 1.5kb upstream of translation start
#usage = python format_fimo.py -i <input FIMO file in default format> -o <name of file to write output to>

import pandas as pd
import argparse

#argparse line that is in all argparse scripts
parser = argparse.ArgumentParser(description='Reformat a FIMO output so that the resulting file only has the gene and the location of the start of the motif upstream of the translation start site')
#add argparse variable for the input file
parser.add_argument("-i","--input",help="input FIMO file")
#add argparse variable for the output file
parser.add_argument("-o","--output",help="output file")
#send the arguments to a variable
args = parser.parse_args()

#read in the original FIMO file as a pandas dataframe
#the default files are separated by tabs so `sep='\t'` is needed
original = pd.read_csv(args.input, sep='\t')

#make a copy of the original dataframe and only pull the gene name and where the motif begins relative to the beginning of the sequence I gave FIMO
result = original[['sequence_name', 'stop']].copy()

#make a new column in the dataframe called `location` that is where the motif starts, relative to the translation start
result['location'] = 1500 - result['stop']

#get rid of the old column that was relative to the beginning of the sequence (1.5kb away from translation start)
result = result.drop('stop', axis=1)

#write the dataframe to a file with tab delimiters and don't write the indexes pandas adds to dataframes
result.to_csv(args.output, sep='\t', index=False)
