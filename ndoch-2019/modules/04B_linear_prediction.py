# 4B - Prediction model with linear regresion:
# https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f

# Modules for prediction model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Reshape cost columns as predictor variables
X = df['Incidents_Per_Million_VMT'].values.reshape(-1,1)
y = df['Annual_VHD_at_35mph'].values.reshape(-1,1)

# Split data into training and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create prediction model and fit data to model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Output the intercept/coefficient
    # note our coefficients will be different from stats.linregress(), as here we fit on a training *subset* of data
print('*** Intercept and Coefficient Values ***')
print('')
print('Intercept Value (Prediction Model) =', regressor.intercept_)
print('')
print('Coefficient Value (Prediction Model) =', regressor.coef_)
print('')

# Predict total cost with linear regresion
y_pred = regressor.predict(X_test)

# Output error metrics
print('*** Error Metrics ***')
print('')
print('Mean Absolute Error =', metrics.mean_absolute_error(y_test, y_pred))
print('')
print('Mean Squared Error =', metrics.mean_squared_error(y_test, y_pred))
print('')
print('Root Mean Squared Error =', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('')

# Output results
df_results = pd.DataFrame(
  {'Actual Values': y_test.flatten(), 'Predicted Values': y_pred.flatten()}
)
df_results