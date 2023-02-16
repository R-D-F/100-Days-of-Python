#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input\Letters\starting_letter.txt") as starting_letter:
    starting_letter = starting_letter.read()
with open("Input/Names/invited_names.txt") as invited_names:
    names_list = invited_names.readlines()

for name in names_list:
    name = name.strip()
    open(f"output/ReadyToSend/{name}_letter.txt", "w")
    letter = open(f"output/ReadyToSend/{name}_letter.txt", "w")
    letter.write(starting_letter.replace("[name]", name))





