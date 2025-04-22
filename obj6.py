# 6. Top 10 Most Purchased Products by Quantity top_products =
df_cleaned.groupby("Description")["Quantity"].sum().nlargest(10) top_products.plot(kind="bar", figsize=(12, 6), color="coral") plt.title("Top 10 Most Purchased Products by Quantity") plt.xlabel("Product Description")
plt.ylabel("Total Quantity Purchased") plt.xticks(rotation=45)
plt.show()

