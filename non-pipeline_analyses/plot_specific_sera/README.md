# Plot full neutralization curves for some specific sera
Description: The code in this directory manually produces full neutralization curves for some specific sera versus a handful of viruses. The input are `pickle`-d [CurveFits objects](https://jbloomlab.github.io/neutcurve/neutcurve.curvefits.html) from `seqneut-pipeline`, which can be plotted using the Python package [`neutcurve`](https://jbloomlab.github.io/neutcurve/).
Author: Caroline Kikawa

## Build `conda` environment
First build and activate the conda environment in [environment.yml](environment.yml) with

    conda env create -f environment.yml
    conda activate titer_plotting

## Run plotting Jupyter Notebook interactively
The code in [plot_specific_sera.py.ipynb](plot_specific_sera.py.ipynb) produces plots of specific sera versus a few different viruses, pulling an input `pickle` file from a plate in the top-level [results/plates](../../results/plates/) directory. The output curves are placed in [results](results) and saved as SVGs.