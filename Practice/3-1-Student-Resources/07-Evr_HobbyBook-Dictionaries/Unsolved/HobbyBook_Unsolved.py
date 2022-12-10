# @TODO: Your code here
# Create a dictionary that has key-value pairs 
    # Add a list
    # Add a dictionary within the dictionary
my_pet = {
    "name": "Lucky",
    "age": 10,
    
    # A list
    "hobbies": ["running", "barking", "sleeping"],
    
    # A dictionary
        # That contains key-value pairs
    "wake_up": {"Monday": "7 am", "Tuesday": "8 am", "Wednesday": "9 am"
    }
}

# We use an f-string to convert any object into a string
    # Refer to the dictionary and then the individual key-value pair you would like to print    
        # This looks likek {my_pet['name']}
            # my_pet is the dictionary that we createad
            # 'name' is the key-value pair inside the dictionary 
print(f'Hello my name is {my_pet["name"]} and I am {my_pet["age"]}.') 

# Again using f-string so we do not have to convnert manually 
    # Use the len() function to retrieve how many object are in the the hobbies list
        # This looks like {len(my_pet['hobbies'])}
            # my_pet is the dict.
            # 'hobbies' is the list inside the dict.
            # This will print out the number 3 since there are only 3 objects in this list
print(f'I have {len(my_pet["hobbies"])} hobbies!') 

# We use index numbering to retrieve a specific object in the hobbiest list
    # In this case I am printing the second object "barking" which is index no. 1 
        # my_pet is the dict.
        # 'hobbies' is the list 
        # [1] is the index no. of the object I want to retrieve
print(f'My favorite hobbie is {my_pet["hobbies"][1]}.') 

# Here to call a key-value pair of a dictionary within a dictionary you simply have to print the dictionary and then its key variable inside that dictionary
    # my_pet is the dict.
    # 'wake_up' is the dict. inside my_pet
    # 'Wednesday' is the key variable to the key-pair value I want to print
print(f'I wake up at {my_pet["wake_up"]["Wednesday"]}.')
