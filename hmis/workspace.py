# 02B - Show dataframe shape

# Remove outlier values, i.e. outside 3 standard deviations
# VMT_is_within_3_standard_deviations = np.abs(df['Annual_VMT'] - df['Annual_VMT'].mean()) <= (3*df['Annual_VMT'].std())
# df = df[VMT_is_within_3_standard_deviations]
# print('Column Dimensions - Excluding Outliers:')
# print(df.shape)
# print("")

# usage: merge clients, entries and exits
# todo: projects do not appear to have clear ID to connect with other tables
clients_enrollments = pd.merge(df_clients, df_enrollments, on='personal_id')
enrollments_exits = pd.merge(clients_enrollments, df_exits, on='personal_id')
enrollments_services = pd.merge(df_enrollments, df_services, on='enrollment_id')

print('client-enrollments: unique values - client ethnicity:')
print(clients_enrollments['client_ethnicity'].unique())
print('')

print('client-enrollments: value counts - client ethnicity:')
print(clients_enrollments['client_ethnicity'].value_counts())
print('')

print('enrollments-exits: unique values - exit reason:')
print(enrollments_exits['exit_reason'].unique())
print('')

print('enrollments-exits: value counts - exit reason:')
print(enrollments_exits['exit_reason'].value_counts())
print('')

print('enrollments-services: unique values - category type:')
print(enrollments_services['service_category'].unique())
print('')

print('enrollments-services: value counts - category type:')
print(enrollments_services['service_category'].value_counts())
print('')

print('clients-enrollments: data shape:')
print(clients_enrollments.shape)
print('')

print('enrollments-exits: data shape:')
print(enrollments_exits.shape)
print('')

print('enrollment-exit-services: data shape:')
print(ee_services.shape)
print('')
