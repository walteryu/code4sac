# 02.00 - data functions

# function to read csv file
# https://stackoverflow.com/questions/32400867/pandas-read-csv-from-url/41880513#41880513
def read_data(path):
    df = pd.read_csv(path)
    return(df)

# function to output csv file
def output_result(df, filepath):
    df.to_csv(filepath)

# function to show table info
def data_profile(df, msg):
    # pass in variable into string
    # https://stackoverflow.com/questions/2960772/how-do-i-put-a-variable-inside-a-string
    print('*** Table Info: %s ***' % msg, '\n')
    print(df.info(), '\n')
    print('*** Table Info: Table Dimensions ***', '\n')
    print(df.shape, '\n')

# function to show unique value for given column
def show_unique(df, col):
    # pass in variable into string
    # https://stackoverflow.com/questions/2960772/how-do-i-put-a-variable-inside-a-string
    print('*** Unique Values: (%s) ***' % col, '\n')
    print(df[col].unique(), '\n')

# function to output summary stats
def summary_stats(df, col):
    # pass in variable into string
    # https://stackoverflow.com/questions/2960772/how-do-i-put-a-variable-inside-a-string
    print('*** Summary Stats: (%s) ***' % col, '\n')
    print(df[col].describe(), '\n')
    # print(col.describe())

# function to rename columns
# https://www.geeksforgeeks.org/how-to-rename-columns-in-pandas-dataframe/
def rename_col(df, old_col, new_col):
    df.rename(
        columns={old_col:new_col},
        inplace=True
    )
    return df

# function convert col to numeric type
# reference: https://stackoverflow.com/questions/47333227/pandas-valueerror-cannot-convert-float-nan-to-integer
def convert_num(df, col):
    # convert type
    df[col] = pd.to_numeric(
        df[col],
        errors='coerce'
    )
    return(df)

# convert string to datetime
# reference: https://stackoverflow.com/questions/32888124/pandas-out-of-bounds-nanosecond-timestamp-after-offset-rollforward-plus-adding-a
def convert_date(df, col):
    # convert type
    df[col] = pd.to_datetime(
        df[col],
        infer_datetime_format=True,
        errors = 'coerce'
    )
    return(df)

# function convert col to string type
def convert_str(df, col):
    # convert type
    df[col].astype(str)
    return(df)

# function to join tables and return results
def merge_table(df_left, df_right, col, method):
    # pd.merge(ca_covid_homeless_csv, ca_county_csv, on='county', how='right')
    df_join = pd.merge(df_left, df_right, on=col, how=method)
    return(df_join)
