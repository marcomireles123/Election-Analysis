x = 1
y = 10

# Checks if one value is equal to another
    # This conditional says 'if x is equal to 1':
    # x is EQUAL to 1
        # print 'x is equal to 1'
if x == 1:
    print("x is equal to 1")

# Checks if one value is NOT equal to another
    # This conditional says 'if y NOT equal to 1':
    # y is NOT equal to 1
        # print 'y is not equal to 1'
if y != 1:
    print("y is not equal to 1")

# Checks if one value is less than another
    # This conditional says: 'If x is less than y':
    # x is LESS than y in this case
        # print 'x is less than y'
if x < y:
    print("x is less than y")

# Checks if one value is greater than another
    # This conditional says 'if y is greater than x':
    # y = 10, x = 1: y is GREATER than x in this case
        # print 'y is greater than x'
if y > x:
    print("y is greater than x")

# Checks if a value is less than or equal to another
    # This conditional says if x is greather than OR equal to 1:
        # print 'x is greater than or equal to 1'
if x >= 1:
    print("x is greater than or equal to 1")

# Checks for two conditions to be met using "and"
    # In this case x DOES equal 1 and y DOES equal 10
        # So the return print will be 'both values returned true' 
if x == 1 and y == 10:
    print("Both values returned true")

# Checks if either of two conditions is met
    # Here we are using the 'or' conditional
    # In this case x IS less than 45
        # But y is NOT less than 5
            # Either way it will still print since at least one of the conditionals was met
if x < 45 or y < 5:
    print("One or more of the statements were true")

# Nested if statements
    # In this case x IS less than 10 
if x < 10:
    
    # y is NOT less than 5
    if y < 5:
        print("x is less than 10 and y is less than 5")
    
    # y does NOT equal to 5
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    
    # This is what will print, because it meets both conditionals 
    else:
        print("x is less than 10 and y is greater than 5")
