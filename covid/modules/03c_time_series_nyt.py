# 03c - create time series

# create chart and adjust figure size
# ref: https://www.drawingfromdata.com/setting-figure-size-using-seaborn-and-matplotlib
df_california.plot(x='date', y='cases', figsize=(20,10))
plt.title(
    'Time Series: Total CA Cases by County (As of 04-03-2020)'
)
