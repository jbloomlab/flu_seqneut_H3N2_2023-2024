# Plot NT50 profiles
This directory plots the neutralization titer (NT50) values output from `seqneut-pipeline` for paper figures. The notebooks to perform the analysis are run interactively, and described below. 
Author: Caroline Kikawa

## Build `conda` environment
First build and activate the conda environment in [environment.yml](environment.yml) with

    conda env create -f environment.yml
    conda activate plot_NT50_profiles

## Input data
The list of vaccine strains, and a list of which of those strains are specifically egg-passaged vaccine strains, are placed in [data/vaccine_strains.csv](data/vaccine_strains.csv) and [data/egg-passaged_vaccine_strains.csv](data/egg-passaged_vaccine_strains.csv), respectively. Otherwise, all input data for the notebooks in [notebooks](notebooks) are pulled directly from `seqneut-pipeline` output.

## Run plotting Jupyter Notebooks interactively
All the analyses are performed interactively with output saved to [results](results). The notebooks are summarized below:
* [notebooks/biological_replicate_correlation.ipynb](notebooks/biological_replicate_correlation.ipynb): Analyzing within- and between-plate replicates. Between plate replicates could only be analyzed for the subset of sera that were run on multiple days/plates.
* [notebooks/calculate_and_plot_variance.ipynb](notebooks/calculate_and_plot_variance.ipynb): Plot the geometric mean and coefficient of variation for each sera across all 2023-circulating viruses. 
* [notebooks/draw_cohort_overview_table.ipynb](notebooks/draw_cohort_overview_table.ipynb): Make a table describing the human cohorts that the tested sera were taken from. 
* [notebooks/plot_historical_vaccine_strains.ipynb](notebooks/plot_historical_vaccine_strains.ipynb): Plot neutralization titers to the past decade of egg- and cell-passaged vaccine strains. 
* [notebooks/plot_individuals.ipynb](notebooks/plot_individuals.ipynb): Make neutralization titer plots for individual sera and cohorts of sera, showing all titers to 2023-circulating strains. 
* [notebooks/plot_pools.ipynb](notebooks/plot_pools.ipynb): Compare the neutralizaiton titers measured from equal-volume serum pools to titers from individually-measured sera. 
* [notebooks/plot_post_vaccination.ipynb](notebooks/plot_post_vaccination.ipynb): Plot pre- and post-vaccination titers in adult vaccine cohorts based in the USA and Australia. 
