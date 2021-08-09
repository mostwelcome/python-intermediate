# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open('./Input/Names/invited_names.txt') as invited:
    invited_list = invited.readlines()

with open('./Input/Letters/starting_letter.txt') as mail:
    lines = mail.readlines()

for guest in invited_list:
    file_name = 'letter_for_' + guest
    with open('./Output/ReadyToSend/' + file_name.strip(), mode='w') as final_letter:
        first_line = lines[0].replace('[name]', guest.strip())
        final_letter.write(first_line)
        for line in lines[1:]:
            final_letter.write(line)
