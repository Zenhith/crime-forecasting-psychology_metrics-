
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# Load MHA data (replace 'MHA_PATH' with your actual CSV path)
mha_path = '2021-2024_MHA.csv'
mha_data = pd.read_csv(mha_path)

# Load Crime data (replace 'CRIME_PATH' with your actual Excel path)
crime_path = '2020-2023_CO.xlsx'
crime_data = pd.read_excel(crime_path, sheet_name=None)

# Concatenate all sheets from the crime data Excel file
crime_data_combined = pd.concat(crime_data.values(), ignore_index=True)

# Add a 'Year' column to match the format of the MHA data
crime_data_combined['Year'] = crime_data_combined['Financial Year'].str.split('/').str[0]

# Aggregate MHA data by year
mha_data['Year'] = mha_data['Year'].astype(str)
mha_aggregated = mha_data.groupby('Year').agg({
    'Total_Count': 'sum',
    'CrudeRate': 'mean'
}).reset_index()

# Aggregate crime data by year and offence group
crime_aggregated = crime_data_combined.groupby(['Financial Year', 'Offence Group']).agg({
    'Number of Offences': 'sum'
}).reset_index()
crime_aggregated['Year'] = crime_aggregated['Financial Year'].str.split('/').str[0]

# Merge crime data with MHA data on 'Year'
merged_data = pd.merge(crime_aggregated, mha_aggregated, on='Year', how='left')

# Convert 'Total_Count' to a numeric value
merged_data['Total_Count'] = pd.to_numeric(merged_data['Total_Count'], errors='coerce')

# Prepare the features (X) and target (y)
X = merged_data[['Total_Count', 'CrudeRate']]
y = merged_data['Number of Offences']

# Handle missing values in X
X = X.fillna(0)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Initialize models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
}

# Train and evaluate each model
model_performance = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    model_performance[model_name] = {'MAE': mae, 'RMSE': rmse}

# Display model performance
performance_df = pd.DataFrame(model_performance).transpose()
print('Model Performance:')
print(performance_df)

# Choose the best model (e.g., Random Forest) for prediction
best_model = RandomForestRegressor(n_estimators=100, random_state=42)
best_model.fit(X_train, y_train)

# Predict using the best model
y_pred = best_model.predict(X_test)

# Display predictions
predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print('Predictions:')
print(predictions_df.head())
