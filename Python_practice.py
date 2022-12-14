print("Hello World")

# The type() command will tell you the data type of whatever is inside the parentheses
    # This will print that 3 is an 'int' (integer) class 
type(3)

type(2019)

# When typing #'s greater than 999 DO NOT use a comma 
    # This will turn the object type into a 'Tuple'
    # You will not get one integer in return, you end up with an ordered pair
ballots = 1,341
ballots
type(ballots)

# Floating point decimals
type(73.81)

# Strings
    # Can use single or double quotation marks
    # Cannot be used for mathematical operations
    # Even a number inside the quotation marks will be considered a string NOT an integer or floating point
        # Data types can be converted to the right ones
type('Hello world')

# Empty strings
    # Nothing in between the opening and closing quotation marks
type('')

# Boolean
    # No quotation marks
    # Can only be true or false
type(True)

# Creating variables
    # Declared when followed up by an = sign
    # Variables can contain integers, floating-point decimals, strings, and booleans
    # Variable names must be in snake case (no space between words, instead an _ is used)
    # Cannot use reserved words in Python for variable names
        # Refer to this list with: help("keywords") command
num_candidates = 3
winning_percentage = 73.81
candidate = 'Diane'
won_election = True

# 3.2.4 Skill Drill (1)
5+2*3

# The // divides one number by another and returns an integer
    # AKA floor division
8//5-3

8+22*2-4

16-3/2+7-1

3**3%5

5+9*3/2-4

# 3.2.4 Skill Drill (2)
(5+2)*3
(8//5)-3
8+(22*(2-4))
16-3/(2+7)-1
3**(3%5)

# Finally, compare the following:
5 + (9 * 3 / 2 - 4)

5 + (9 * 3 / (2 - 4))

# 3.2.5 Data structures (lists)

# Ensure you run the list after typing it out
    # Otherwise when trying to print or recall the list, you will get an error that the list was not defined
counties = ['Arapahoe', 'Denver', 'Jefferson']
counties

# 3.2.5 Index Lists
    # Indexing starts at 0. Therefore, the index of the first item is 0, the index of the second number is 1, and so on
    # Because indexing begins at 0, the index of the last item in a list is 1 less than the number of items in the list

# To get the 1st item in a list you will use 0
    # This returns Arapahoe which is the first county in the counties list
    # Alt code: print(counties[2])
counties[0]

# 3.2.5 Find the length of a list
    # Use the len() function and then add the 'list' inside the parantheses 

# Output here will be 3
len(counties)

# 3.2.5 Slice lists
    # Use the list[start : end] function to slice a list
    # 'start' refers to the index of the 1st item slice
    # 'end' is the index marking the end slice 

# This will return everything but not including the index 2 
counties[0:2]
counties[1:3]

# 3.2.5 add items to a list
    # Use the append() function and syntax list.append()

# This has now added El Paso to the existing counties list
counties.append('El Paso')
counties

# Using the syntax list.index(index, obj) we have specified where in the list we want to add the new object 
    # Use this instead of defaulting to the last index in the list
    # insert() is the function
    # list.insert(index, obj) is the syntax
    # list = the list you want to maniupate
    # insert = function
    # index = the position where you want the object at 
    # obj = the string, boolean, integer you want to add 
counties.insert(2, 'El Paso')
counties

# Using .remove() we can remove one instance of the obj in the list
counties.remove('El Paso')
counties

# Use .pop() method to specify which object you want to remove relative to its index position in the list
    # El paso is 4th in the list so its index is 3
counties.pop(3)
counties

# Change an element in a list 
    # You can change items in a list using syntax list[index] = obj
    # obj is what you want to change the current item for

# The object @ index 2 in the list counties will be changed to El Paso
    # Jefferson was changed to El Paso
counties[2] = 'El Paso'
counties

# 3.2.7 Dictionaries

# Create an empty dictionary using my_dict = {} syntax
counties_dict = {}
counties_dict

# Add the counties and their voters to the dictionary
    # The county is the key and the voter count is the value (key: value pair)
counties_dict['Arapahoe']=422829
counties_dict['Denver']=463353
counties_dict['Jefferson']=432438
counties_dict

# Get the length of a dictionary using len() function
len(counties_dict)

# Print all key, value pairs using .items() function
    # Tuples will be the output, 1st element is the key and 2nd element is the value
counties_dict.items()

# Get only the keys using .keys() function 
counties_dict.keys()

# Get only the values using .values() function
counties_dict.values()

# Get a specific value using .get()
    # Where inside the parentheses you can put a key and output its value
counties_dict.get('Denver')
    # Alt code
    # counties_dict['Denver']

# List of dictionaries

# Make an empty list 
voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data

# Add the new county ???El Paso??? and its registered voters, 461149, to the second position in voting_data
voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})

# Remove ???Arapahoe??? and its registered voters from voting_data
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})

# Make ???Denver??? and its registered voters the third item in voting_data, but keep ???Jefferson??? and its registered voters as the second item
voting_data.remove({'county': 'Jefferson', 'registered_voters': 432438})
voting_data.insert(1, {'county': 'Jefferson', 'registered_voters': 432438})

# Add ???Arapahoe??? and its registered voters to voting_data
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data

# 3.2.8 Decision Statements

# Practice using the if statement on our counties list to determine if the second county in the list is Denver. 
    # If so, then we will print "Denver" to the screen
counties = ["Arapahoe","Denver","Jefferson"]
    # == is the sign for 'equal to'
if counties[1] == 'Denver':
    print(counties[1])

# if-else statements
temperature = int(input("What is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

# Nested if-else statements
#What is the score?
score = int(input("What is your test score? "))
# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

# Alt code for if-else statements
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

# 3.2.9 Membership and Logical Operators

# Membership Operators
counties = ["Arapahoe","Denver","Jefferson"]
    # The operator 'in' states that we are trying to determine if El Paso is in the list of counties
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# Logical Operators
    # Operators are 'and', 'or', 'not'
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# Here we changed the operator to 'or' instead of 'and'
    # Now the statement will only check if one or the other county is included
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

# 3.2.10 Repition Statements

# While loops
    # Once x is greater than 5 the loop stops
x = 0
while x <= 5:
    print(x)
    # We increment the value of x by 1 using this operation
    x = x+1

# Hello world will not be printed in this loop because count is 7 
    # 7 is not less than 1
count = 7
while count  < 1:
    print("Hello World")

# For loops
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

# Much simpler version of the code preceeding it
    # Instead of a for loop we use the range() method
    # Eliminates having to create a list and declaring it
for num in range(5):
    print(num)

# Variable i is used to indicate the values 0, 1, and 2
# Inside the range function we get the length of the list in counties which is the integer 3
# We iterate through the list where the variable i = 0 where 'Arapahoe' is printed and so on until all the strings in counties are printed 
for i in range(len(counties)):
    print(counties[i])

# Iterate Through a Dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# Get the Keys of a Dictionary
for county in counties_dict:
    print(county)

# Use the keys() method
for county in counties_dict.keys():
    print(county)

# Get the Values of a Dictionary

# Use the values() method
for voters in counties_dict.values():
    print(voters)

# Use the get() method
for county in counties_dict:
    print(counties_dict.get(county))

# Get the Key-Value Pairs of a Dictionary

# Use the items() method
for county, voters in counties_dict.items():
    print(county, voters)

# Get Each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)