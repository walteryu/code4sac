# 03C - Create chart

# Add axis labels to chart
plot_by_area.set_xlabel('')
plot_by_area.set_ylabel('')

# Sort data by region for plotting
cost_by_area = df.groupby('').size()

# Output to check sort function
print(cost_by_area)

# Create chart
plot_by_area = cost_by_area.plot(title='')

# Add axis labels to chart
plot_by_area.set_xlabel('')
plot_by_area.set_ylabel('')
