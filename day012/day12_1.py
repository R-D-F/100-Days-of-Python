################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

### Local scope
### exists within functions

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# ### When you create a variable inside a function you can only use it inside that function
# ### it has "Local Scope"

# drink_potion()
# print(potion_strength)

### If we want it accessable outside the function we need to make it have "Global Scope"
### the only difference between local and global is where you define the variable

# player_health = 10

# def drink_potion():
#     potion_strenght = 2 
#     print(player_health)

# drink_potion

### This concept of local and global scope does not just apply to variables, it applies to everything you name. like functions, dictionaries etc. This is called the "Namespace". Namespace is only valid in certain scopes
### Does python have block scope? NO
### This means that 
# if 3 > 2:
#     a_variable = 10
### does not count as a fence. a_variable is still global scope

### How to modify a variable with global scope
# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function {enemies}")
# ### here we are creating an entirely new variable that is sepperate from the global one

# increase_enemies()
# print(f"enemies outside function: {enemies}")

### the way to do what we are trying to do above is to do this
# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 2
#     print(f"enemies inside function {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

### there is a reason that they make it kinda hard to do. Because it is generally a bad idea because it is confusing and prone to creating bugs and errors. Best practice is to avoid modifying global scope. The way to get around this is to use return statements instead.

# enemies = 1

# def increase_enemies():
#     '''increase value of enemy by 1'''
#     print(f"enemies inside function {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

### Global Constants
### variables which you define and which you are never planning on changing
### The naming convention in python for constants is to turn name them in ALL CAPS
