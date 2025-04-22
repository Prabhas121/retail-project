# 8. Sales by Month
df_cleaned['InvoiceDate'] = pd.to_datetime(df_cleaned['InvoiceDate'], format='%d-%m-%Y %H:%M')
df_cleaned['Month'] = df_cleaned['InvoiceDate'].dt.month monthly_sales = df_cleaned.groupby("Month")["UnitPrice"].sum() plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="bar", color="teal") plt.title("Sales by Month") plt.xlabel("Month")
plt.ylabel("Total Sales") plt.xticks(rotation=0) plt.show()
