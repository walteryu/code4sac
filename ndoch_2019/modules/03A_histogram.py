# 03A - Histogram plot

# Set plot size and title
plt.figure(figsize=(16, 8))
plt.title('Histogram Plot - Annual VMT')

# Create historgram for Annual Vehicle Miles Traveled
sns.distplot(df['Annual_VMT'], kde=False) # `kde=False` turns off the default density estimate plot, try setting it to True !