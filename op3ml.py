import pandas as pd
import numpy as np


marketing_data = pd.read_excel(
    r"C:\Users\Ruhisai\Downloads\Lab Session Data.xlsx",
    sheet_name="marketing_campaign"
)

print("Columns in the dataset:")
print(marketing_data.columns)

features = marketing_data[["Kidhome", "Teenhome"]].to_numpy()


target = marketing_data["Income"].to_numpy()

coefficients = np.linalg.pinv(features).dot(target)

# Print the resulting coefficients
print("Calculated coefficients:")
print(coefficients)