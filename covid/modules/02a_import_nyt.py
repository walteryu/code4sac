# 02A - Load data into notebook
# Source data: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv

# load data into notebook; make sure file is in folder as notebook
df_county = pd.read_csv('data/us-counties.csv')

print("*** column names - county cases ***")
print(df_county.info())
print("")

print('*** data shape - cases by US county ***')
print(df_county.shape)
print('')

print('*** unique values - US state ***')
print(df_county['state'].unique())
print('')

# df.describe(include='all')
# note the `include='all'` argument will include non-numeric columns (e.g. # unique)

# Output summary statistics for dataframe
print('*** summary statistics - daily cases by US county ***')
df_county['cases'].describe()
