# 03c - create time series

# Create chart
ax = df_california.plot(x='date', y='cases')
ax = plt.title(
    'Time Series: Total CA Cases by County (As of 04-03-2020)'
)
ax = plt.rcParams["figure.figsize"] = (16,12)
