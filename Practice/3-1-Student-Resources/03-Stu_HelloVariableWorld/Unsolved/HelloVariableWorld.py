# Create a variable called 'name' that holds a string
name = "Marco"

# Create a variable called 'country' that holds a string
    # Country is the variable
    # The variable 'country' contains a string: 'United States of America'
country = "United States of America"

# Create a variable called 'age' that holds an integer
    # age is the variable
    # Inside the variable 'age' is an integer: 25
        # Integers just hold the number, they do not need ""
age = 25

# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 20

# Calculate the daily wage for the user
daily_wage = hourly_wage * 8

# Create a variable called 'satisfied' that holds a boolean
satisfied = True

# Print out "Hello <name>!"
# "Hello" is a string that we want printed out
# name is the variable
# "!" is also a string 
# Effectively you are building a formula to print a desired statement
# Make sure you leave a space after Hello and " otherwise Hello and the name will together
print("Hello " + name + "!")

# Print out what country the user entered
print("You live in the " + country)

# Print out the user's age
# str(age) is converting age; which is an integer; into a string so that it can print out normally
    # Without converting, you will get an erorr when printing
print("You are " + str(age) + " years old")

# This is the refactored code using the f-string
    # print(f"You are {age} years old")

# With an f-string, print out the daily wage that was calculated
# An f-string is preferred because it does not need conversion 
    # So this line of code will work even though daily_wage is an integer type
print(f"You make {daily_wage} per day")

# With an f-string, print out whether the users were satisfied
# Once again the f-string is being used 
    # Since the variable "satisfied" is a boolean  
        # Would have to be converted if we were not using an f-string
print(f"Are you satisfied with your current wage? {satisfied}") 
