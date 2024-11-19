# Downloading and processing H3N2 sequences from GISAID
Author: Caroline Kikawa

## Quick summary
I want to create a custom `seasonal-flu` build using my 2023-2024 `seqneut` library strains and the 2-year nextstrain build available at time of library generation. 
I can't use the 2-year tree on it's own, because the library includes some strains that weren't in the 2-year build at the time. 
These strains include high-frequency HA haplotypes that I identified using Nextclade datasets,
and recent historical egg- and cell-passaged vaccine strains. 

## Build `conda` virtual environment
An environment is specified in the top-level directory in [environment.yml](../../../environment.yml), build and activate with:

    conda env create -f environment.yml
    conda activate nextstrain

## Identifying 2-year tree strains to download
I used a script by John Huddletston to pull strain names, GISAID IDs, and a bunch of other information from a JSON tree file.
This script is placed in [scripts/auspice_tree_to_table.py](scripts/auspice_tree_to_table.py), and ran with:

    python scripts/auspice_tree_to_table.py --tree trees_and_metadata/flu_seasonal_h3n2_ha_2y.json --output-metadata trees_and_metadata/flu_seasonal_h3n2_ha_2y_metadata.tsv

I then pulled GISAID IDs and save those IDs to an output TSV, placed in [data/2y_nextstrain_tree_ha_accesions.tsv](data/2y_nextstrain_tree_ha_accesions.tsv)
This script is run with:

    python scripts/pull_gisaid_ids.py 

The resulting list of GISAID IDs to query is placed in [download](download).

## Identifying library strains to download
I needed to re-download library strains because it appears I didn't download all the relevant metadata at the the time of library generation.
I used the GISAID IDs associated with each strain, placed in [download/library_ha_accessions.csv](download/library_ha_accessions.csv).
The vaccine strains are placed in [download/vaccine_ha_accessions.csv](download/vaccine_ha_accessions.csv).

## GISAID download
I searched for sequences by GISAID ID in the EpiFlu database.
I needed to break this into a few searches/downloads due to sequence number download limits.
Following the direction in the the `seasonal-flu` main directory repo, I downloaded both HA nucleotide sequences and associated metadata. 
Each of these files is placed in [download](download), and are not tracked in this repository due to GISAID data sharing restrictions. 

## Concatenating FASTA files and metadata XLS
Currently, only a single FASTA sequence file and metadata XLS file are allowed as input. 
All XLS- and FASTA-format files in [download](download) are concatenated with [scripts/concatenate_xls.py](scripts/concatenate_xls.py) and [scripts/concatenate_fasta.py](scripts/concatenate_fasta.py), respectively, which are run with:

    python scripts/concatenate_fasta.py
    python scripts/concatenate_xls.py

## Make strain to ID map
To make a dataframe of strain name and each corresponding GISAID ID, run the following script:

    python scripts/make_strain_to_id_map.py

The output is placed in [concatenated_files/strain_to_id_map.csv](concatenated_files/strain_to_id_map.csv).