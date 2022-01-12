import tkinter

window = tkinter.Tk()

window.title("Mile to Km Converter")
# window.minsize(width=350, height=100)
window.config(padx=10, pady=10)


def convert():
    miles = distance.get()
    km = round(float(miles) * 1.609344, 2)
    km_value.config(text=str(km))

# Labels
miles_label = tkinter.Label(text="Miles", font=("Arial", 10))
miles_label.grid(row=0, column=2)

is_equal = tkinter.Label(text="is equal to", font=("Arial", 10))
is_equal.grid(row=1, column=0)

km_value = tkinter.Label(text="0", font=("Arial", 10))
km_value.grid(row=1, column=1)

km_label = tkinter.Label(text="Km", font=("Arial", 10))
km_label.grid(row=1, column=2)

# Distance input
distance = tkinter.Entry(width=15)
distance.grid(row=0, column=1)

# Button
button = tkinter.Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()