import pandas as pd
df = pd.read_csv("state.csv")
print("Mean\n",df[["Population","Murder"]].mean())
print("\n")
print("Median\n",df[["Population","Murder"]].median())
print("\n")
print("Variance\n",df[["Population","Murder"]].var())