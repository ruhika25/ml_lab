import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# load data
df=pd.read_excel("Lab Session Data.xlsx",sheet_name="marketing_campaign")

# label encoding
le=LabelEncoder()

for c in ["Education","Marital_Status"]:
    df[c]=le.fit_transform(df[c].astype(str))

# minkowski function
def mink_dist(x,y,p):
    s=0

    for i in range(len(x)):
        s+=abs(x[i]-y[i])**p

    return s**(1/p)

# first two rows
num=df.select_dtypes(include=np.number)

x=num.iloc[0].values
y=num.iloc[1].values

d=[]

for p in range(1,11):
    d.append(mink_dist(x,y,p))

print(d)

plt.plot(range(1,11),d,marker='o')
plt.xlabel("p")
plt.ylabel("Distance")
plt.title("Minkowski Distance")
plt.grid(True)
plt.show()