
# Splitting and Reassembling Text

# A comma-separated string of African countries
countries = "Nigeria,Ghana,Kenya,Rwanda,South Africa"

# A date in DD/MM/YYYY format
date = "27/11/2026"

# Split the countries into a list
country_list = countries.split(",")

# Split the date into individual components
date_parts = date.split("/")

# Print the original strings
print("Original countries:", countries)
print("Original date:", date)

# Print the individual countries
print("Country list:", country_list)

# Print individual date components using indexes
print("Day:", date_parts[0])
print("Month:", date_parts[1])
print("Year:", date_parts[2])

