# 04D logistic regression

# ref: https://pythonfordatascience.org/logistic-regression-python/

sns.regplot(
    x= 'cases',
    y= 'deaths',
    data= df_california,
    logistic= True
).set_title("Total CA Cases: Log Odds Linear Plot")
