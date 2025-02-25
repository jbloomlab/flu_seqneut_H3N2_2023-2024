# Library pooling
This directory describes the process of initial pooling, assessing viral barcode balancing, and assessing the fraction of viral barcode reads on increasing plated MDCK-SIAT1 cells. 
Author: Caroline Kikawa

## Input
All data for the notebooks in [notebooks](notebooks) are pulled directly from `seqneut-pipeline` output.

## Running the analysis
All the analyses are performed interactively with some output saved to [figures](figures) for the paper. The notebooks are summarized below:
* [notebooks/240108_library_pooling_equal_volumes.ipynb](notebooks/240108_library_pooling_equal_volumes.ipynb): The initial library pooled all strains at equal volumes. Balancing was assessed for subsequent re-pooled libraries. 
* [notebooks/240115_library_pooling_adjusted_repool.ipynb](notebooks/240115_library_pooling_adjusted_repool.ipynb): The library was re-pooled based on intial equal volume pooling was assessed. 
* [notebooks/240131_library_pooling_adjusted_comparison_to_H1_library.ipynb](notebooks/240131_library_pooling_adjusted_comparison_to_H1_library.ipynb): The re-pooled H3 library (same as above) was compared to the H1 library described in Loes et al. 2024. 
* [notebooks/240328_MOItest_variableCell.ipynb](notebooks/240328_MOItest_variableCell.ipynb): The re-pooled H3 library (same as above) was tested on different plated densities of MDCK-SIAT1 cells. 
* [notebooks/241001_library_pooling_verify_repool.ipynb](notebooks/241001_library_pooling_verify_repool.ipynb): The H3 library needed to be remade because stocks were low. The library was re-pooled according to original calculations from the first initial experiment and verified. 