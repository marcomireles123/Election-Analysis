# @TODO: Your code here
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

