#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt", mode="r") as n:
    names = [name.replace("\n", "") for name in n.readlines()]

with open("./Input/Letters/starting_letter.txt", mode="r") as l:
    letter = l.read()

for name in names:
    new_letter = letter.replace("[name]", name)
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as nl:
        nl.write(new_letter)



