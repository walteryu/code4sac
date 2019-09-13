# 03B - Create box plots for routes' Annual Vehicle Miles Traveled, by county
# Set plot size and title
plt.figure(figsize=(16, 12))
plt.title('Box Plot - Annual VMT by County')

# Create chart
ax = sns.boxplot(x="County", y="Annual_VMT", data=df)