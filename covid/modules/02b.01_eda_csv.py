# 02B.01 - exploratory data analysis (eda)
# Source data: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv

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

# convert string to datetime
# reference: https://stackoverflow.com/questions/32888124/pandas-out-of-bounds-nanosecond-timestamp-after-offset-rollforward-plus-adding-a
def convert_date(col):
    # convert type
    col = pd.to_datetime(
        col,
        infer_datetime_format=True,
        errors = 'coerce'
    )

# nytimes dataset
convert_num(df_total['date'])
