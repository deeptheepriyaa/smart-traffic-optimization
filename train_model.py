import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Sample dataset (Replace with actual traffic data)
X = np.random.rand(100, 2) * 100  # Random features (vehicle count, avg speed)
y = np.random.rand(100) * 10      # Random target (traffic flow score)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the new model
joblib.dump(model, "traffic_model.pkl")

print("✅ Model re-trained and saved successfully!")
