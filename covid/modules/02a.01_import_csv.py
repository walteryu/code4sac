# 02A.01 - Load data into notebook

# load data via file
# Source data: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv
# df_total = pd.read_csv('data/nyt_county_cases.csv')

# nytimes dataset: load data via url
# https://stackoverflow.com/questions/32400867/pandas-read-csv-from-url/41880513#41880513
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
df_total = pd.read_csv(url)

# nytimes dataset: filter by state
# https://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining
df_california = df_total[df_total['state'] == 'California']

# kff dataset: load data via file
# Source data: https://www.kff.org/health-costs/issue-brief/state-data-and-policy-actions-to-address-coronavirus/#stateleveldata
df_total_kff = pd.read_csv('data/kff_state_testing_v1.csv')

# output table info
def data_profile(df, msg):
    print(msg, '\n')
    print('dataframe shape: ', df.shape, '\n')
    print(df.info(), '\n')
    print('dataframe data types:\n\n', df.dtypes, '\n')

# nytimes dataset
data_profile(
    df_total,
    '*** Table Info: NYT Dataset - Total Cases by US County ***'
)
# nytimes dataset
data_profile(
    df_california,
    '*** Table Info: NYT Dataset - Total Cases in CA ***'
)
# kff dataset
data_profile(
    df_total_kff,
    '*** Table Info: KFF Dataset - Total Results by US State ***'
)

# output unique values
def show_unique(col, msg):
    print('\n', msg, '\n')
    print(col.unique())

# nytimes dataset
show_unique(
    df_total['state'],
    '*** Unique Values: NYT Dataset - US States ***'
)
# kff dataset
show_unique(
    df_total_kff['location'],
    '*** Unique Values: KFF Dataset - US States ***'
)

# output summary stats
def summary_stats(col, msg):
    print('\n', msg, '\n')
    print(col.describe())

# nytimes dataset
summary_stats(
    df_total['cases'],
    '*** Summary Stats: NYT Dataset - Total Cases by US County ***'
)
# kff dataset
summary_stats(
    df_total_kff['tests_with_results'],
    '*** Summary Stats: KFF Dataset - Total Tests with Results by State ***'
)
# kff dataset
summary_stats(
    df_total_kff['total_tests_per_1k_residents'],
    '*** Summary Stats: KFF Dataset - Total Tests per 1k Residents by State ***'
)
