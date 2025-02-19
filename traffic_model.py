import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("traffic_data.csv")

# Feature Engineering
X = df[['vehicle_count', 'average_speed']]
y = df['congestion_level']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Machine Learning Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
print("Model Error:", mean_absolute_error(y_test, y_pred))

# Save Model
import joblib
joblib.dump(model, "traffic_model.pkl")
print("Model saved as traffic_model.pkl")
