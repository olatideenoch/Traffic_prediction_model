import pandas as pd
import numpy as np

np.random.seed(42)

n = 100

data = pd.DataFrame({
    'hour': np.random.randint(0, 24, n),
    'day_of_week': np.random.randint(1, 8, n),
    'is_weekend': np.random.randint(0, 2, n),
    'is_holiday': np.random.randint(0, 2, n),
    'current_volume': np.random.randint(100, 2000, n),
    'previous_hour_volume': np.random.randint(100, 2000, n),
    'road_capacity': np.random.randint(800, 2500, n),
    'average_speed': np.random.randint(5, 80, n),
    'rainfall_mm': np.random.randint(0, 30, n),
    'temperature': np.random.randint(20, 38, n),
    'event_nearby': np.random.randint(0, 2, n),
    'accident_reported': np.random.randint(0, 2, n),
    'road_work': np.random.randint(0, 2, n),
    'bus_frequency': np.random.randint(5, 30, n),
    'signal_density': np.random.randint(1, 15, n),
    'lane_count': np.random.randint(1, 6, n),
    'population_density': np.random.randint(1000, 15000, n)
})

# Create congestion target

congestion_score = (
    (data['current_volume'] / data['road_capacity']) * 50
    + data['rainfall_mm'] * 1.5
    + data['event_nearby'] * 10
    + data['accident_reported'] * 15
    + data['road_work'] * 10
    - data['average_speed'] * 0.4
)

data['congestion'] = np.where(congestion_score > 35, 1, 0)

# Create delay target

data['delay_minutes'] = (
    congestion_score
    + np.random.normal(0, 5, n)
).round(1)

data['delay_minutes'] = data['delay_minutes'].clip(lower=0)

data.to_csv('transport_dataset.csv', index=False)

print(data.head())
print("\nDataset shape:", data.shape)