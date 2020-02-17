# 03E - box plots for enrollments-exits duration

# Set plot size and title
plt.figure(figsize=(16, 12))
plt.title('Box Plot: Enrollments-Exits - Time Duration in Days by Veteran Status')

# Create chart
ax = sns.boxplot(
    y="client_veteran_status",
    x="enrollment_exit_time",
    data=enrollments_exits
)
