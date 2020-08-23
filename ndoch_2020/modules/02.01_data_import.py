# 02.01 - data import

# note: module based on tutorial below
# https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/

# load data via url
# https://stackoverflow.com/questions/32400867/pandas-read-csv-from-url/41880513#41880513
# url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
# df_total = pd.read_csv(url)

# function to read csv file
def read_data(path):
    df = pd.read_csv(path)
    return(df)

data_url = "https://data.sfgov.org/api/views/tmnf-yvry/rows.csv?accessType=DOWNLOAD"
df_data = read_data(data_url)

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
