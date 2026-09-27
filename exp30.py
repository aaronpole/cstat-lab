import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("lois_continuous.csv")

# Remove units row
df = df.iloc[1:]

# Filter records
swale = df[df["Unnamed: 2"] == "Swale at Catterick Bridge"]

# Convert to numeric
temperature = pd.to_numeric(
    swale["Temperature water continuous"],
    errors="coerce"
)

oxygen = pd.to_numeric(
    swale["Oxygen dissolved continuous"],
    errors="coerce"
)

# Calculate values
mean_temperature = temperature.mean()
median_oxygen = oxygen.median()

print("Mean Temperature:", round(mean_temperature, 2))
print("Median Dissolved Oxygen:", round(median_oxygen, 2))

# Plot histogram
temperature.plot(
    kind="hist",
    bins=15,
    edgecolor="black"
)

plt.title("Water Temperature at Swale at Catterick Bridge")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()