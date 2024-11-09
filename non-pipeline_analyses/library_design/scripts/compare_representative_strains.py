##################################################################################################################################
''' 
compare_representative_strains.py


'''


# Import packages
import pandas as pd
import os

##################################################################################################################################
# [Phylogenetic method]
# My inputs are 2 TSV outputs  because I ran on the 2y (two year) and 6m (six month) trees for H3N2
# Program was run in October 2023, trees last updated in late Sept 2023
files = {'two_year': 'representative_strains_per_haplotype_2y.tsv', 
		 'six_month': 'representative_strains_per_haplotype_6m.tsv'}


# Code for identifying clade overlap 
strains_df = pd.DataFrame()
for key in files: 
	# Import emerging clades output
	df = pd.read_csv(os.path.join('auspice_haplotypes', files[key]), sep='\t')
	df['timeframe'] = key
	# Select minimum branch length strains
	strains_df = pd.concat([strains_df, df[['name', 'div', 'num_date',
	'clade_membership', 'subclade', 'haplotype', 'timeframe']]])

print('Here is some basic info on the Auspice/Phylogenetic method-selected strains...')


# All haploytpes
haplotypes = strains_df['haplotype'].tolist()
print(f'the number output haplotypes is... {len(haplotypes)}')

# Unique haplotypes
unique_haplotypes = [i for i in haplotypes if haplotypes.count(i)==1]
print(f'the number of unique haplotypes occurring is... {len(unique_haplotypes)}')

# Haplotypes that appear both in 2y and 6m trees
overlapping_haplotypes = list(set(haplotypes).difference(unique_haplotypes))
print(f'the number of overlapping haplotypes is... {len(overlapping_haplotypes)}')

# Subselect original dataframe on overlapping haplotypes
overlapping_haplotypes_df = (strains_df[strains_df['haplotype']
	.isin(overlapping_haplotypes)]
	.query('timeframe == "six_month"'))

# Subselect original dataframe on unique haplotypes
unique_haplotypes_df = (strains_df[strains_df['haplotype']
	.isin(unique_haplotypes)])


# Add overlapping and unique dataframes back together
auspice_strains_df = pd.concat([overlapping_haplotypes_df, unique_haplotypes_df]).reset_index(drop=True)

print('...')

print('Now we can compare the number of strains from 6-month and 2-year, pre and post filtering.')
print('We should have kept all 6 month strains, and only a subselection of 2-year, if there was overlap.')
print('initial 6 month strains remaining are... ', len(strains_df.query('timeframe == "six_month"')))
print('initial 2 year strains remaining are... ', len(strains_df.query('timeframe == "two_year"')))

print('the 6 month strains remaining are... ', len(auspice_strains_df.query('timeframe == "six_month"')))
print('the 2 year strains remaining are... ', len(auspice_strains_df.query('timeframe == "two_year"')))




# Strain names can be searched in GISAID
# However, because names of strains can sometimes be mismatched bewteen
# NextStrain and GISAID, it's better to search accession numbers.

# Pull accession numbers from metadata
metadata_file = 'nextclade_metadata_h3n2_2023-11-21.tsv'
metadata = pd.read_csv(metadata_file, sep='\t')
metadata['name'] = metadata['seqName']
auspice_strains_df = auspice_strains_df.merge(metadata[['name', 'short-clade', 'HA1_substitutions', 'accession_ha']], how='left', on=['name'])
# There's a typo in one of my sequence EPIs...
auspice_strains_df = (auspice_strains_df
	.replace({'EPI2004948': 'EPI2004947'})
	.sort_values(by=['clade_membership'])
	.reset_index(drop=True)
	)


# Add clade_mutation label to joined metadata file
auspice_strains_df['clade_HA1muts'] = (auspice_strains_df['short-clade'] + ':' + 
	auspice_strains_df['HA1_substitutions'].str.replace('HA1:',''))
# Label contents as originating from Phylogenetic method
auspice_strains_df['origin'] = 'auspice'



twoYear_haplo_withMetadata_df = (unique_haplotypes_df
	.query('timeframe == "two_year"')
	.merge(metadata[['name', 'short-clade', 'HA1_substitutions', 'accession_ha',]], how='left', on=['name'])
	)

twoYear_haplo_withMetadata_df['clade_HA1muts'] = (twoYear_haplo_withMetadata_df['short-clade'] + ':' + 
	twoYear_haplo_withMetadata_df['HA1_substitutions'].str.replace('HA1:',''))
# print(twoYear_haplo_withMetadata_df)



# Write out accession numbers only 
outfile = 'GISAID_query/auspice_accession_numbers.csv'
auspice_strain_accession = auspice_strains_df['accession_ha']
print(f'the number of [Phylogenetic method] unique accessions is... {len(auspice_strain_accession.drop_duplicates())}')
with open(outfile, 'w') as f:
	for item in auspice_strain_accession:	
		f.write(item + '\n')





##################################################################################################################################
# [NextClade method]
# My input is a single TSV, generated with help from John Huddleston (Bedford lab).
# All outputs were generated from a metadata file generated on October 6th by John.
# See README for more details

files = {'since2023': 'representative_strains_per_HA1_haplotype_nextclade.tsv'}

nextclade_strains_df = pd.DataFrame()
for key in files: 
	# Import emerging clades output
	df = pd.read_csv(os.path.join('nextclade_haplotypes', files[key]), sep='\t')
	df['rankClass'] = key
	# Select minimum branch length strains
	nextclade_strains_df = pd.concat([nextclade_strains_df, df[['seqName', 'short-clade', 'subclade',
	'aaSubstitutions', 'HA1_substitutions', 'accession_ha', 'date', 'date_submitted', 'region', 'country', 'division', 'location', 
	'passage_category', 'originating_lab', 'submitting_lab', 'HA1_haplotype_count']]])


print(nextclade_strains_df.head())


# Write out accession numbers only 
outfile = 'GISAID_query/nextclade_accession_numbers.csv'
nextclade_strain_accession = nextclade_strains_df['accession_ha']
print(f'the number of [Nextclade method] unique accessions is... {len(nextclade_strain_accession.drop_duplicates())}')
with open(outfile, 'w') as f:
	for item in nextclade_strain_accession:	
		f.write(item + '\n')


nextclade_strains_df['name'] = nextclade_strains_df['seqName']
nextclade_strains_df['origin'] = 'nextclade'
nextclade_strains_df['clade_HA1muts'] = nextclade_strains_df['short-clade'] + ':' + nextclade_strains_df['HA1_substitutions'].str.replace('HA1:','')



print('...')
print('Now we can add the Auspice and Nextclade dataframes together and examine overlap between haplotypes.')
print('To keep nomenclature consistent, we will create "clade_HA1mutation" labels.')



total_df = pd.concat([auspice_strains_df, nextclade_strains_df])[['name', 'clade_HA1muts', 'origin']]
# print(total_df)



# All haploytpes
clade_muts = total_df['clade_HA1muts'].tolist()
print(f'the number output clade_muts is... {len(clade_muts)}')
print('the number of unique clade_muts is... ', len(total_df.clade_HA1muts.unique()))

# Unique clade_muts
unique_clade_muts = [i for i in clade_muts if clade_muts.count(i)==1]
print(f'the number of clade_muts occurring once is... {len(unique_clade_muts)}')

# Haplotypes that appear both in 2y and 6m trees
overlapping_clade_muts = list(set(clade_muts).difference(unique_clade_muts))
print(f'the number of overlapping clade_muts is... {len(overlapping_clade_muts)}')

# Subselect original dataframe on overlapping clade_muts
overlapping_clade_muts_df = (total_df[total_df['clade_HA1muts']
	.isin(overlapping_clade_muts)]
	.query('origin == "auspice"'))

# Subselect original dataframe on unique clade_muts
unique_clade_muts_df = (total_df[total_df['clade_HA1muts']
	.isin(unique_clade_muts)])

# Add overlapping and unique dataframes back together
filtered_total_df = pd.concat([overlapping_clade_muts_df, unique_clade_muts_df]).reset_index(drop=True)










# Auspice 6m and 2y merged with nextclade
auspice_haplo_withCounts_df = (auspice_strains_df
	.merge(nextclade_strains_df[['name', 'clade_HA1muts', 'HA1_haplotype_count']], how='left', suffixes = ('_auspice2y', '_nextclade'), on=['clade_HA1muts'])
	# .dropna()
	.reset_index(drop=True)
	[['name_auspice2y', 'accession_ha', 'name_nextclade', 'short-clade', 'subclade', 'HA1_substitutions', 'timeframe', 'HA1_haplotype_count']]
	)

# Some haplotypes will have been sampled 0 times in Next clade
# Replace 'na' values with 0
auspice_haplo_withCounts_df['HA1_haplotype_count'] = auspice_haplo_withCounts_df['HA1_haplotype_count'].fillna(0)

# Write output
auspice_haplo_withCounts_df.to_csv('plotting/data/Auspice_haploStrains_withCounts.csv')






# Two year merged with nextclade
twoYear_haplo_withCounts_df = (twoYear_haplo_withMetadata_df
	.merge(nextclade_strains_df[['name', 'clade_HA1muts', 'HA1_haplotype_count']], how='left', suffixes = ('_auspice2y', '_nextclade'), on=['clade_HA1muts'])
	.dropna()
	)

# print(twoYear_haplo_withCounts_df)
twoYear_haplo_withCounts_df[['name_auspice2y', 'accession_ha', 'HA1_haplotype_count']].to_csv('plotting/data/twoYear_haplo_strains_withCounts.csv')







# # Check that Auspice 6m and 2y strains contain the top X haplotypes reported by Auspice
# nextclade_top50_haplotypes = pd.read_csv(os.path.join('nextclade_haplotypes', 'top_HA1_haplotypes.tsv'), sep = '\t')

# # Look at HA1 subs in Nextclade and check each string
# top50_haplo_missedByAuspice = pd.DataFrame()

# for index, row in nextclade_top50_haplotypes.iterrows():
# 	haplo = row[0]
# 	break

# 	if haplo not in auspice_haplo_withCounts_df['HA1_substitutions'].tolist():
# 		top50_haplo_missedByAuspice = pd.concat([top50_haplo_missedByAuspice, nextclade_top50_haplotypes.iloc[[index]]])


# print('...')


# if top50_haplo_missedByAuspice.empty: 
# 	print('Auspice method has captured top 50 haplotypes by Nextclade method...')
# else:
# 	top50_haplo_missedByAuspice = (
# 		top50_haplo_missedByAuspice
# 		.merge(nextclade_strains_df[['name', 'short-clade', 'subclade', 'HA1_substitutions', 'accession_ha',]], how='left', on=['HA1_substitutions'])
# 		.dropna()
# 		.reset_index(drop=True)
# 		[['name', 'accession_ha', 'short-clade', 'subclade', 'HA1_substitutions', 'HA1_haplotype_count']]
# 		)

# 	(top50_haplo_missedByAuspice).to_csv('plotting/data/top50_haplo_missedByAuspice.csv')





########################################################################################################################################

# Mutation frequency
# How many different mutations do we have?
# How many unique?
# How many mutations occur on multiple lineages? 



# Join both Auspice/NextClade and NextClade missed 24 strains into mega dataset
auspice_haplo_withCounts_df['name'] = auspice_haplo_withCounts_df['name_auspice2y']
auspice_haplo_tidy = auspice_haplo_withCounts_df[['name', 'timeframe', 'accession_ha', 'short-clade', 'subclade', 'HA1_substitutions','HA1_haplotype_count']]
auspice_haplo_tidy = auspice_haplo_tidy.assign(method = 'auspice')
# top50_haplo_missedByAuspice = top50_haplo_missedByAuspice.assign(method = 'nextclade-top50')


########################################################################################################################################

### Get all haplotypes
megaset = pd.concat([auspice_haplo_tidy, 
	# top50_haplo_missedByAuspice
	]).reset_index(drop=True)
haplotypes = (megaset['HA1_substitutions'].str.replace('HA1:', '').tolist())
# print(haplotypes)

# Get all mutations, including repeats
mutations = []
for haplo in haplotypes:

	for mut in haplo.split(','):

		mutations.append(mut)
# Save all mutations
pd.DataFrame(mutations, columns = ['mutations']).to_csv('plotting/data/all_mutations.csv')

# Get unique mutations
unique_mutations = list(set(mutations))


### Get all haplotypes (n=60, Auspice only)
auspice_haplotypes = (auspice_haplo_tidy['HA1_substitutions'].str.replace('HA1:', '').tolist())

# Get all mutations, including repeats
auspice_mutations = []
for haplo in auspice_haplotypes:

	for mut in haplo.split(','):

		auspice_mutations.append(mut)
pd.DataFrame(auspice_mutations, columns = ['mutations']).to_csv('plotting/data/auspice_mutations.csv')

# Get unique mutations
unique_auspice_mutations = list(set(auspice_mutations))


########################################################################################################################################


# Write histogram of mutation occurance
counts_of_mutations = {}
for i in mutations:
	counts_of_mutations[i] = counts_of_mutations.get(i,0) + 1
sorted_counts_of_mutations = dict(sorted(counts_of_mutations.items(), key=lambda item: item[1], reverse=True))
# print(sorted_counts_of_mutations)


# Sites with multiple mutations 
# First make dataframe of all unique wt,site,mut combinations 
df = (pd.DataFrame(unique_mutations, columns = ['mutation'])
	.assign(
		wt = lambda x: x['mutation'].str[0],
		site = lambda x: (x['mutation'].str[1:-1]).astype(int),
		mut = lambda x: x['mutation'].str[-1])
	.sort_values(by = 'site')
	.reset_index(drop=True)
	)
# Then write sites seen more than once to their own dataframes
multiple_mut_sites_df = (pd.concat(g for _, g in df.groupby('site') if len(g) > 1).reset_index(drop=True))
# print(multiple_mut_sites_df)


# # Write out combined dataframe to csv
# auspice_strains_df.to_csv('h3_haplotypes_combined_timeframes.csv')

# # Write out strain names only 
# outfile = 'strain_names.csv'
# strain_names = list(set(auspice_strains_df['min_branch_strain']))
# with open(outfile, 'w') as f:
# 	for item in strain_names:	
# 		f.write(item + '\n')



# # Write out pre-2021 strain names  
# outfile = 'pre2021_strain_names.csv'
# strain_names = auspice_strains_df['min_branch_strain']
# with open(outfile, 'w') as f:
# 	f.write('strain_name\n')
# 	for item in strain_names:
# 		if int(item.split('/')[-1]) < 2022:	
# 			f.write(item + '\n')


# # Write out accession numbers only 
# outfile = 'accession_numbers.csv'
# strain_accession = auspice_strains_df['accession_ha']
# print(f'the number of unique accessions is... {len(strain_accession.drop_duplicates())}')
# with open(outfile, 'w') as f:
# 	for item in strain_accession:	
# 		f.write(item + '\n')






