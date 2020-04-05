# 4A - simple linear regresion (slr) with stat functions

# create slr vars
x = df_california['cases']
y = df_california['deaths']

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

print("*** linear regression results ***")
print("y-slope =", round(slope, 4))
print("y-intercept =", round(intercept, 4))
print("r-squared value =", round(r_value**2, 4))

# Linear regression plot
plt.figure(figsize=(16, 12))
plt.title('SLR Plot: Total CA Deaths-Cases (As of 04-03-2020)')
sns.regplot(x=x, y=y, data=df_california)
