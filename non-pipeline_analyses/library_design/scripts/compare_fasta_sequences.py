

# Import packages
import pandas as pd
import os
from Bio import SeqIO



gisaiddir = 'GISAID_query'
gisaid_download = 'GISAID_download_9-Oct-2023'




nextclade_sequences = SeqIO.parse(open(os.path.join(gisaiddir, gisaid_download, 'nextclade_isolate_HAprot.fasta')),'fasta')


auspice_sequences = SeqIO.parse(open(os.path.join(gisaiddir, gisaid_download, 'auspice_isolate_HAprot.fasta')),'fasta')
auspice_ls = []
for fasta in auspice_sequences:
    header, sequence = fasta.id, str(fasta.seq)
    name = header.split('|')[0]
    auspice_ls.append([name, sequence])





counter = 0

nextclade_ls = []
for fasta in nextclade_sequences:
    header, sequence = fasta.id, str(fasta.seq)
    name = header.split('|')[0]
    nextclade_ls.append([name, sequence])
    if 'X' in sequence:
    	print(name)

    for strain in auspice_ls:
    	ref_Name = strain[0]
    	ref_Seq = strain[1]

    	if sequence == ref_Seq:
    		print(f'NextClade seq {name} has a match in Auspice list {ref_Name}')
    		counter += 1






print(f'There are {counter} sequences in NextClade set that overlap with Auspice set...')
print(f'This means there are {len(nextclade_ls)-counter} NextClade sequences that are AA-level unique...')



