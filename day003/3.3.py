#Nested if else statements
#Checking if height is over 120 cm and if yes we check the age 
# to see if they get adult or child price

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age >= 18:
        print("You pay adult price.")
    elif age >= 12:
        print("You pay teen price.")
    else:
        print("You pay child price.")

else:
    print("Sorry, you have to grow taller before you can ride.")
