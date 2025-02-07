import smtplib, datetime as dt, random
from email_sender.email_sender import send_gmail

MY_EMAIL = 'dansoltan05@gmail.com'
PASSWORD = 'jwka uwus daeb licl'
RECEIVER = 'mysecondaryaccpl123xyz@gmail.com'

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

current_time = dt.datetime.now()
week_day = current_time.weekday()
if dt.datetime.now().weekday() == week_day:
    with open('32/quotes.txt') as quotes:
        quotes = quotes.readlines()
        quote_to_send = random.choice(quotes)
        send_gmail(MY_EMAIL, PASSWORD, RECEIVER, f'{WEEKDAYS[week_day]} Motivational Quote', quote_to_send, 'Me')
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=MY_EMAIL, password=PASSWORD)
# connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER,
# msg='Subject:Greetings!\n\nHello, World!')
# connection.close()


