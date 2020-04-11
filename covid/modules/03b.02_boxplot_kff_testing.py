# 03B.02 - create box plots

# set plot size and title
plt.figure(figsize=(16, 12))
plt.title('Box Plot: Total COVID-19 Tests with Results\n Note: Each Record = Total for Single US State')

# create boxplot
sns.boxplot(
    y="location",
    x="tests_with_results",
    data=df_results_plot
)

# check/replace null values and columns
# https://dzone.com/articles/pandas-find-rows-where-columnfield-is-null
# df_california.fillna(0)
df_results_plot.dropna()
# print(df_ca_plot.isnull().values.any())
null_columns = df_results_plot.columns[df_results_plot.isnull().any()]
print(df_results_plot[df_results_plot.isnull().any(axis=1)][null_columns].head())

# create plots
# sns.pairplot(df_results_plot)
# sns.heatmap(df_ca_plot)

# set plot size and title
plt.figure(figsize=(16, 12))
plt.title('Box Plot: Total COVID-19 Percent with Positive Results by US State\n Note: Each Record = Total for Single US State')

# create boxplot
sns.boxplot(
    y="location",
    x="percentage_test_positive",
    data=df_positive_plot
)

# set plot size and title
plt.figure(figsize=(16, 12))
plt.title('Box Plot: Total COVID-19 Tests per 1k Residents by US State\n Note: Each Record = Total for Single US State')

# create boxplot
sns.boxplot(
    y="location",
    x="total_tests_per_1k_residents",
    data=df_1k_plot
)
