import pandas as pd

data = {
    'Department': ['IT', 'IT', 'HR', 'HR', 'Sales', 'Sales'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Salary': [50000, 55000, 45000, 48000, 40000, 42000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


pivot = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    columns='Gender',
    aggfunc='mean'
)

print("\nPivot Table:")
print(pivot)


crosstab = pd.crosstab(
    df['Department'],
    df['Gender']
)

print("\nCross Tabulation:")
print(crosstab)