import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("traffic_data.csv")

# Basic Stats
print(df.describe())

# Plot Vehicle Count Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['vehicle_count'], bins=20, kde=True)
plt.title("Vehicle Count Distribution")
plt.xlabel("Vehicle Count")
plt.ylabel("Frequency")
plt.show()

