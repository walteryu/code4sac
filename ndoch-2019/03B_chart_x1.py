# 03B - Create chart

# Sort data by region for plotting
cost_by_region = df.groupby('').size()

# Output to check sort function
print(cost_by_region)

# Create chart
plot_by_area = cost_by_region.plot(title='')

# Add axis labels to chart
plot_by_area.set_xlabel('')
plot_by_area.set_ylabel('')
