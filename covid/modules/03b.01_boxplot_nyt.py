# 03B.01 - create box plots

# set plot size and title
plt.figure(figsize=(16, 12))
plt.title('Box Plot: Total CA Cases by County')

# create boxplot
sns.boxplot(
    y="county",
    x="cases",
    data=df_california
)

# check/replace null values and columns
# https://dzone.com/articles/pandas-find-rows-where-columnfield-is-null
# df_california.fillna(0)
df_ca_plot = df_california[['county', 'cases', 'deaths']]
df_ca_plot.dropna()
# print(df_ca_plot.isnull().values.any())
# null_columns=df_ca_plot.columns[df_ca_plot.isnull().any()]
# print(df_ca_plot[df_ca_plot.isnull().any(axis=1)][null_columns].head())

# create plots
# sns.pairplot(df_ca_plot)
# sns.heatmap(df_ca_plot)
