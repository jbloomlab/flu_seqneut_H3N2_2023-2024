'''
make_strain_to_id_map.py

Author: Caroline Kikawa
Description: Get all strain names and IDs from downloaded FASTA and write to concatenated_files

'''

# Imports
import pandas as pd

def get_fasta_headers(fasta_file):
    headers = []
    with open(fasta_file, 'r') as file:
        for line in file:
            if line.startswith('>'):
                headers.append(line.strip('>').strip().split('|'))

    return headers

def list_to_csv(list_of_lists, outfile):
    df = pd.DataFrame(list_of_lists, columns = ['strain', 'GISAID_id'])
    df.to_csv(outfile, index=False)
    


# Main method
if __name__ == "__main__":
    file = 'concatenated_files/raw_sequences_ha.fasta'
    outfile = 'concatenated_files/strain_to_id_map.csv'

    ls = get_fasta_headers(file)
    list_to_csv(ls, outfile)
    