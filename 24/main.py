#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('24/Input/Letters/starting_letter.txt') as starting_letter:
    contents = starting_letter.read()
    with open('24/Input/Names/invited_names.txt') as invited_names:
        for name in invited_names:
            new_letter_contents = contents.replace('[name]', name.strip())
            new_letter_name = f'letter_for_{name.strip()}.docx'
            open(f'24/Output/ReadyToSend/{new_letter_name}', 'w').write(new_letter_contents)
            print(new_letter_contents)

    #print(contents)