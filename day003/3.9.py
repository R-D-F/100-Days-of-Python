# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
### My solution 
'''
loveOMeter = 0 
name1Lower = str.lower(name1)
name2Lower =  str.lower(name2)

trueCount = name1Lower.count('t') + name2Lower.count('t') + name1Lower.count('r') + name2Lower.count('r') + name1Lower.count('u') + name2Lower.count('u') + name1Lower.count('e') + name2Lower.count('e')
loveCount = name1Lower.count('l') + name2Lower.count('l') + name1Lower.count('o') + name2Lower.count('o') + name1Lower.count('v') + name2Lower.count('v') + name1Lower.count('e') + name2Lower.count('e')

strTrueCount = str(trueCount)
strLoveCount = str(loveCount) 
strLoveOMeter = strTrueCount + strLoveCount
loveOMeter = int(strLoveOMeter)      

if loveOMeter < 10 or loveOMeter > 90:
    print(f"Your score is {loveOMeter}, you go together like coke and mentos.") 
elif loveOMeter >= 40 and loveOMeter <= 50:
    print(f"Your score is {loveOMeter} you are alright together.")
else:
    print(f"Your score is {loveOMeter}.")
'''
### Prof solution
combinedString = name1 + name2
lowerCombinedString = combinedString.lower()
t = lowerCombinedString.count("t")
r = lowerCombinedString.count("r")
u = lowerCombinedString.count("u")
e = lowerCombinedString.count("e")

true = t + r + u + e

l = lowerCombinedString.count("l")
o = lowerCombinedString.count("o")
v = lowerCombinedString.count("v")
e = lowerCombinedString.count("e")

love = l + o + v + e
 
loveScore = int(str(true) + str(love))


if loveScore < 10 or love > 90:
    print(f"Your love score is {loveScore}, you go together like coke and mentoes.")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alrigt together.")
else:
    print(f"Your love score is {loveScore}.")

