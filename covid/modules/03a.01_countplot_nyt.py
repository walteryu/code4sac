# 03A.01 - create count plot

# create histogram
# `kde=False` turns off the default density estimate plot
# sns.distplot(clients_enrollments['client_ethnicity'], kde=False)

# set plot size and title
plt.figure(figsize=(12, 8))
plt.title('Count Plot: Total Case Count by US State (As of 04-03-2020)')

# create countplot
sns.countplot(y="state", data=df_total)

# set plot size and title
plt.figure(figsize=(12, 8))
plt.title('Count Plot: Total Case Count in CA by County (As of 04-03-2020)')

# create countplot
sns.countplot(y="county", data=df_california)
