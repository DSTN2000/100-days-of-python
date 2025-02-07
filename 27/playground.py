import tkinter
import itertools

WIDTH = 1920
HEIGHT = 1080
FONT = ('Arial', 24, 'normal')

window = tkinter.Tk()
window.title('Tkinter')
window.minsize(width=WIDTH, height=HEIGHT)
window.state('zoomed')

label = tkinter.Label(text='Hello, World!', font=FONT)
label.grid(column=0, row=0)


id = itertools.count()
def click_button():

    click_id = next(id)
    label.config(text=f'I got clicked {click_id+1} times!'\
                 f' And you entered {input.get()}')

button = tkinter.Button(text='Click Me!', command=click_button)
button.grid(column = 1, row=1)

input = tkinter.Entry()
input.grid(column=3,row=3)

new_button = tkinter.Button(text='Click Me Too!', command=lambda : print('You clicked a new button'))
new_button.grid(column=2,row=0)


window.mainloop()
