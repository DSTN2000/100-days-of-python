from tkinter import *
import itertools
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

FONT_TIME = (FONT_NAME, 32, 'bold')
FONT_TIMER = (FONT_NAME, 48, 'italic')
FONT_CHECKMARK = (FONT_NAME, 24, 'bold italic')
FONT_BUTTONS = (FONT_NAME, 8, 'bold')

rep_id = 0
rep_duration_sec = [[WORK_MIN, SHORT_BREAK_MIN][i %
                                                2]*60 for i in range(7)] + [LONG_BREAK_MIN*60]
checkmarks_count=0
timer = None
timer_can_start = True

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global rep_id, checkmarks_count, timer_can_start
    rep_id = 0
    checkmarks_count = 0
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    checkmark_label.config(text='')
    canvas.itemconfig(canvas_text,text='0:00')
    timer_can_start=True

# ---------------------------- TIMER MECHANISM ------------------------------- #
def initiate_timer():
    global timer_can_start
    if timer_can_start:
        timer_can_start=False
        start_timer()
    else:
        return

def start_timer():
    global rep_id, rep_duration_sec, timer_label, checkmarks_count, timer_can_start
    if rep_id % 2:
        if rep_id == 7:
            timer_label.config(text='Long break', fg=RED)
        else:
            timer_label.config(text='Break', fg=PINK)
        checkmarks_count+=1
        checkmark_label.config(text=f'{'✓'*checkmarks_count}')
    else:
        timer_label.config(text='Work', fg=GREEN)
    countdown(rep_duration_sec[rep_id])
    rep_id += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(seconds):
    display_min = seconds//60
    display_sec = seconds % 60
    if display_sec < 10:
        display_sec = f'0{display_sec}'
    canvas.itemconfig(canvas_text, text=f'{display_min}:{display_sec}')
    if seconds > 0:
        global timer
        timer = window.after(1000, countdown, seconds-1)
    elif seconds == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='28/tomato.png')
canvas.create_image(100, 112, image=tomato_image)
canvas_text = canvas.create_text(
    100, 130, text='0:00', font=FONT_TIME, fill='white')
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', font=FONT_TIMER, fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

checkmark_label = Label(text='', font=FONT_CHECKMARK, fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

reset_button = Button(text='Reset', font=FONT_BUTTONS, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

start_button = Button(text='Start', font=FONT_BUTTONS,
                      highlightthickness=0, command=initiate_timer)
start_button.grid(column=0, row=2)


window.mainloop()
