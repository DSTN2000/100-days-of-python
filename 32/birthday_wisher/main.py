##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

MY_EMAIL = 'dansoltan05@gmail.com'
PASSWORD = 'jwka uwus daeb licl'
RECEIVER = 'mysecondaryaccpl123xyz@gmail.com'

import email_sender.email_sender
import letter_templates, os, random, email_sender, pandas as pd, datetime as dt
templates_dir = letter_templates.__path__[0]
file_names = [name for name in os.listdir(templates_dir) if '.txt' in name]
files = []
for file_name in file_names:
    with open(f'{templates_dir}\\{file_name}') as file:
        files.append(file.read())
df = pd.read_csv('32/birthday_wisher/birthdays.csv', index_col=0)
current_date = (dt.datetime.now().day, dt.datetime.now().month)
for _, row in df.iterrows():
    birth_date = [n for n in row[1:]]
    birth_date = (dt.datetime(*birth_date).day, dt.datetime(*birth_date).month)
    if birth_date == current_date:
        email_msg = random.choice(files).replace('[NAME]', row.name)
        print(email_msg)
        #email_sender.email_sender.send_gmail(MY_EMAIL, PASSWORD, RECEIVER, 'Happy Birthday!', email_msg, 'me')