# 03A.01 - create count plot

# create histogram
# `kde=False` turns off the default density estimate plot
# sns.distplot(clients_enrollments['client_ethnicity'], kde=False)

# set plot size and title
plt.figure(figsize=(12, 8))
plt.title('Count Plot: Total Case Count by US State')

# create countplot and sort categories by value
# https://stackoverflow.com/questions/46623583/seaborn-countplot-order-categories-by-count
sns.countplot(
    y="state",
    data=df_total,
    order = df_total['state'].value_counts().index
)

# set plot size and title
plt.figure(figsize=(12, 8))
plt.title('Count Plot: Total Case Count in CA by County')

# create countplot and sort categories by value
# https://stackoverflow.com/questions/46623583/seaborn-countplot-order-categories-by-count
sns.countplot(
    y="county",
    data=df_california,
    order = df_california['county'].value_counts().index
)
