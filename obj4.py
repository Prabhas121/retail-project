# 4. Average UnitPrice by Country avg_price_country =
df_cleaned.groupby("Country")["UnitPrice"].mean().sort_values(ascendin g=False)
plt.figure(figsize=(12, 6))
sns.barplot(x=avg_price_country.index, y=avg_price_country.values, palette="viridis")
plt.title("Average UnitPrice by Country") plt.xlabel("Country") plt.ylabel("Average Unit Price") plt.xticks(rotation=90)
plt.show()
