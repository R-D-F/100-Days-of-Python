# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
heightFloat = float(height)
weightFloat = float(weight)
bmiFloat = (weightFloat / (heightFloat**2))
bmiInt = int(bmiFloat)
bmiFloatRounded = round(bmiFloat)
if bmiFloatRounded < 18.5:
    print(f"Your BMI is {bmiFloatRounded}, you are underweight.")
elif bmiFloatRounded < 25:
    print(f"Your BMI is {bmiFloatRounded}, you have a normal weight.")
elif bmiFloatRounded < 30:
    print(f"Your BMI is {bmiFloatRounded}, you are slightly overweight.")
elif bmiFloatRounded < 35: 
    print(f"Your BMI is {bmiFloatRounded}, you are obese.")
else:
    print(f"Your BMI is {bmiFloatRounded}, you are clinically obese.")
