'''Exercise 1'''

import pandas as pd

df = pd.read_csv("iris2.csv")

print(df.head(5))
print(df.dtypes)
print(df.describe())

'''Exercise 2'''

#identify columns
import pandas as pd

df = pd.read_csv("iris2.csv")

columns_with_missing = df.colulmns[df.isnull().sum() > 0]

for column in columns_with_missing:
    if pd.api.types.is_numeric_dtype(df[column]):
        df[column].fillna(df[column].mean(), inplace=True)
df.dropna(subset=columns_with_missing, Inplace=True)

df['new_columns'] = df['existing.column'] * 2

print (df)

