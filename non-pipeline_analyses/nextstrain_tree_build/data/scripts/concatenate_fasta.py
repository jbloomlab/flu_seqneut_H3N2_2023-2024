'''
concatenate_fasta.py

Takes directory of files, looks for FASTA formatted files and concatenates them.
See usage to toggle input and output. 

'''

import os
import shutil

def concatenate_fasta_files(target_dir, output_file):
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(target_dir):
            if filename != output_file:
                if filename.endswith(".fasta") or filename.endswith(".fa"):
                    file_path = os.path.join(target_dir, filename)
                    print(f'Found {file_path}, reading...')
                    with open(file_path, 'r') as infile:
                        # Use shutil.copyfileobj to efficiently copy content
                        print(f'Copying to {output_file}')
                        shutil.copyfileobj(infile, outfile)
                    

# Usage
target_dir = './download'
output_file = './concatenated_files/raw_sequences_ha.fasta'
os.makedirs('./concatenated_files', exist_ok=True)
concatenate_fasta_files(target_dir, output_file)
print('Done.')

