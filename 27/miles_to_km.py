import tkinter
import itertools

WIDTH = 500
HEIGHT = 300
FONT = ('Arial', 12, 'normal')

window = tkinter.Tk()
window.title('Miles to km')
window.minsize(width=WIDTH, height=HEIGHT)

miles_label = tkinter.Label(text='Miles', font=FONT)
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text='Km', font=FONT)
km_label.grid(column=2, row=1)

is_equal_to_label = tkinter.Label(text='is equal to', font=FONT)
is_equal_to_label.grid(column=0, row=1)

value_label = tkinter.Label(text='0', font=FONT)
value_label.grid(column=1, row=1)

button = tkinter.Button(text='Calculate', command=lambda: value_label.config(
    text=str(float(input.get())*1.6)), font=FONT)
button.grid(column=1, row=2)

input = tkinter.Entry()
input.grid(column=1, row=0)



window.mainloop()
