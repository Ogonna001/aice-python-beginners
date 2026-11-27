
# Cleaning Messy Data

# Two strings with extra spaces and inconsistent capitalisation
country = "   nIGERIA   "
goal = "   learning PYTHON and devops   "

# Clean the strings
clean_country = country.strip().title()
clean_goal = goal.strip().lower()

# Use replace() to correct a word
updated_goal = clean_goal.replace("devops", "software engineering")

# Print original and cleaned values
print("Original country:", country)
print("Cleaned country:", clean_country)

print("Original goal:", goal)
print("Cleaned goal:", clean_goal)

print("Updated goal:", updated_goal)

