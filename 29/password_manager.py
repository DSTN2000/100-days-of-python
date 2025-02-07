from tkinter import *
from tkinter import messagebox
from password_gen import generate_password
import pyperclip
import pandas as pd
import json

LABEL_FONT = ('Arial', 8, 'normal')

# ---------------------------- SAVE PASSWORD ------------------------------- #

data = pd.read_csv('29/password_manager.csv', index_col=0).to_dict('list')
#print(data)

def save_data(data=data):
    for entry in entries:
        if not entry.get():
            messagebox.showwarning(title='Oops', message='Don\'t leave any fields empty!')
            return
    answer_is_ok = messagebox.askokcancel(title=website_entry.get(), message=f'The details entered are: '\
                           f'\nWebsite: {website_entry.get()}'\
                           f'\nEmail/Username: {email_entry.get()}'\
                           f'\nPassword: {password_entry.get()}')

    if answer_is_ok:        
        for k, i in zip(data, range(3)):
            data[k].append(entries[i].get())

        #add to the .csv file
        data = pd.DataFrame(data).drop_duplicates().reset_index(drop=True)
        print(data)
        data.to_csv('29/password_manager.csv')

        #add to the .json file
        data_for_json=json.loads(data.to_json(orient='records'))
        json.dump(data_for_json,open('29/password_manager.json', 'w'), indent=5)

        password_entry.delete(0,END)
        website_entry.delete(0,END)
        messagebox.showinfo(title='Success', message='Added new password data')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file='29/logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text='Website: ', font=LABEL_FONT)
website_label.grid(column=0, row=1, sticky='E')
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=1, sticky='W')
website_entry.focus()

email_label = Label(text='Email/Username: ', font=LABEL_FONT)
email_label.grid(column=0, row=2, sticky='E')
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,'example@gmail.com')

password_label = Label(text='Password: ', font=LABEL_FONT)
password_label.grid(column=0, row=3, sticky='E')
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1, sticky='W')
gen_button = Button(text='Genereate Password', font=LABEL_FONT, width=12,\
                    command=lambda: (password_entry.delete(0,END),\
                                     password_entry.insert(0,generate_password()),\
                                     pyperclip.copy(password_entry.get())))
gen_button.grid(column=1, row=3, columnspan=2, sticky='E')


def search():
    data_from_json = json.load(open('29/password_manager.json'))
    print(data_from_json)
    res=[]
    for dict_ in data_from_json:
        if dict_['website'] == website_entry.get():
            res.append(f'Email/Username: {dict_['email']}\n'\
                       f'Password: {dict_['password']}')
    if len(res) > 1:
        res = [f'{i+1}. {res[i]}' for i in range(len(res))]
    if res:
        messagebox.showinfo(message='\n\n'.join(res), title=website_entry.get())
    else:
        messagebox.showinfo(message='No assotiated data found', title=website_entry.get())
search_button = Button(text='Search', font=LABEL_FONT, width=12, command=search)
search_button.grid(column=1, row=1, columnspan=2, sticky='E')

entries = [website_entry, email_entry, password_entry]

add_button = Button(text='Add', font=LABEL_FONT, width=34, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
