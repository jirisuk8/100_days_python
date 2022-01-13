from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Arial", 8, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.extend([random.choice(letters) for _ in range(nr_letters)])
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)

    pass_word = "".join(password_list)

    password.delete(0, END)
    password.insert(END, pass_word)
    pyperclip.copy(pass_word)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website.get()
    name = username.get()
    pwd = password.get()
    new_data = {
        web: {
            "email": name,
            "password": pwd
        }
    }

    # Input check
    if len(web) < 1 or len(name) < 1 or len(pwd) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)

# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search_password():
    web = website.get()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="There are no records in the database")
    else:
        if web in data:
            user = data[web]["email"]
            pwd = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {user}\nPassword: {pwd}")
        else:
            messagebox.showinfo(title="Oops", message="No password found for desired website")


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
website.grid(row=1, column=1, sticky="EW")
website.focus()

username = Entry(width=35)
username.insert(END, "jirka@email.com")
username.grid(row=2, column=1, columnspan=2, sticky="EW")

password = Entry()
password.grid(row=3, column=1, sticky="EW")

# buttons
gen_password = Button(text="Generate password", command=create_pwd)
gen_password.grid(row=3, column=2, sticky="EW")

gen_password = Button(text="Search", command=search_password)
gen_password.grid(row=1, column=2, sticky="EW")

add_password = Button(text="Add", width=35, command=save)
add_password.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
