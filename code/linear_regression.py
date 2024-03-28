import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Adatok beolvasása a CSV fájlból
df = pd.read_csv('Irrigation_scheduling_ML\\dataset.csv')

# Az utolsó sor kiválasztása a legfrissebb adatokhoz
latest_data_row = df.iloc[-1:][['Soil_Moisture', 'Humidity', 'Temperature']]
actual_hours_until_watering = df.iloc[-1]['Hours_Until_Watering']
df = df.iloc[:-1]  # Az utolsó sorral ne foglalkozzon tanulásban
X = df[['Soil_Moisture', 'Humidity', 'Temperature']]
y = df['Hours_Until_Watering']

# Adatok felszeletelése
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# A lineáris regresszió inicializálása és a modell betanítása
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Predikciók készítése a teszt set-eken
y_pred = model.predict(X_test_scaled)

# A modell teljesítéményének értékelése, tárolása majd kijelzése
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MSE: {mse}')
print(f'R^2: {r2}')

# Új manuálisan beállított adatok eltárolása
manual_data_df = pd.DataFrame([[80, 50, 20]], columns=['Soil_Moisture', 'Humidity', 'Temperature'])
# Ez a manuális adat skálázása
manual_data_scaled = scaler.transform(manual_data_df)
# Majd predikciója
predicted_hours_manual = model.predict(manual_data_scaled)

# A CSV fájl utolsó sorának skálázása
latest_data_scaled = scaler.transform(latest_data_row)
# Majd ennek is a predikciója
predicted_hours = model.predict(latest_data_scaled)

# Hogyha esetleg negatív órát írna ki akkor jelezze nullával
print(f'Actual Hours Until Watering: {actual_hours_until_watering}')
if float(predicted_hours[0]) < 0: 
    print(f'Predicted Hours Until Watering: 0')
else:
    print(f'Predicted Hours Until Watering: {round(predicted_hours[0], 2)}')

if float(predicted_hours_manual[0]) < 0:
    print(f'Predicted Hours Until Watering (manual): 0')
else:
    print(f'Predicted Hours Until Watering (manual): {round(predicted_hours_manual[0], 2)}')
