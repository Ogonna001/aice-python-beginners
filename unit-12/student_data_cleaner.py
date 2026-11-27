
# Building a Student Data Cleaner

# Messy student registration data
student_name = "   oGONNA uMEH   "
student_email = "   OGONNA@GMAIL.COM   "
student_phone = "   0803-123-4567   "

# Clean the registration details
clean_name = student_name.strip().title()
clean_email = student_email.strip().lower()
clean_phone = student_phone.strip().replace("-", "").replace(" ", "")

# Validate the email and phone number
email_valid = "@" in clean_email
phone_valid = len(clean_phone) == 11

# Print the cleaned student profile
print("STUDENT PROFILE")
print("--------------------")
print("Name:", clean_name)
print("Email:", clean_email)
print("Phone:", clean_phone)

# Print validation results
print("--------------------")
print("Email valid:", email_valid)
print("Phone valid:", phone_valid)

