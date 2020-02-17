# 02C - summary statistics

# note you can also get summary statistics for the entire dataframe, e.g.:
# df.describe(include='all')
# note the `include='all'` argument will include non-numeric columns (e.g. # unique)

# output summary statistics for dataframe
# print('Summary Statistics - Annual VMT Column:')
# df['Annual_VMT'].describe()

print('clients-enrollments: data shape:')
print(clients_enrollments.shape)
print('')

print('enrollments-exits: data shape:')
print(enrollments_exits.shape)
print('')

print('enrollment-exit-services: data shape:')
print(ee_services.shape)
print('')
