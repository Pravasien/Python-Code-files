import pandas as pd
import numpy as np
data = {
    "Id": [1, 2, 3, 4],
    "Name": ["Pankaj", "Meghna", "David", "Lisa"],
    "Role": ["CEO", np.nan, np.nan, np.nan],
    "Salary": [100, 200, np.nan, np.nan]
}
dataframe_1 = pd.DataFrame(data)
print(" Initial DataFrame ")
print(dataframe_1)
print("Initial 2 rows (Head)")
print(dataframe_1.head(2))
print("Last 2 rows (Tail)")
print(dataframe_1.tail(2))
print("Detailed Info")
dataframe_1.info()
dataframe_dropped_rows_null = dataframe_1.dropna()
print("DataFrame after dropping rows with nulls")
print(dataframe_dropped_rows_null)
df_dropped_cols = dataframe_1.dropna()
print("DataFrame after dropping columns with nulls")
print(df_dropped_cols)
dataframe_1["Salary"] = dataframe_1["Salary"].fillna(300)
print("Updated DataFrame (Salary filled with 300)")
print(dataframe_1)
dataframe_1["Role"] = dataframe_1["Role"].fillna("CEO")
print("Final Updated DataFrame (Role filled with CEO)")
print(dataframe_1)