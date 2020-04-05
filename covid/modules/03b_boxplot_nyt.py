# 03b - create box plots

# set plot size and title
plt.figure(figsize=(16, 12))
plt.title('Box Plot: Total CA Cases by County (As of 04-03-2020)')

# create chart
ax = sns.boxplot(
    y="county",
    x="cases",
    data=df_california
)
