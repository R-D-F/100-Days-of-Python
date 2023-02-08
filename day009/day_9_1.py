### dictionarys and nesting
### final project is to build a secret auction program
### dictionaries in python: they allow us to group together and tag related pieces of information
### key value pairs
### very similar to a table
### {key: value} this is the syntax for a dictionary
### if you wanted to assign values to the key and the values:
### {"Bug": "An error in a program that prevents the program from running as expected"}

### to have more than one entry we separate key:value pairs with commas

###{"Bug": "An error in a program that prevents the program from running as expected", "Function": "A piece of code that you can easily call over and over again.", "Loop": "The action of doing somehthing over and over again"}

### propper dictionary formatting:
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again.",
    
}
### what if you want to retreive an item from a dictionary

print(programming_dictionary["Bug"])

### be sure to spell the key correctly, capitalization needs to be correct, make sure to provid the key in the actual data type

### what about adding data?

programming_dictionary["Loop"] = "The action of doing somehting over and over again."

print(programming_dictionary)

### create an empty dictionary
empty_dictionary = {}
### add to empty_dictionary
#empty_dictionary[]
### wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

### edit an item in a dictionary, same syntax for adding new items
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

### Loop through a dictionary
### just gives keys:
for key in programming_dictionary:
    print(key)
    ### to print values:
    print(programming_dictionary[key])
