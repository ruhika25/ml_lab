import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


stock_df = pd.read_excel(
    r"C:\Users\ruhisai\Downloads\Lab Session Data.xlsx",
    sheet_name="IRCTC Stock Price"
)


stock_df["Date"] = pd.to_datetime(stock_df["Date"])
stock_df["Weekday"] = stock_df["Date"].dt.day_name()
stock_df["MonthNumber"] = stock_df["Date"].dt.month


stock_prices = stock_df["Price"].to_numpy()
daily_change = stock_df["Chg%"].to_numpy()

def calculate_mean(values):
    total = sum(values)
    return total / len(values)


def calculate_variance(values):
    avg = calculate_mean(values)
    variance = sum((value - avg) ** 2 for value in values) / len(values)
    return variance


print("Mean using NumPy:", np.mean(stock_prices))
print("Mean using Custom Function:", calculate_mean(stock_prices))

print("Variance using NumPy:", np.var(stock_prices))
print("Variance using Custom Function:", calculate_variance(stock_prices))


start_time = time.time()
for _ in range(10):
    np.mean(stock_prices)
numpy_avg_time = (time.time() - start_time) / 10

start_time = time.time()
for _ in range(10):
    calculate_mean(stock_prices)
custom_avg_time = (time.time() - start_time) / 10

print("Average NumPy Execution Time:", numpy_avg_time)
print("Average Custom Execution Time:", custom_avg_time)


wednesday_data = stock_df[stock_df["Weekday"] == "Wednesday"]["Price"]

print("Overall Average Price:", np.mean(stock_prices))
print("Wednesday Average Price:", np.mean(wednesday_data))


april_data = stock_df[stock_df["MonthNumber"] == 4]["Price"]
print("April Average Price:", np.mean(april_data))

loss_probability = (stock_df["Chg%"] < 0).sum() / len(stock_df)
print("Probability of Loss:", loss_probability)

wednesday_profit = stock_df[
    (stock_df["Weekday"] == "Wednesday") &
    (stock_df["Chg%"] > 0)
]

print(
    "Probability of Profit on Wednesday (Overall):",
    len(wednesday_profit) / len(stock_df)
)


total_wednesdays = len(stock_df[stock_df["Weekday"] == "Wednesday"])
conditional_probability = len(wednesday_profit) / total_wednesdays

print("P(Profit | Wednesday):", conditional_probability)

plt.scatter(stock_df["Weekday"], stock_df["Chg%"])
plt.axhline(0, linestyle="--")
plt.title("Percentage Change by Day of the Week")
plt.xlabel("Day")
plt.ylabel("Daily Change (%)")
plt.show()