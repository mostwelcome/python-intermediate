from tkinter import *
import json
import random
from tkinter import messagebox

import pyperclip


# ---------------------------- Search Password ------------------------------- #

def search_password():
    try:
        website = website_entry.get()
        if not website:
            messagebox.showinfo(message='Please give website details')
        else:
            with open('data.json', 'r') as data_file:
                data_found = json.load(data_file)
                password_details = data_found[website]
                messagebox.showinfo(title=website,
                                    message=f" Email : {password_details.get('email')} \n Password: {password_details.get('password')}")
    except FileNotFoundError:
        messagebox.showinfo(message='Oops !! No Previous data found')
    except KeyError:
        messagebox.showinfo(message='No previous data saved for this website')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    if len(password_entry.get()) != 0:
        password_entry.delete(0, END)
    # Password Generator
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []

    # for letter in range(1, nr_letters+1):
    #     password_list.append(random.choice(letters))
    print(nr_letters)
    password_list = [random.choice(letters)
                     for letter in range(1, nr_letters + 1)]
    password_list_numbers = [random.choice(
        numbers) for number in range(1, nr_numbers + 1)]
    password_list_symbols = [random.choice(
        symbols) for symbol in range(1, nr_symbols + 1)]

    password_list.extend(password_list_symbols)
    password_list.extend(password_list_numbers)
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    # copy the password to clip board as we don't need to copy paste manually
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        'email': email,
        'password': password
    }}
    if len(website) == 0 or email == 0 or password == 0:
        messagebox.showinfo(
            message='Oops !! Please make sure none of the field is empty')
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the details entered :\nEmail : {email}\nPassword :{password}\nIs it okay to save?\n')

        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    # Read the old data
                    data = json.load(data_file)
            except:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Update the old data with new data
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                # clearing entries
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# x = [i**2 if i%2 ==0 else i for i in range(1,10)]
# print(x)

# value = 123
# print(value, 'is', 'even' if value % 2 == 0 else 'odd')


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)

canvas.grid(row=0, column=1)

# labels
website_label = Label(text='Website')
website_label.grid(row=1, column=0)
email_label = Label(text='Email')
email_label.grid(row=2, column=0)
password_label = Label(text='Password')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
# default email
email_entry.insert(0, 'abc@gmail.com')
password_entry = Entry(width=40)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
generate_password_button = Button(
    text='Generate Password', command=generate_password)
generate_password_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text='Search Password', command=search_password)
search_button.grid(row=5, column=1, columnspan=2)
save_button = Button(text='Save Password', width=30, command=save)
save_button.grid(row=6, column=1, columnspan=2)
window.mainloop()
