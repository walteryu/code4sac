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
df_numeric = df_numeric[np.abs(df_numeric['Number of Incidents']- df_numeric['Number of Incidents'].mean()) <= (3*df_numeric['Number of Incidents'].std())]

print('Column Dimensions - Excluding Outliers:')
print(df_numeric.shape)
