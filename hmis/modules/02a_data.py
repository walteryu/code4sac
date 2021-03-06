# 02A - Load data into notebook

# load data into notebook; make sure file is in folder as notebook
df_assessments = pd.read_csv('data/assessments.csv')
df_clients = pd.read_csv('data/clients.csv')
df_enrollments = pd.read_csv('data/enrollments.csv')
df_exits = pd.read_csv('data/exits.csv')
df_projects = pd.read_csv('data/projects.csv')
df_services = pd.read_csv('data/services.csv')

# example of converting column data type
# df['cost'] = pd.to_numeric(df['cost'])

# drop null values
# df = df.dropna()

# replace white spaces
# https://stackoverflow.com/questions/13757090/pandas-column-access-w-column-names-containing-spaces
# print("*** column names - assessments ***")
# df_assessments.columns = [c.replace(' ', '_') for c in df_assessments.columns]
# print(list(df_assessments.columns))
# print("")
# print("*** column names - clients ***")
# df_clients.columns = [c.replace(' ', '_') for c in df_clients.columns]
# print(list(df_clients.columns))
# print("")
# print("*** column names - enrollments ***")
# df_enrollments.columns = [c.replace(' ', '_') for c in df_enrollments.columns]
# print(list(df_enrollments.columns))
# print("")
# print("*** column names - exits ***")
# df_exits.columns = [c.replace(' ', '_') for c in df_exits.columns]
# print(list(df_exits.columns))
# print("")
# print("*** column names - projects ***")
# df_projects.columns = [c.replace(' ', '_') for c in df_projects.columns]
# print(list(df_projects.columns))
# print("")
# print("*** column names - services ***")
# df_services.columns = [c.replace(' ', '_') for c in df_services.columns]
# print(list(df_services.columns))
# print("")

# print out first 5 lines of dataset below
# print(df_assessments.head(5))
# print(df_clients.head(5))
# print(df_enrollments.head(5))
# print(df_exits.head(5))
# print(df_projects.head(5))
# print(df_services.head(5))

# inspect for data types and missing values (note: Pandas stores character strings as type 'object')
print("*** column names - assessments ***")
print(df_assessments.info())
print("")
print("*** column names - clients ***")
print(df_clients.info())
print("")
print("*** column names - enrollments ***")
print(df_enrollments.info())
print("")
print("*** column names - exits ***")
print(df_exits.info())
print("")
print("*** column names - projects ***")
print(df_projects.info())
print("")
print("*** column names - services ***")
print(df_services.info())
print("")

# 02B - Show dataframe shape

# Remove outlier values, i.e. outside 3 standard deviations
# VMT_is_within_3_standard_deviations = np.abs(df['Annual_VMT'] - df['Annual_VMT'].mean()) <= (3*df['Annual_VMT'].std())
# df = df[VMT_is_within_3_standard_deviations]
# print('Column Dimensions - Excluding Outliers:')
# print(df.shape)
# print("")

# merge clients, entries and exits
clients_enrollments = pd.merge(df_clients, df_enrollments, on='personal_id')
enrollments_exits = pd.merge(clients_enrollments, df_exits, on='personal_id')

print('Unique Values - Client Ethnicty:')
print(clients_enrollments['client_ethnicity'].unique())
print('')

print('Value Counts - Client Ethnicty:')
print(clients_enrollments['client_ethnicity'].value_counts())
print('')

print('Unique Values - Exit Reason:')
print(enrollments_exits['exit_reason'].unique())
print('')

print('Value Counts - Exit Reason:')
print(enrollments_exits['exit_reason'].value_counts())
print('')

print('Client/Enrollment - Data Shape:')
print(clients_enrollments.shape)
print('')

print('Enrollment/Exit - Data Shape:')
print(enrollments_exits.shape)
print('')

# 02C - Summary statistics

# Output summary statistics for dataframe
print('Summary Statistics - Annual VMT Column:')
df['Annual_VMT'].describe()

# Note you can also get summary statistics for the entire dataframe, e.g.
# df.describe(include='all') # note the `include='all'` argument will include non-numeric columns (e.g. # unique)

# 02C - Summary statistics

# Note you can also get summary statistics for the entire dataframe, e.g.:
# df.describe(include='all')
# note the `include='all'` argument will include non-numeric columns (e.g. # unique)

# Output summary statistics for dataframe
# print('Summary Statistics - Annual VMT Column:')
# df['Annual_VMT'].describe()
