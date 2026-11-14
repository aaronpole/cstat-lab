import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("lois_continuous.csv")
df = df.iloc[1:]
swale = df[df["Unnamed: 2"] == "Swale at Catterick Bridge"]
temperature = pd.to_numeric(swale["Temperature water continuous"],errors="coerce")
oxygen = pd.to_numeric(swale["Oxygen dissolved continuous"],errors = "coerce")
print("Temperature mean : ",temperature.mean())
print("Oxygen median : ",oxygen.median())

temperature.plot(kind="hist",bins=15,edgecolor="black")
plt.title("Water Temperature at Swale at Catterick Bridge")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.grid()
plt.show()
