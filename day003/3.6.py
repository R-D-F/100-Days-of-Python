#Nested if else statements
#Checking if height is over 120 cm and if yes we check the age 
# to see if they get adult or child price
### my solution
""" print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

adultPrice = 12
teenPrice = 7
childPrice = 5
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
age = int(input("What is your age? "))
if age >= 18:
    photo = input("Do you want a photo y/n ")
    if photo == "y" or "Y" or "Yes":
        print(f"Your price is {adultPrice + 3}$ ")
    else: 
        print(f"Your price is {adultPrice}$")
elif age >= 12:
    photo = input("Do you want a photo y/n ")
    if photo == "y" or "Y" or "Yes":
        print(f"Your price is {teenPrice + 3}$ ")
    else: 
        print(f"Your price is {teenPrice}$")
else:
    photo = input("Do you want a photo y/n ")
    if photo == "y" or "Y" or "Yes":
        print(f"Your price is {childPrice + 3}$ ")
    else: 
        print(f"Your price is {childPrice}$") """
###


#Professor solution
bill = 0
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age >= 18:
        bill = 12
        print(f"Your price is ${bill}")
    elif age >= 12:
        bill = 7
        print(f"Your price is ${bill}")
    else: 
        bill = 5
        print(f"Your price is ${bill}")
    photo = print (input("Do you want a photo y/n?"))
    if photo == "y" or "Y" or "Yes" or "yes":
        bill += 3
        print (f"Your final bill is ${bill}")
    else: 
        print(f"Your bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
