# 4C - prediction model with linear regresion:
# https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f

# plot a randomly sampled 25 values
df_25 = df_results.sample(25)
df_25.plot(kind='bar',figsize=(16,10))

# create bar plot of actual and predicted values
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
