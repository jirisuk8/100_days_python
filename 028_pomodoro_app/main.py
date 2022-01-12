from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 #25
SHORT_BREAK_MIN = 1 #5
LONG_BREAK_MIN = 1 #20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def stop_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    working_sessions = (1, 3, 5, 7)
    break_sessions = (2, 4, 6)

    if reps in working_sessions:
        countdown(WORK_MIN * 60)
        label_timer.config(text="Work", fg=GREEN)

    elif reps in break_sessions:
        countdown(SHORT_BREAK_MIN * 60)
        label_timer.config(text="Break", fg=PINK)
    else:
        countdown(LONG_BREAK_MIN * 60)
        label_timer.config(text="Break", fg=RED)
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    def min_secs(num):
        if num<10:
            return f'0{num}'
        else:
            return f'{num}'

    count_min = math.floor(count/60)
    count_sec = count%60
    counter = f'{min_secs(count_min)}:{min_secs(count_sec)}'

    canvas.itemconfig(timer_text, text=counter)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks +="✔"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro app")
window.config(padx=100, pady=50, bg=YELLOW)

# Label timer
label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW,font=(FONT_NAME, 30, "bold"))
label_timer.grid(row=0, column=1)

# check label
check_label = Label(fg=GREEN, bg=YELLOW,font=(FONT_NAME, 10, "bold"))
check_label.grid(row=3, column=1)

# tomato picture + timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)


# Buttons
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=stop_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

# Check labels


window.mainloop()