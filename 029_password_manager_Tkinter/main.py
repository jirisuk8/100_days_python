from tkinter import *

FONT = ("Arial", 8, "bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

# logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# labels
label1 = Label(text="Website:")
label1.grid(row=1, column=0)

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)

label3 = Label(text="Password:")
label3.grid(row=3, column=0)

# entries
website = Entry(width=35)
website.grid(row=1, column=1, columnspan=2, sticky="EW")

username = Entry(width=35)
username.grid(row=2, column=1, columnspan=2, sticky="EW")

password = Entry()
password.grid(row=3, column=1, sticky="EW")

# buttons
gen_password = Button(text="Generate password")
gen_password.grid(row=3, column=2, sticky="EW")

add_password = Button(text="Add", width=35)
add_password.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()


