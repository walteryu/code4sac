# 02C - Summary statistics

# Output summary statistics for dataframe
print('Summary Statistics - Annual VMT Column:')
df['Annual_VMT'].describe()

# Note you can also get summary statistics for the entire dataframe, e.g.
# df.describe(include='all') # note the `include='all'` argument will include non-numeric columns (e.g. # unique)