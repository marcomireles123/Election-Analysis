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
