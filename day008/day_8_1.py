### Functions that allow them to give you input

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# your_name = input("type your name")
# my_name = input("type my name")

# def greet(a,b):
#     print(f"Hello {a}")
#     print(f"My name is {b}")
#     print("Eat my shorts, cowabunga dude")
# greet(your_name, my_name)

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name("Angela")

### there are two things that we are working with here, when we call a function and we pass over the peice of data we have given it, we are effectivly creating a new variable called "something", in this case, (it is just the name of the parameter we give to the funciton) and we are setting it to equal this piece of data, "123" in this case which is called the "argument".  

# def my_function(something):
#     #do this with something
#     #Then do this 
#     #Finaly do this

# my_function(123)

#"something" is the Parameter
#"123" is the Argument