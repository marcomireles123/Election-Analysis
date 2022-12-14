# Create a Python list to store your grocery list
# Lists are created using []
    # The list is named 'grocery_list' 
        # This list contains 5 string objects 
        # As an index it would appear as 0-4
grocery_list = ["Milk", "Bread", "Eggs", "Peanut Butter", "Jelly"]

# Print the grocery list
    # Use the print function
print(grocery_list)

# Change "Peanut Butter" to "Almond Butter" and print out the updated list
    # Index does not start with 1 it starts with 0 
        # Peanut Butter is the 4 object so it is no. 3 in the index 
grocery_list[3] = "Almond Butter"
print(grocery_list)

# Remove "Jelly" from grocery list and print out the updated list
    # Use the .remove() function followed by the object string you want removed
grocery_list.remove("Jelly")
print(grocery_list)

# Add "Coffee" to grocery list and print the updated list
    # Use the .append() function followed by the new object string you want to add
    # By default it will add these objects to the end of the list
grocery_list.append("Coffee")
print(grocery_list)

# Use the .index() function followed by a specific object inside the index 
    # Returns the index number in the list for that object
    # Milk is 0 since it is the first object in the list
print(grocery_list.index("Milk"))

    # Coffee is 4 since in this list of 5 objects, it is the last object in the index
print(grocery_list.index("Coffee"))

# len() returns the length of a list
    # There are 5 objects in this list so it prints out that there are 5 objects
print(len(grocery_list))