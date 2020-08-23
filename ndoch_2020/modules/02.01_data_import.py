# 02.01 - data import

# note: module based on tutorial below
# https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/

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

data_profile(df_data, 'SFPD Reports')

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
