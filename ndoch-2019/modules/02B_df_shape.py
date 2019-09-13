# 02B - Show dataframe shape

print('Unique Values - Route:')
print(df['Route'].unique())
print('')

print('Value Counts - Route:')
print(df['Route'].value_counts())
print('')

print('Unique Values - County:')
print(df['County'].unique())
print('')

print('Value Counts - County:')
print(df['County'].value_counts())
print('')

print('Column Dimensions - Including Outliers:')
print(df.shape)
print('')

# Remove outlier values, i.e. outside 3 standard deviations
    # here we use a series of logicals (True True False etc.) to retain a subset of the data
VMT_is_within_3_standard_deviations = np.abs(df['Annual_VMT'] - df['Annual_VMT'].mean()) <= (3*df['Annual_VMT'].std())
df = df[VMT_is_within_3_standard_deviations]

print('Column Dimensions - Excluding Outliers:')
print(df.shape)