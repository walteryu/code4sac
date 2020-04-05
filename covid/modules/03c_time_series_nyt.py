# 03c - create time series

# Set plot size and title
plt.figure(figsize=(16, 12))
plt.title('Time Series: Total CA Cases by County (As of 04-03-2020)')

# Create chart
ax = sns.tsplot(
    data=df_california,
    time="date",
    unit="cases",
    condition="county",
    value="Total Cases"
)
