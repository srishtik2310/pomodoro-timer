from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    label.config(text ="Timer")
    tick.config(text = "")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_tim = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60

    if reps % 2 == 1 and reps < 8:
        count_down(work_tim)
        label.config(text = "WORK", bg = YELLOW, fg = GREEN)

    if reps % 2 == 0 and reps < 8:
        count_down(short_break)
        label.config(text="Short Break", bg=YELLOW, fg=RED)

    if reps == 8:
        count_down(long_break)
        label.config(text="Long Break", bg=YELLOW, fg=PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
        count_sec = int(count_sec)

    if count_min == 0:
        count_min = "00"
        count_min = int(count_min)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ""
        work_sessions = reps//2
        for i in range(work_sessions):
            mark += "✅ "
            tick.config(text = mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(bg = YELLOW, padx= 50, pady = 50)
window.minsize(400, 400)
canvas = Canvas(width= 200, height= 224, bg = YELLOW, highlightthickness= 0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_image)
timer_text = canvas.create_text(103, 130, text = "00:00", fill = "white", font =(FONT_NAME, 34, "bold"))
canvas.grid(row = 1, column = 1)

label = Label(text = "Timer", bg = YELLOW, font = (FONT_NAME, 22, "bold"), fg = GREEN)
label.grid(row = 0, column = 1)

start_button = Button(text = "Start", bg = "white", highlightthickness= 0, command = start_timer)
start_button.grid(row = 2, column = 0)

stop_button = Button(text = "Reset", bg = "white", highlightthickness= 0, command = reset_timer)
stop_button.grid(row = 2, column = 2)

tick = Label(text = "", bg = YELLOW, fg = GREEN, font =(FONT_NAME, 34, "bold"))
tick.grid(row = 3, column =1)


window.mainloop()