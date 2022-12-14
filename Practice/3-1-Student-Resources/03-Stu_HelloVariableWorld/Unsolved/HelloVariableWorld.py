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
    # The varibale is hourly_wage
    # Inside the variable 'hourly_wage' is an integer: 20
hourly_wage = 20


# Calculate the daily wage for the user
    # Create a variable that contains the formula to calcualte the daily wage
    # The new variable is daily_wage
        # Inside this variable is a formula 
            # We take the previous variable of 'hourly_wage' and multiply it by 8; the number of hours worked in a day
            # When printed this will return an integer for daily_wage; in this case 160
daily_wage = hourly_wage * 8
print(daily_wage)

# Create a variable called 'satisfied' that holds a boolean
    # The variable is 'satisfied'
    # A boolean is a true or false statement 
        # In this example it is true
satisfied = True

# Print out "Hello <name>!"
    # "Hello" is a string that we want printed out
    # <name> is the variable
    # "!" is also part of the string 

        # Effectively you are building a formula to print a desired statement
        # Make sure you leave a space after Hello and " otherwise Hello and the name will together
print("Hello " + name + "!")

# Print out what country the user entered
    # "Yoou live in the " is the string
    # country is the variable from earlier 
print("You live in the " + country)

# Print out the user's age
    # str(age) is converting age; which is an integer; into a string so that it can print out normally
        # Without converting, you will get an erorr when attempting to print
print("You are " + str(age) + " years old")

# Use an f-string instead, to prevent using the 'str()' method every time
    # This is the refactored code using the f-string
# print(f"You are {age} years old")

# With an f-string, print out the daily wage that was calculated
# An f-string is preferred because it does not need conversion 
    # So this line of code will work even though daily_wage is an integer type
print(f"You make {daily_wage} per day")

# With an f-string, print out whether the users were satisfied
# Once again the f-string is being used to convert the boolean 'satisfied' into a string
print(f"Are you satisfied with your current wage? {satisfied}") 
