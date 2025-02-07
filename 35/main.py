import pandas as pd, requests,random
import email_sender
import email_sender.email_sender

MY_LONG = 23.823311
MY_LAT = 53.670429

MY_EMAIL = 'dansoltan05@gmail.com'
PASSWORD = 'jwka uwus daeb licl'
RECEIVER = 'mysecondaryaccpl123xyz@gmail.com'

keys = pd.read_csv('35/keys.csv')
keys = keys.to_dict(orient='list')['keys']

responce = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={MY_LAT}&lon={MY_LONG}&appid={random.choice(keys)}')
responce = responce.json()

will_rain_or_snow = False
forecast_12_hours = responce['list'][:4:]
for timestamp in forecast_12_hours:
    #print(timestamp, '\n')
    for weather_condition in timestamp['weather']:
        if weather_condition['id'] < 700:
            will_rain_or_snow = True
if will_rain_or_snow:
    email_sender.email_sender.send_gmail(MY_EMAIL, PASSWORD, RECEIVER, 'Bring an umbrella!', 'It will probably rain or snow in the next 12 hours', 'me')
    