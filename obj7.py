# 7. Count of Orders by CustomerID
customer_orders = df_cleaned["CustomerID"].value_counts().head(10) plt.figure(figsize=(12, 6))
sns.barplot(x=customer_orders.index, y=customer_orders.values, palette="Blues")
plt.title("Top 10 Customers by Number of Orders") plt.xlabel("CustomerID")
plt.ylabel("Number of Orders") plt.xticks(rotation=90)
 
plt.show()

