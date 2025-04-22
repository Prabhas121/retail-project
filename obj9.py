# 9. Heatmap of Correlation Between Numerical Features numerical_df = df_cleaned.select_dtypes(include=["number"]) correlation_matrix = numerical_df.corr() plt.figure(figsize=(12, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5) plt.title("Correlation Heatmap of Numerical Features") plt.show()
