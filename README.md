# Sequencing-based neutralization assays to estimate serum neutralizing titers in adult and pediatric cohorts using a library of 61 seasonal H3N2 influenza viruses circulating in late 2023 and 17 recent and historical vaccine strains 
This repository contains data and analysis of sequencing-based neutralization assays using a library of 78 seasonal H3N2 influenza viruses, including 17 recent and historical vaccine strains (with both egg- and cell-passaging histories) and 61 strains representing circulating H3N2 diversity in November 2023. 
These experiments were performed by Caroline Kikawa, using method and analysis developed by the [Bloom lab](https://jbloomlab.github.io/) and described in [Loes et al (2024)](https://journals.asm.org/doi/10.1128/jvi.00689-24).

## Quick summary
* The actual strains in the library are listed in CSV format in [./data/H3N2library_2023-2024_allStrains.csv](./data/H3N2library_2023-2024_allStrains.csv), and the process of library design is described in [non-pipeline_analyses/library_design/README.md](non-pipeline_analyses/library_design/README.md).
    * The trimmed HA1 sequences are placed in [.non-pipeline_analyses/library_design/results/2023-2024_H3_library_protein_HA1.fasta](.non-pipeline_analyses/library_design/results/2023-2024_H3_library_protein_HA1.fasta)
    * The HA ectodomain sequences (with the H3 transmembrane domain removed) are placed in [.non-pipeline_analyses/library_design/results/2023-2024_H3_library_protein_HA_ectodomain.fasta](.non-pipeline_analyses/library_design/results/2023-2024_H3_library_protein_HA_ectodomain.fasta).
    * The chimeric HA protein construct sequences with upstream signal peptide fixed to WSN sequence, downstream transmembrane domain fixed to H3 consensus, and downstream C-terminal tail fixed to WSN sequence are listed in [.non-pipeline_analyses/library_design/results/2023-2024_H3_library_protein_constructs.fasta](.non-pipeline_analyses/library_design/results/2023-2024_H3_library_protein_constructs.fasta)

* This library was then assayed against sera from different human cohorts, specifically:
    * 78 unique human serum samples from the University of Pennsylvania, taken at 0 and 28 days post vaccination (from 39 matched individuals) with the egg-based 2022-2023 seasonal influenza virus vaccine. The H3N2 vaccine component that season was A/Darwin/9/2021.
    * 56 pediatric human serum samples from Seattle Children's Hospital obtained from routine blood draws.
    * 20 sera samples from a cohort from Australia taken pre- and post-vaccination from 10 individuals vaccinated with the cell-based 2024 Southern Hemisphere vaccine
    * Some pools of the sera from the different cohorts.

* The aggregated titers for each cohort are in in [results/aggregated_titers](results/aggregated_titers). Specifically:
    * titers for the Penn vaccine cohort: [./results/aggregated_titers/titers_PennVaccineCohort.csv](./results/aggregated_titers/titers_PennVaccineCohort.csv)
    * titers for the Seattle Children's Hospital cohort: in [./results/aggregated_titers/titers_SCH.csv](./results/aggregated_titers/titers_SCH.csv)
    * titers for the Australia vaccine cohort: [./results/aggregated_titers/titers_AusVaccineCohort.csv](./results/aggregated_titers/titers_AusVaccineCohort.csv)
    * titers for the pooled sera: [./results/aggregated_titers/titers_PooledSera.csv](./results/aggregated_titers/titers_PooledSera.csv)

## Description of input data
The input data are in [./data/](data), and include:
* [./data/miscellaneous_plates/](./data/miscellaneous_plates/): directory of CSV files detailing well IDs of plates requiring barcoding counting but *do not* need curves fit. This is useful for library titrations to estimate strain balancing and titers. See [`seqneut-pipeline` documentation on `miscellaneous_plates`](https://github.com/jbloomlab/seqneut-pipeline/tree/87580b7425494a4b8277749f9aa220ace3fe1541?tab=readme-ov-file#miscellaneous_plates) for more details. 
* [./data/neut_standard_sets/](./data/neut_standard_sets/): directory containing the CSV listing the barcodes linked to the spike-in non-neutralized control RNAs. See [Loes et al. 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10942427/) for more details. 
* [./data/plates/](./data/plates/): directory of CSV files that maps 96-well plate well IDs to each individual serum-containing or no-serum well. See [`seqneut-pipeline` documentation on `plates`](https://github.com/jbloomlab/seqneut-pipeline/tree/87580b7425494a4b8277749f9aa220ace3fe1541?tab=readme-ov-file#plates) for more details.
* [./data/viral_libraries/](./data/viral_libraries/): directory of CSV files that match 16-nucleotide barcodes to the library strain names.
* [./data/H3N2library_2023-2024_allStrains.csv](./data/H3N2library_2023-2024_allStrains.csv): CSV of strain names in the library that dictates the order viruses are plotted on the X-axis of aggreagted NT50 plots. 

## Library background and design
Information on the library design is placed in [.non-pipeline_analyses/library_design/](non-pipeline_analyses/library_design).

## Library pooling and quality checks
Analysis of library strain balancing and calculations for re-pooling library are placed in [.non-pipeline_analyses/library_pooling/](non-pipeline_analyses/library_pooling). These are currently manually run notebooks on barcode counts processed from `miscellaneous_plates`.

## Running the pipeline
This repository contains an analysis of the data using the Bloom lab software [`seqneut-pipeline`](https://github.com/jbloomlab/seqneut-pipeline) as a submodule. See that repository for intstructions on how to use Github submodules, including `seqneut-pipeline`. 

The configuration for the analysis is in [config.yml](config.yml) and the analysis itself is run by `snakemake` using [Snakefile](Snakefile).
Again, see [`seqneut-pipeline`](https://github.com/jbloomlab/seqneut-pipeline) for more description of how the pipeline works.

To run the pipeline, build the `seqneut-pipeline` conda environment from the [environment.yml](https://github.com/jbloomlab/seqneut-pipeline/blob/main/environment.yml) in `seqneut-pipeline`.
Then run the pipeline using:

    snakemake -j <n_jobs> --software-deployment-method conda

To run on the Hutch cluster, you can use the Bash script [run_Hutch_cluster.bash](run_Hutch_cluster.bash).

## Exploring the results
The results are placed in [./results/](results), and HTML rendering of results is in [./docs/](docs). For interactive plots, see the GitHub pages at [https://jbloomlab.github.io/flu_seqneut_H3N2_2023-2024/](https://jbloomlab.github.io/flu_seqneut_H3N2_2023-2024/)

Running the pipeline will generate many curves, which are stored as 'pickle' objects. To generate custom plots with specific curves, use the manually run notebook in [./notebooks/plot_specific_sera.py.ipynb](./notebooks/plot_specific_sera.py.ipynb). 
There are also detailed analysis notebooks generated by this pipeline. The final titers for each serum-virus pair are in [results/aggregated_titers/](results/aggregated_titers/)
The [./results/](results) also contains additional more detailed files with the per-viral-barcode counts for each sample, the fraction infectivities used to fit the neutralization curves, and details on the curve fits and titers for each individual replicate.

There are also custom plotting notebooks in [./non-pipeline_analyses/](non-pipeline_analyses), which are works-in-progress. 
