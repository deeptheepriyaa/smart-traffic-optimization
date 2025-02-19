import joblib
import random

# Load trained model
model = joblib.load("traffic_model.pkl")

# Simulated Traffic Data Input
def get_live_traffic_data():
    return {
        "vehicle_count": random.randint(5, 50),
        "average_speed": random.uniform(10, 60)
    }

# Adjust Traffic Signal Duration Based on AI Predictions
def control_traffic_lights():
    data = get_live_traffic_data()
    congestion_prediction = model.predict([[data["vehicle_count"], data["average_speed"]]])[0]
    
    # Traffic Light Timing Logic
    if congestion_prediction > 0.7:
        signal_time = 30  # Red light for 30s
    elif congestion_prediction > 0.4:
        signal_time = 15  # Moderate delay
    else:
        signal_time = 5  # Fast clearance
    
    print(f"Vehicle Count: {data['vehicle_count']}, Avg Speed: {data['average_speed']:.2f}")
    print(f"Predicted Congestion: {congestion_prediction:.2f}")
    print(f"Traffic Light Duration: {signal_time}s")

for _ in range(10):  # Simulate 10 traffic light cycles
    control_traffic_lights()
