import numpy as np

temperatures = np.array([28, 32, 29, 35, 31, 27, 33])

print("Average Temperature:", np.mean(temperatures))
print("Highest Temperature:", np.max(temperatures))
print("Lowest Temperature:", np.min(temperatures))

days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday",
                 "Friday", "Saturday", "Sunday"])

print("Days above 30°C:", days[temperatures > 30])

updated_temperatures = temperatures + 2

print("Updated Temperatures:", updated_temperatures)