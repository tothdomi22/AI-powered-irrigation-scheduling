import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Irrigation_scheduling_ML\dataset.csv')

latest_data_row = df.iloc[-1:][['Soil_Moisture', 'Humidity', 'Temperature']]
actual_hours_until_watering = df.iloc[-1]['Hours_Until_Watering']
df = df.iloc[:-1] 
X = df[['Soil_Moisture', 'Humidity', 'Temperature']]
y = df['Hours_Until_Watering']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MSE: {mse}')
print(f'R^2: {r2}')


new_data = scaler.transform([[78, 50, 20]])
predicted_hours_manual = model.predict(new_data)

latest_data_scaled = scaler.transform(latest_data_row)
predicted_hours = model.predict(latest_data_scaled)



print(f'Actual Hours Until Watering: {actual_hours_until_watering}')

if float(predicted_hours[0])<0: 
    print(f'Predicted Hours Until Watering: 0')
else:
    print(f'Predicted Hours Until Watering: {predicted_hours[0]}')

if float(predicted_hours_manual[0])<0:
    print(f'Predicted Hours Until Watering (manual): 0')
else:
    print(f'Predicted Hours Until Watering (manual): {predicted_hours_manual[0]}')
