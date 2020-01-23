# 02B - Show dataframe shape

# replace white spaces
# https://stackoverflow.com/questions/13757090/pandas-column-access-w-column-names-containing-spaces
df_assessments.columns = [c.replace(' ', '_') for c in df_assessments.columns]
df_clients.columns = [c.replace(' ', '_') for c in df_clients.columns]
df_enrollments.columns = [c.replace(' ', '_') for c in df_enrollments.columns]
df_exits.columns = [c.replace(' ', '_') for c in df_exits.columns]
df_projects.columns = [c.replace(' ', '_') for c in df_projects.columns]
df_services.columns = [c.replace(' ', '_') for c in df_services.columns]

# print(df_assessments.head(5))
# print(df_clients.head(5))
# print(df_enrollments.head(5))
# print(df_exits.head(5))
# print(df_projects.head(5))
# print(df_services.head(5))

print(list(df_assessments.columns))
print(list(df_clients.columns))
print(list(df_enrollments.columns))
print(list(df_exits.columns))
print(list(df_projects.columns))
print(list(df_services.columns))

# merge clients, entries and exits
clients_enrollments = pd.merge(df_clients, df_enrollments, on='Personal_ID')
enrollments_exits = pd.merge(clients_enrollments, df_exits, on='Personal_ID')

print('Unique Values - Clients:')
print(enrollments_exits['Personal_ID'].unique())
print('')
#
# print('Value Counts - Route:')
# print(df['Route'].value_counts())
# print('')
#
# print('Unique Values - County:')
# print(df['County'].unique())
# print('')
#
# print('Value Counts - County:')
# print(df['County'].value_counts())
# print('')
#
# print('Column Dimensions - Including Outliers:')
# print(df.shape)
# print('')

# Remove outlier values, i.e. outside 3 standard deviations
# VMT_is_within_3_standard_deviations = np.abs(df['Annual_VMT'] - df['Annual_VMT'].mean()) <= (3*df['Annual_VMT'].std())
# df = df[VMT_is_within_3_standard_deviations]
#
# print('Column Dimensions - Excluding Outliers:')
# print(df.shape)
