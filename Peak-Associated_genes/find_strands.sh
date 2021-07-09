#!/bin/bash
while read LINE; do
    STRAND=$(echo $LINE | cut -d ' ' -f7,7)
    GENE=$(echo $LINE | cut -d '=' -f2,2 | cut -d';' -f1,1)
    echo $STRAND"   "$GENE >> strands_ids.txt
done < $1
