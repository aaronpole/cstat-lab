import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("BankChurners.csv")

# Handle missing values
num_cols = df.select_dtypes(include='number').columns
cat_cols = df.select_dtypes(exclude='number').columns

df[num_cols] = df[num_cols].fillna(df[num_cols].median())

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# 1. Attrition Flag Ratio
df['Attrition_Flag'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Attrition Flag Ratio")
plt.ylabel("")
plt.show()

# 2. Bar Charts
sns.countplot(data=df, x='Gender')
plt.title("Gender Distribution")
plt.show()

sns.countplot(data=df, x='Card_Category')
plt.title("Card Category Distribution")
plt.show()

# 3. Box Plots
sns.boxplot(data=df, y='Credit_Limit')
plt.title("Credit Limit")
plt.show()

sns.boxplot(data=df, y='Total_Trans_Amt')
plt.title("Transaction Amount")
plt.show()

# 4. Descriptive Statistics
print("Descriptive Statistics:")
print(df.describe().round(2))

# 5. Correlation Heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(
    df.select_dtypes(include='number').corr(),
    cmap='coolwarm'
)
plt.title("Correlation Heatmap")
plt.show()

# 6. Remove unnecessary columns
removed = [
    'CLIENTNUM',
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon',
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_1'
]

removed = [col for col in removed if col in df.columns]
df.drop(columns=removed, inplace=True)

print("\nColumns Removed:")
print(removed)