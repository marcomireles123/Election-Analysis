# Loop through a range of numbers (0 through 4)
    # This will print out 0-4 
        # Index starts with 0
    # With index numbering there are 5 numbers
for x in range(5):
    print(x)

# This is simply for organizing the prints 
    # Otherwise there would be no spacing between them and all the numbers would be close together 
        # Makes the final output harder to read without this line 
print("-----------------------------------------")

# Loop through a range of numbers (2 through 6 - yes 6! Up to, but not including, 7)
    # This will only print 2-6 and not 7
for x in range(2, 7):
    print(x)

print("----------------------------------------")

# Iterate through letters in a string
    # This will print out the individual letters in "Peace" 
word = "Peace"
for letters in word:
    print(letters)

print("----------------------------------------")

# Iterate through a list
    # This will print out the individual string objects from the list and assign it to a new variable 'animal' at the same time
zoo = ["cow", "dog", "bee", "zebra"]
for animal in zoo:
    print(animal)

print("----------------------------------------")

# Loop while a condition is being met
run = "y"

while run == "y":
    print("Hi!")

    # the input will appear in the ' ' quotations
    run = input("To run again. Enter 'y'")

