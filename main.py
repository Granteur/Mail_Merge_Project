REPLACE = "[name]"
#TODO: Create a letter using starting_letter.txt 
#opens invited_names file, and stores the listed names in a variable called 'names'
with open("./Input/Names/invited_names.txt") as names_list:
    names = names_list.readlines()

#opens a sample letter that has a placeholder string, & stores as a string inside letter_template variable
with open("./Input/Letters/starting_letter.txt") as sample_letter:
    letter_template = sample_letter.read()
    #for each name in invited_names.txt
    #Replace the [name] placeholder with the actual name.
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_template.replace(REPLACE, stripped_name)
        #Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as finished_letter:
            finished_letter.write(new_letter)
    
