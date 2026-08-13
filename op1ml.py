import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

stock = pd.read_excel(
    r"C:\Users\ruhisai\Downloads\Lab Session Data.xlsx",
    sheet_name="IRCTC Stock Price"
)

stock["Date"] = pd.to_datetime(stock["Date"])
stock["Day"] = stock["Date"].dt.day_name()
stock["Month"] = stock["Date"].dt.month

price = stock["Price"].to_numpy()

def mean_val(data):
    return sum(data) / len(data)

def var_val(data):
    avg = mean_val(data)
    return sum((x - avg) ** 2 for x in data) / len(data)

print("Mean (NumPy):", np.mean(price))
print("Mean (Custom):", mean_val(price))
print("Variance (NumPy):", np.var(price))
print("Variance (Custom):", var_val(price))

start = time.time()
for _ in range(10):
    np.mean(price)
numpy_time = (time.time() - start) / 10

start = time.time()
for _ in range(10):
    mean_val(price)
custom_time = (time.time() - start) / 10

print("NumPy Time:", numpy_time)
print("Custom Time:", custom_time)

wed = stock[stock["Day"] == "Wednesday"]["Price"]
apr = stock[stock["Month"] == 4]["Price"]

print("Overall Mean:", np.mean(price))
print("Wednesday Mean:", np.mean(wed))
print("April Mean:", np.mean(apr))


loss_prob = (stock["Chg%"] < 0).sum() / len(stock)
wed_profit = len(stock[(stock["Day"] == "Wednesday") & (stock["Chg%"] > 0)])
total_wed = len(stock[stock["Day"] == "Wednesday"])

print("Loss Probability:", loss_prob)
print("Profit on Wednesday:", wed_profit / len(stock))
print("P(Profit | Wednesday):", wed_profit / total_wed)

plt.scatter(stock["Day"], stock["Chg%"])
plt.axhline(0, linestyle="--")
plt.title("Chg% vs Day")
plt.show()