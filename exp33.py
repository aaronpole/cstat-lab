import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("Dataset_Ques_1_4.csv")

months = df["month_number"]

# (a) Total Profit Line Plot
plt.plot(months, df["total_profit"])
plt.title("Total Profit")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.show()


# (b) Styled Line Plot
plt.plot(months, df["total_profit"],
         color="red", linestyle="--",
         marker="o", linewidth=2)

plt.title("Styled Total Profit Plot")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.show()


# (c) Multi-line Plot
plt.plot(months, df["facecream"], label="Face Cream")
plt.plot(months, df["facewash"], label="Face Wash")
plt.plot(months, df["toothpaste"], label="Toothpaste")
plt.plot(months, df["bathingsoap"], label="Bathing Soap")

plt.title("Product Sales")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.legend()
plt.show()


# (d) Scatter Plot
plt.scatter(df["toothpaste"], df["bathingsoap"])

plt.title("Toothpaste vs Bathing Soap Sales")
plt.xlabel("Toothpaste")
plt.ylabel("Bathing Soap")
plt.show()


# (e) Bar Chart
plt.bar(months, df["total_profit"])

plt.title("Monthly Total Profit")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.show()


# (f) Bar Chart and Save Figure
plt.bar(months, df["total_profit"])

plt.title("Monthly Total Profit")
plt.xlabel("Month")
plt.ylabel("Total Profit")

plt.savefig("total_profit_bar.png")
plt.show()


# (g) Histogram
plt.hist(df["total_profit"], bins=5, edgecolor="black")

plt.title("Total Profit Distribution")
plt.xlabel("Total Profit")
plt.ylabel("Frequency")
plt.show()


# (h) Pie Chart
products = [
    "Face Cream", "Face Wash", "Toothpaste",
    "Bathing Soap", "Shampoo", "Moisturizer"
]

sales = [
    df["facecream"].sum(),
    df["facewash"].sum(),
    df["toothpaste"].sum(),
    df["bathingsoap"].sum(),
    df["shampoo"].sum(),
    df["moisturizer"].sum()
]

plt.pie(sales, labels=products, autopct="%1.1f%%")

plt.title("Total Product Sales")
plt.show()


# (i) Subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(months, df["total_profit"])
axes[0, 0].set_title("Total Profit")

axes[0, 1].bar(months, df["total_units"])
axes[0, 1].set_title("Total Units")

axes[1, 0].plot(months, df["facecream"])
axes[1, 0].set_title("Face Cream Sales")

axes[1, 1].plot(months, df["toothpaste"])
axes[1, 1].set_title("Toothpaste Sales")

plt.tight_layout()
plt.show()


# (j) Stack Plot
plt.stackplot(
    months,
    df["facecream"],
    df["facewash"],
    df["toothpaste"],
    df["bathingsoap"],
    df["shampoo"],
    df["moisturizer"],
    labels=products
)

plt.title("Stacked Product Sales")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.legend(loc="upper left")
plt.show()