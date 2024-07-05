import math
from tkinter import *
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None
mark = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=PINK, font=(FONT_NAME, 30, "bold"), bg=YELLOW)

    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED, font=(FONT_NAME, 30, "bold"), bg=YELLOW)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minute = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    if count == 0:
        start_timer()

    if minute and seconds == 0:
        winsound.Beep(1, 5)

    global mark
    mark = ""
    work_sessions = math.floor(reps / 2)
    for _ in range(work_sessions):
        mark += "✔"
    checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image=tomato)
timer_text = canvas.create_text(100, 135, text="00:00", font=("Arial", 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

start = Button(text="Start", bg=YELLOW, font=(FONT_NAME, 10, "bold"), command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg=YELLOW, font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset.grid(column=2, row=2)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=2)

window.mainloop()
