# 03A.02 - create count plot

# create histogram
# `kde=False` turns off the default density estimate plot
# sns.distplot(clients_enrollments['client_ethnicity'], kde=False)

# set plot size and title
plt.figure(figsize=(12, 8))
plt.title('Count Plot: Total COVID-19 Tests with Results by US State')

# create countplot
sns.countplot(y="tests_with_results", data=df_total_kff)

# set plot size and title
plt.figure(figsize=(12, 8))
plt.title('Count Plot: Total Case Count in CA by County (As of 04-03-2020)')

# create countplot
sns.countplot(y="percentage_test_positive", data=df_total_kff)

# set plot size and title
plt.figure(figsize=(12, 8))
plt.title('Count Plot: Total COVID-19 Tests per 1k Residents by US State')

# create countplot
sns.countplot(y="total_tests_per_1k_residents", data=df_total_kff)

# set plot size and title
plt.figure(figsize=(12, 8))
plt.title('Category Plot: Total COVID-19 Tests per 1k Residents by US State')
sns.catplot(
    x='tests_with_results',
    y='percentage_test_positive',
    data=df_total_kff,
    kind='bar'
)
