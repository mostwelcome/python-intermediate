from tkinter import *
window = Tk()

window.title('Mile to KM converter')
window.minsize(width=250,height=200)
window.config(padx=20,pady=20)

#Entry
input_text = Entry(width=10)
input_text.grid(column=1,row=0)


miles_label= Label(text='Miles',font=("Arial",16,'bold'))
miles_label.grid(column=2,row=0)


label= Label(text='is equal to',font=("Arial",16,'bold'))
label.grid(column=0,row=1)


#Text
text = Text(height=1, width=10)
#Puts cursor in textbox.
text.grid(column=1,row=1)
text.focus()
#Adds some text to begin with.


km_label= Label(text='Km',font=("Arial",16,'bold'))
km_label.grid(column=2,row=1)

def buttonClick():
    print('I got clicked')
    miles = float(input_text.get())
    km = (miles/0.62137)
    text.insert(END, round(km,2))
    print(round(km,2))

button = Button(text='Calculate',command=buttonClick)
button.grid(column=1,row=2)


window.mainloop()



