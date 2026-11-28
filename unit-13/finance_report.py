
# Financial Report Using Python Math Functions

import math

# Business financial data
sales = [25000, 35000, 40000, 30000, 50000]
expenses = 65000

# Built-in functions
total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
number_of_sales = len(sales)

# Calculate average sales
average_sales = total_sales / number_of_sales

# Math module function
rounded_average = math.ceil(average_sales)

# Calculate profit
profit = total_sales - expenses

# Display formatted financial report
print("===== BUSINESS FINANCIAL REPORT =====")
print(f"Total Sales: ₦{total_sales:,}")
print(f"Total Expenses: ₦{expenses:,}")
print(f"Business Profit: ₦{profit:,}")
print(f"Highest Sale: ₦{highest_sale:,}")
print(f"Lowest Sale: ₦{lowest_sale:,}")
print(f"Average Sales: ₦{average_sales:,.2f}")
print(f"Rounded Average Sales: ₦{rounded_average:,}")
print(f"Number of Sales: {number_of_sales}")
print("====================================")

