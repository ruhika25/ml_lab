
df_stock = pd.read_excel(r'C:\Users\ruhisai\Downloads\Lab Session Data.xlsx', sheet_name='IRCTC Stock Price')

pop_mean = df_stock['Price'].mean()
print(f"Population Mean (all data): {pop_mean:.2f}")

for i in range(3):
    sample = df_stock.sample(20) 
    sample_mean = sample['Price'].mean()
    print(f"Sample {i+1} Mean (20 days): {sample_mean:.2f}")