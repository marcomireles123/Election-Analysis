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