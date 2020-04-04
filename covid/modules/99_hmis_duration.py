# 03B create enrollment-exit time duration column

# reference: https://stackoverflow.com/questions/37840812/pandas-subtracting-two-date-columns-and-the-result-being-an-integer
enrollments_exits['enrollment_exit_time'] = enrollments_exits['entry_screen_creation_date'].sub(enrollments_exits['project_exit_date'], axis=0)
print(enrollments_exits.info())

# note: address date typos and null values
# reference:
enrollments_exits['enrollment_exit_time'] = enrollments_exits['enrollment_exit_time'] / np.timedelta64(1, 'D')
