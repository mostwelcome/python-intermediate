from tkinter import *

window = Tk()

window.title('First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label


my_label = Label(text='I am a label', font=("Arial", 24, 'bold'))
my_label.grid(column=0, row=0)

my_label['text'] = "new text"


# Button

def buttonClick():
    print('I got clicked')
    print(input_text)
    my_label['text'] = input_text.get()


button = Button(text='click me', command=buttonClick)
button.grid(column=1, row=1)

button2 = Button(text='New Button', command=buttonClick)
button2.grid(column=2, row=0)

# Entry
input_text = Entry(width=10)
input_text.grid(column=3, row=3)

print(input_text.get())
window.mainloop()
