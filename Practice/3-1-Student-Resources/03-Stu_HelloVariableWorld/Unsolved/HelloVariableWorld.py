# Create a variable called 'name' that holds a string
name = "Marco"

# Create a variable called 'country' that holds a string
country = "United States of America"

# Create a variable called 'age' that holds an integer
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
print("You are " +str(age) + " years old")

# With an f-string, print out the daily wage that was calculated
print(f"You make {daily_wage} per day")

# With an f-string, print out whether the users were satisfied
print(f"Are you satisfied with your current wage? {satisfied}") 
