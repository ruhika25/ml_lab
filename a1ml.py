import pandas as pd
import numpy as np

df = pd.read_excel("Lab Session Data.xlsx", sheet_name="Purchase Data")

print(df)


X = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]].values

y = df["Payment (Rs)"].values

print("\nX =")
print(X)

print("\ny =")
print(y)