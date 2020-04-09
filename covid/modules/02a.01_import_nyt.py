# 02A.01 - Load data into notebook
# Source data: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv

# load data into notebook; make sure file is in folder as notebook
df_total = pd.read_csv('data/nyt_county_cases.csv')

print("*** dataset info - total cases by US county ***")
print(df_total.info())
print("")

print('*** data shape - total cases by US county ***')
print(df_total.shape)
print('')

print('*** unique values - US state ***')
print(df_total['state'].unique())
print('')

# df.describe(include='all')
# note the `include='all'` argument will include non-numeric columns (e.g. # unique)

# Output summary statistics for dataframe
print('*** summary statistics - total cases by US county ***')
df_total['cases'].describe()
