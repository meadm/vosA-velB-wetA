#1/bin/bash
for num in {1..3}; do
	grep 'AN' WT/WT_${num}.htseq | sed 's/-T//' > WT/WT_${num}_2.htseq
	grep 'AN' VosA/VosA_${num}.htseq | sed 's/-T//' > VosA/VosA_${num}_2.htseq
	grep 'AN' VelB/VelB_${num}.htseq | sed 's/-T//' > VelB/VelB_${num}_2.htseq

done
