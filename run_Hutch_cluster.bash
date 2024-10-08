#!/bin/bash
#
#SBATCH -c 32

snakemake \
    --use-conda \
    -j 32 \
    --rerun-incomplete \
    --software-deployment-method conda \
    --keep-going
