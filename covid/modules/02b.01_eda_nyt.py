# 02B.01 - eda/nytimes
# Source data: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv

# convert string to datetime
# reference: https://stackoverflow.com/questions/32888124/pandas-out-of-bounds-nanosecond-timestamp-after-offset-rollforward-plus-adding-a

# index for plot based by date
# indexedDataset = dataset.set_index(['SampleDate'])

# convert col to numeric type
# reference: https://stackoverflow.com/questions/47333227/pandas-valueerror-cannot-convert-float-nan-to-integer
def convert_num(col):
    # convert type
    col = pd.to_numeric(
        col,
        errors='coerce'
    )
    # print msg in case of error
    # if col.dtypes != 'int64' or 'float64':
    #     print('error: numeric conversion not successful')

convert_num(df_1618['DISTRICTID'])

df_total['date'] = pd.to_datetime(
    df_total['date'],
    infer_datetime_format=True,
    errors = 'coerce'
)

print("*** confirm data types conversion - datetime ***")
print("")
print(df_total.info())
print("")

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

# filter by state
# https://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining
df_california = df_total[df_total['state'] == 'California']

print("*** dataset info - total cases in CA by county ***")
print("")
print(df_california.info())
print("")
