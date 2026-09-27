import matplotlib.pyplot as plt

continents = ["Asia", "Africa", "North America",
              "South America", "Antarctica", "Europe", "Australia"]

area = [44.58, 30.37, 24.71, 17.84, 14.20, 10.18, 8.53]

plt.bar(continents, area)

plt.title("Area of Continents")
plt.xlabel("Continents")
plt.ylabel("Area (million km²)")
plt.xticks(rotation=45)

plt.show()