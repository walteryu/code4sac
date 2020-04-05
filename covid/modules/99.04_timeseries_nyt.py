# 04D time series analysis
# ref: https://towardsdatascience.com/time-series-analysis-in-python-an-introduction-70d5a5b1d52a

import fbprophet
# Prophet requires columns ds (Date) and y (value)
df_california = df_california.rename(columns={'date': 'ds', 'cases': 'y'})

# Make the prophet model and fit on the data
ca_prophet = fbprophet.Prophet(changepoint_prior_scale=0.15)
ca_prophet.fit(df_california)
