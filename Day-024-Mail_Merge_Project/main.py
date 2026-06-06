PLACEHOLDER = "[name]" #Good habit

with open("./Input/Letters/starting_letter.txt", "r") as file:
    template = file.read()

with open("./Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()

for name in names:
    clean_name = name.strip()  # Remove the white space \n, do this first before creating file.
    new_letter = template.replace(PLACEHOLDER, clean_name)
    with open(f"./Output/ReadyToSend/Letter_for_{clean_name}.txt", mode="w") as completed_letter: #Create a new txt for each name.
        completed_letter.write(new_letter)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
