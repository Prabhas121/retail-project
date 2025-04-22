
# 3. Proportion of Orders by Country
country_orders = df_cleaned["Country"].value_counts() plt.figure(figsize=(10, 5)) sns.barplot(x=country_orders.index, y=country_orders.values, palette="Set2")
plt.title("Proportion of Orders by Country") plt.xlabel("Country")
plt.ylabel("Number of Orders") plt.xticks(rotation=90) plt.show()
