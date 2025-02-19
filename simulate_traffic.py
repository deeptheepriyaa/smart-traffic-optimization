import numpy as np
import pandas as pd
import time

def generate_traffic_data():
    traffic_data = {
        'timestamp': [],
        'location': [],
        'vehicle_count': [],
        'average_speed': [],
        'congestion_level': []
    }

    locations = ['Intersection_A', 'Intersection_B', 'Intersection_C']

    for _ in range(500):  # Simulate 500 data points
        location = np.random.choice(locations)
        vehicle_count = np.random.randint(5, 50)
        avg_speed = np.random.uniform(10, 60)  # Speed in km/h
        congestion_level = max(0, (50 - vehicle_count) / 50)  # Normalize congestion (0 to 1)

        traffic_data['timestamp'].append(pd.Timestamp.now())
        traffic_data['location'].append(location)
        traffic_data['vehicle_count'].append(vehicle_count)
        traffic_data['average_speed'].append(avg_speed)
        traffic_data['congestion_level'].append(congestion_level)

        time.sleep(0.1)  # Simulate real-time data flow

    df = pd.DataFrame(traffic_data)
    df.to_csv("traffic_data.csv", index=False)
    print("Traffic data simulation complete. Saved to traffic_data.csv.")

generate_traffic_data()
