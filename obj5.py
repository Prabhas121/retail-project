# 5. Quantity vs Unit Price plt.figure(figsize=(8, 5))
sns.scatterplot(x=df_cleaned["Quantity"], y=df_cleaned["UnitPrice"], color='blue', alpha=0.5)
plt.title("Quantity vs Unit Price") plt.xlabel("Quantity") plt.ylabel("Unit Price") plt.show()
