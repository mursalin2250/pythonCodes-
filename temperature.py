import numpy as np
data = np.array([
    [25, 26, 24, 23, 27, 28, 29],
    [30, 31, 32, 33, 34, 35, 36],
    [20, 19, 18, 17, 16, 15, 14]
])

cities = ["City A", "City B", "City C"]
avg_temp = np.mean(data, axis=1)
for city, avg in zip(cities, avg_temp):
    print(f"Average temperature for {city}: {avg:.2f} °C")

hottest_temp = np.max(data)
print(f"Hottest temperature recorded: {hottest_temp} °C")

coolest_temp = np.min(data, axis=1)
for city, temp in zip(cities, coolest_temp):
    print(f"Coolest day in {city}: {temp} °C")
