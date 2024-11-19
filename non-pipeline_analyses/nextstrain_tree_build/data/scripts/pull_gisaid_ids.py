'''
pull_gisaid_ids.py

Description:
Takes a JSON-stripped TSV of strain names with columm ['name'] and matches to 
a Nextclade metadata.tsv with column ['seqName', 'ha_accession'] and
saves a TSV of GISIAD accesions to user-defined outfile.

Author: Caroline Kikawa

'''


# Import packages
import pandas as pd
import numpy as np

# Functions for opening and merging TSVs, returning 
# number of matches, number of mismtaches, and
# ['ha_accession'] column to save as TSV

def merge_tree_and_nextclade_metdata(treefile, nextcladefile):
    
    # Get DataFrames from input
    tree_df = pd.read_csv(treefile, sep = '\t')
    nextclade_df = pd.read_csv(nextcladefile, sep = '\t').rename(columns = {'seqName': 'name'})
    
    # Merge DataFrames
    merged_df = tree_df.merge(nextclade_df, on=['name'], how = 'left')
        
    # Count strain names to compare those with matched HA accessions
    entries = len(merged_df)
    entries_with_matches = len(merged_df[['name', 'accession_ha']].dropna(axis=0))
    
    # Get array of HA accessions
    ha_accessions = merged_df[['name', 'accession_ha']].dropna(axis=0).accession_ha # Drop rows with na

    # Some of these accessions have the string pattern "EPIEPI######"
    # This is some sort of type that totally messes up the GISAID search

    i=0 # Initialize accession count
    epiepi_accessions = [] # Initialize EPIEPI accessions list
    cleaned_ha_accessions = [] # Initialize string-replaced HA accessions list
    
    for accession in ha_accessions:
        if 'EPIEPI' in accession:
            epiepi_accessions.append(accession) # Append to EPIEPI list
            accession = accession.replace('EPIEPI', 'EPI') # String replace

        cleaned_ha_accessions.append(accession) # Add accession to cleaned list

    return entries, entries_with_matches, cleaned_ha_accessions, epiepi_accessions


def save_array_to_tsv(array, outfile):
    # Use built-in array to TSV
    np.savetxt(outfile, array, delimiter='\t', header='accession_ha', fmt='%s') # Save format as strings


# Main method
if __name__ == "__main__":

    json_table_file = 'trees_and_metadata/flu_seasonal_h3n2_ha_2y_metadata.tsv'
    nextclade_metadata_file = 'trees_and_metadata/nextclade_metadata_h3n2_2023-11-21.tsv'

    outfile = 'download/2y_nextstrain_tree_ha_accesions.tsv'

    entries, entries_with_matches, ha_accessions, epiepi_accessions = merge_tree_and_nextclade_metdata(json_table_file, nextclade_metadata_file)

    print(f'Identified {entries} sequence names in JSON table file...')
    print(f'Identfied {entries_with_matches} sequences with HA accessions in Nextclade metadata file...')
    print(f'There are {len(epiepi_accessions)} accessions with "EPIEPI" pattern, but they have been string replaced with "EPI"...')
    
    print(f'Saving HA accessions to {outfile}...')
    save_array_to_tsv(ha_accessions, outfile)





