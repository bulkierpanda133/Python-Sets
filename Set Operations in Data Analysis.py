#Task 1: Duplicate Entries Cleanup

# List of customer IDs with duplicates
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Remove duplicates by converting the list to a set
unique_customer_ids = set(customer_ids)

# Display the unique customer IDs
print("Unique customer IDs:", unique_customer_ids)
