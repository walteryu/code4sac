# 4A - Statistical functions with linear regresion

# Linear regression of Annual_VHD_at_35mph on Incidents_Per_Million_VMT

x = df['Incidents_Per_Million_VMT']
y = df['Annual_VHD_at_35mph']

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

print("*** linear regression results ***")
print("slope of total and labor cost =", round(slope, 4))
print("y-int of total and labor cost =", round(intercept, 4))
print("r-squared value of total and labor cost =", round(r_value**2, 4))

# Linear regression plot
plt.figure(figsize=(16, 12))
sns.regplot(x=x, y=y, data=df)