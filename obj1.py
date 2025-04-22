CustomerID Completeness

plt.figure(figsize=(8, 5))
missing_customer = df["CustomerID"].isnull().sum()
available_customer = df["CustomerID"].notnull().sum()
plt.bar(["Available Data", "Missing Data"], [available_customer, missing_customer], color=["lightgreen", "lightblue"])
plt.title("Availability of CustomerID Data")
 
plt.ylabel("Number of Entries") plt.show()
