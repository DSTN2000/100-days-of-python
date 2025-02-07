from tkinter import *
import pandas as pd
import random
import shutil

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Arial', 40, 'italic')
LANGUAGE_POS = {'x':400,'y':150}
WORD_FONT = ('Arial', 60, 'bold')
WORD_POS = {'x':400,'y':263}
CARD_HEIGHT = 526
CARD_WIDTH = 800

# ---------------------------- GETTING DATA ------------------------------- #
def get_data():
    try:
        pd.read_csv('31/data/words_to_learn.csv')
    except FileNotFoundError:
        shutil.copy('31/data/french_words.csv', '31/data/words_to_learn.csv')
    data = pd.read_csv('31/data/words_to_learn.csv')
    data = data.to_dict(orient='records')
    return data
card_data = None
flip = None
# ---------------------------- GENERATING CARD SIDES ------------------------------- #
def new_word(previous_word_is_familiar=True):
    global card_data, flip
    if flip:
        window.after_cancel(flip)
    data = get_data()
    if card_data and previous_word_is_familiar:
        for dict_ in data:
            if dict_['French'] == card_data['front']['word']:
                data.remove(dict_)
                print(len(data))
                pd.DataFrame(data).to_csv('31/data/words_to_learn.csv', index=False)
    new_word_data = random.choice(data)
    front_side = {'word': new_word_data['French'], 'language': 'French'}
    back_side = {'word': new_word_data['English'], 'language': 'English'}
    card_data = {'front': front_side, 'back': back_side}
    canvas.itemconfig(word, text=card_data['front']['word'])
    canvas.itemconfig(language, text=card_data['front']['language'])
    flip_card()
    flip = window.after(3000, flip_card,'back')

# ---------------------------- CARD FLIPPING ------------------------------- #
def flip_card(side='front'):
    image = card_front_image if side == 'front' else card_back_image 
    canvas.itemconfig(card, image=image)
    fill = 'white' if side=='back' else 'black' 
    canvas.itemconfig(word, text=card_data[side]['word'], fill=fill)
    canvas.itemconfig(language, text=card_data[side]['language'], fill=fill)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flash')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file='31/images/card_front.png')
card_back_image = PhotoImage(file='31/images/card_back.png')
card = canvas.create_image(CARD_WIDTH/2, CARD_HEIGHT/2, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

word = canvas.create_text(*WORD_POS.values(), text='Word', font=WORD_FONT)
language = canvas.create_text(*LANGUAGE_POS.values(), text='Title', font=LANGUAGE_FONT)

left_image = PhotoImage(file='31/images/wrong.png')
left_button = Button(image=left_image, highlightthickness=0, command=lambda: new_word(False))
left_button.grid(column=0, row=1)

right_image = PhotoImage(file='31/images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=new_word)
right_button.grid(column=1, row=1)

new_word()

window.mainloop()
