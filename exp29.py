import pandas as pd

df = pd.read_csv("state.csv")

print("Mean:")
print(df[["Population", "Murder"]].mean())

print("\nMedian:")
print(df[["Population", "Murder"]].median())

print("\nVariance:")
print(df[["Population", "Murder"]].var())