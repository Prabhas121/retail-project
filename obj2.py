Quantity Distribution

plt.figure(figsize=(8, 5))
sns.histplot(df_cleaned["Quantity"], bins=30, kde=True, color="green")
plt.title("Distribution of Quantity")
plt.xlabel("Quantity") plt.ylabel("Frequency") plt.show()
