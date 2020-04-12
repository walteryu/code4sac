# 02B.02 - eda/kff data 
# Source data: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv

# convert string to datetime
# reference: https://stackoverflow.com/questions/32888124/pandas-out-of-bounds-nanosecond-timestamp-after-offset-rollforward-plus-adding-a

# index for plot based by date
# indexedDataset = dataset.set_index(['SampleDate'])

# example of converting column data type
# df['cost'] = pd.to_numeric(df['cost'])

# drop null values
# df = df.dropna()

# Remove outlier values, i.e. outside 3 standard deviations
# VMT_is_within_3_standard_deviations = np.abs(df['Annual_VMT'] - df['Annual_VMT'].mean()) <= (3*df['Annual_VMT'].std())
# df = df[VMT_is_within_3_standard_deviations]
# print('Column Dimensions - Excluding Outliers:')
# print(df.shape)
# print("")

# merge clients, entries and exits
# clients_enrollments = pd.merge(df_clients, df_enrollments, on='personal_id')
# enrollments_exits = pd.merge(clients_enrollments, df_exits, on='personal_id')

print("*** dataset info - total results by state ***")
print("")
print(df_total_kff.info())
print("")
