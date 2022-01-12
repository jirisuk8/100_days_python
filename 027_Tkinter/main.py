import tkinter

window = tkinter.Tk()

window.title("First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    text = "I got clicked"
    # my_label['text'] = inpt.get()
    my_label.config(text=inpt.get())
    print(text)
    return text


# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)
# my_label['text'] = "New text"
my_label.config(text="New text", padx=80, pady=80)

# Button
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="New button", command=button_clicked)
button2.grid(column=2, row=0)
# Entry
inpt = tkinter.Entry(width=10)
inpt.grid(column=3, row=3)

window.mainloop()