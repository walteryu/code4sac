# 03A - histogram plot

# create histogram
# `kde=False` turns off the default density estimate plot
# sns.distplot(clients_enrollments['client_ethnicity'], kde=False)

# set plot size and title
plt.figure(figsize=(12, 8))
plt.title('Count Plot: Clients/Enrollments - Ethnicity')

# create countplot
sns.countplot(y="client_ethnicity", data=clients_enrollments)

# set plot size and title
plt.figure(figsize=(12, 8))
plt.title('Count Plot: Enrollments/Exits - Exit Reason')

# create countplot
sns.countplot(y="exit_reason", data=enrollments_exits)

# set plot size and title
plt.figure(figsize=(12, 8))
plt.title('Count Plot: Enrollments/Services - Service Category')

# create countplot
sns.countplot(y="service_category", data=enrollments_services)
