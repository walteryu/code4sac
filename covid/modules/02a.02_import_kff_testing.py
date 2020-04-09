# 02A.02 - Load data into notebook
# Source data: https://www.kff.org/health-costs/issue-brief/state-data-and-policy-actions-to-address-coronavirus/#stateleveldata

# load data into notebook; make sure file is in folder as notebook
df_total_kff = pd.read_csv('data/kff_state_testing_v1.csv')

print('*** data info - total results by state ***')
print(df_total_kff.info())
print("")

print('*** data shape - total results by state ***')
print(df_total_kff.shape)
print('')

print('*** summary statistics - total tests with results by state ***')
print(df_total_kff['tests_with_results'].describe())
print('')

# df.describe(include='all')
# note the `include='all'` argument will include non-numeric columns (e.g. # unique)

# Output summary statistics
print('*** summary statistics - total tests per 1k residents by state ***')
df_total_kff['total_tests_per_1k_residents'].describe()
