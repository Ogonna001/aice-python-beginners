
# Practising Item Distribution

# Total items and number of groups
total_items =  fifty = 50
groups = 6

# Calculate complete shares
shares = total_items // groups

# Calculate leftover items
leftovers = total_items % groups

# Display distribution results
print("Total items:", total_items)
print("Number of groups:", groups)
print("Items per group:", shares)
print("Leftover items:", leftovers)

# Check whether the total number of items is even or odd
if total_items % 2 == 0:
    print("The total number of items is even.")
else:
    print("The total number of items is odd.")

