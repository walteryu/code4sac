# 03D - box plots for enrollments-exits duration

# Set plot size and title
plt.figure(figsize=(16, 12))
plt.title('Box Plot: Enrollments-Exits - Time Duration in Days by Gender')

# Create chart
ax = sns.boxplot(
    y="client_gender",
    x="enrollment_exit_time",
    data=enrollments_exits
)
