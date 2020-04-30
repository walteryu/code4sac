# 02A.01 - Load data into notebook
# Source data: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv

# load data into notebook; make sure file is in folder as notebook
# df_total = pd.read_csv('data/nyt_county_cases.csv')

# load data via url
# https://stackoverflow.com/questions/32400867/pandas-read-csv-from-url/41880513#41880513
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
df_total = pd.read_csv(url)

# output table info
def data_profile(df, msg):
    print(msg, '\n')
    print('dataframe shape: ', df.shape, '\n')
    print(df.info(), '\n')
    print('dataframe data types:\n', df.dtypes)

data_profile(
    df_total,
    '*** Table Info: NYT Dataset - Total Cases by US County ***'
)

# output unique values
def show_unique(col, msg):
    print('\n', msg, '\n')
    print(col.unique())

show_unique(
    df_total['state'],
    '*** Unique Values: NYT Dataset - US States ***'
)

# output summary stats
def summary_stats(col, msg):
    print('\n', msg, '\n')
    print(col.describe())

summary_stats(
    df_total['cases'],
    '*** Summary Stats: NYT Dataset - Total Cases by US County ***'
)
