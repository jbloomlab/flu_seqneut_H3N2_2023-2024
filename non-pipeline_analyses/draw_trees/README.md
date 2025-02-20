# Drawing trees for paper figures 
Author: Caroline Kikawa

## Input
The JSON for the library tree was generated using from a custom Nextstrain `seasonal-flu` build, see [../non-pipeline_analyses/nextstrain_tree_build](../non-pipeline_analyses/nextstrain_tree_build) for more details. The recent 2-year Nextstrain tree depicted in Supplemental Figure 6 was downloaded using the following command:

    curl https://nextstrain.org/seasonal-flu/h3n2/ha/2y --header 'Accept: application/vnd.nextstrain.dataset.main+json' --compressed > flu_seasonal_h3n2_ha_2y_dowloaded250218.json

The JSONs are placed in [data](data), along with other metadata necessary for drawing custom trees, including:
* [data/vaccine_strains.csv](data/vaccine_strains.csv): a CSV-format list of all vaccine strains included in the H3N2 library
* [data/egg-passaged_vaccine_strains.csv](data/egg-passaged_vaccine_strains.csv): a CSV-format list of *egg-passaged* vaccine strains included in the H3N2 library
* [data/growth_vs_titers_gisaid-ha1-within1_2023-mincounts80_child-and-adultprevax-sera_scatter.csv](data/growth_vs_titers_gisaid-ha1-within1_2023-mincounts80_child-and-adultprevax-sera_scatter.csv): a CSV-format table of the growth rates associated with each strain for the MLR model fit to GISAID sequences that were within 1 HA1 mutation of any strain in the library, and that had a minimum 80 sequencing counts in 2023
* [data/nextclade.csv](data/nextclade.csv): a CSV-format table of strain metadata used to annotate tree nodes

## Performing the analysis
There are two Jupyter notebooks that are run interactively. 
* [draw_recent_Nextstrain_2y_tree.ipynb](draw_recent_Nextstrain_2y_tree.ipynb): draws the recent 2-year Nextstrain tree, annotating subclades and highlighting strains containing 145 mutations. This tree is shown in Supplementary Figure 6.
* [draw_recent_Nextstrain_2y_tree.ipynb](draw_recent_Nextstrain_2y_tree.ipynb): draws the tree generated from the custom Nextstrain `seasonal-flu` build, inclduing those depicted in main text Figure 2 and Figure 5. 

## Output
The saved tree images from running the notebooks interactively are placed in [results](results). Additionally, a list of ordered strain names used to match the order of strains on the tree to the order of strains on the X-axis of the neutralization titer plots generated in other custom analyses (e.g., [../non-pipeline_analyses/plot_NT50_profiles](../non-pipeline_analyses/plot_NT50_profiles) and the main `seqneut-pipeline` output) is placed in [results/ordered_strains.csv](results/ordered_strains.csv)
