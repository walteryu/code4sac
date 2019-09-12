# 03A - Histogram plot

# Set plot size and title
plt.figure(figsize=(16, 8))
plt.title('Histogram Plot - Annual VMT')

# Create historgram for total cost
sns.distplot(df['Annual_VMT'])
