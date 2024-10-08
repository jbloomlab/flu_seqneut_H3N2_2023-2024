"""Top-level ``snakemake`` file that runs analysis."""

import pandas as pd
from os.path import join

configfile: "config.yml"

include: "seqneut-pipeline/seqneut-pipeline.smk"


rule all:
    input:
        seqneut_pipeline_outputs  # outputs from pipeline
        # "results/plots_for_paper/plot_specific_sera/curves.pdf" # outputs from plotting notebook


rule plot_specific_sera:
    """Plot curves for a few specific sera."""
    input:
        curvefits_pickle="results/aggregated_titers/curvefits_PennVaccineCohort.pickle",
    output:
        plot_pdf="results/plots_for_paper/plot_specific_sera/curves.pdf",
    log:
        notebook="results/plots_for_paper/plot_specific_sera/plot_specific_sera.ipynb",
    conda:
        "seqneut-pipeline/environment.yml"
    notebook:
        "notebooks/plot_specific_sera.py.ipynb"
