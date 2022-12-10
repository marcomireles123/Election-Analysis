# @TODO: Your code here
# Create a dictionary that has key-value pairs 
    # Add a list
    # Add a dictionary within the dictionary
my_pet = {
    "name": "Lucky",
    "age": 10,
    "hobbies": ["running", "barking", "sleeping"],
    "wake_up": {"Monday": "7 am", "Tuesday": "8 am", "Wednesday": "9 am"
    }
}

# We use an f-string to convert any object into a string
    # Refer to the dictionary and then the individual key-value pair you would like to print
print(f'Hello my name is {my_pet["name"]} and I am {my_pet["age"]}.') 

# Again using f-string so we do not have to convnert manually 
    # Use len function to retrieve a number for the hobbies list
print(f'I have {len(my_pet["hobbies"])} hobbies!') 

# We use index numbering to retrieve a specific object in the hobbiest list
    # In this case I am printing the second object "barking" which is index #1 
print(f'My favorite hobbie is {my_pet["hobbies"][1]}.') 

# Here to call a key-value pair of a dictionary within a dictionary you simply have to print the dictionary and then its key pair variable inside the dictionary
print(f'I wake up at {my_pet["wake_up"]["Wednesday"]}.')
