# 02.02 - data clean

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
