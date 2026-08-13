import pandas as pd
from sklearn.preprocessing import LabelEncoder

# here we load the dataset
df = pd.read_excel("Lab Session Data.xlsx", sheet_name="marketing_campaign")

# label encoding funciton
def lbl_enc(df, cols):
    df = df.copy()
    le = LabelEncoder()

    for c in cols:
        df[c] = le.fit_transform(df[c].astype(str))

    return df

# one hot encoding function
def oh_enc(df, cols):
    df = df.copy()
    df = pd.get_dummies(df, columns=cols)
    return df

# categoricall
cols = ["Education", "Marital_Status"]

#running functions
df_lbl = lbl_enc(df, cols)
print("Label Encoding")
print(df_lbl.head())
gdf_hot = oh_enc(df, cols)
print("\nOne Hot Encoding")
print(df_hot.head())

# original shape
print("Origi shape:", df.shape)

# label encoded ddata
df_lbl = lbl_enc(df, cols)
print("Label shape:", df_lbl.shape)

# one hot encoded dta
df_hot = oh_enc(df, cols)
print("One Hot Encoded shape:", df_hot.shape)


