# Build the 2-year Nextstrain tree from November 2023 with `seqneut` 2023-2024 library strains
Description: Using the pipeline and tutorial set up by the Bedford lab for [seasonal-flu](https://github.com/nextstrain/seasonal-flu/), build a phylogenetic tree of the sequences from the 2-year H3N2 tree available at time of library creation (November 2023) and all library strains (which were not all present in the original build). 
Author: Caroline Kikawa

## Create `conda` virtual environment
To process input data and (minimally) run the `nextstrain build` command, create and activate the `conda` virtual environment with:

    conda env create -f environment.yml
    conda activate nextstrain

## Make input data
Input data are specified in [data/](data/) and were downloaded per the instructions in the [seasonal-flu](https://github.com/nextstrain/seasonal-flu/).
The actual process of batch downloading and processing the sequences is documented in the subdirectory [data/README.md](data/README.md), along with the scripts necessary to get GISAID IDs from a tree, etc.

## Edit the build configuration
This build was created following the instructions in the main directory [README.md](README.md) with the exception of an `--include` flag that was added for a few strains that failed the molecular clock filter.
These strains have significant mismatch between their inferred date and recorded collection date.

## Run the pipeline
If running on the Hutch cluster, first grab 8 cores. Then, I ran the build (coercing all strains to be included with `--forceall` flag) with:

    nextstrain build . --configfile profiles/gisaid/builds.yaml --forceall

I copied the output tree locally to [results/h3h2_ha.json](results/h3h2_ha.json). 

## Upload the tree build to the `jbloomlab` Nextstrain Groups page
I followed the instructions for logging in with the Nextstrain CLI outlined [here](https://docs.nextstrain.org/en/latest/guides/share/groups/index.html). Then, in the  top-level directory of the `seasonal-flu` build, I uploaded my tree using:

    nextstrain remote upload \
      nextstrain.org/groups/jbloomlab/seqneut/h3n2-ha-2023-2024 \
        auspice/h3n2_ha.json \
        auspice/h3n2_ha_tip-frequencies.json 

