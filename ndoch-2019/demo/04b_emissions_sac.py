# load data into notebook; make sure file is in folder as notebook
em = pd.read_csv('carb_2017_emissions_sac_v1.csv')

# print out first 5 lines of dataset below
print(em.head(5))

# inspect for data types and missing values (note: Pandas stores character strings as type 'object')
# print('Dataset information:\n')
# print(em.info())

# Create box plots
# Set plot size and title
plt.figure(figsize=(16, 12))
plt.title('Box Plot - CO^2 by Vehicle Speed')

# Create chart
ax = sns.boxplot(x="Speed", y="CO2_RUNEX", data=em)

# Create box plots
# Set plot size and title
plt.figure(figsize=(30, 12))
plt.title('Box Plot - CO^2 by Model Year')

# Create chart
ax = sns.boxplot(x="Model Year", y="CO2_RUNEX", data=em)

# Create box plots
# Set plot size and title
plt.figure(figsize=(30, 12))
plt.title('Box Plot - CO^2 by VMT')

# Create chart
ax = sns.scatterplot(x="VMT", y="CO2_RUNEX", data=em)

# Pairs plots
ax = sns.pairplot(em)
