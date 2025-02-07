import requests, re, datetime as dt, email_sender, time
import email_sender.email_sender


MY_LONG = 23.823311
MY_LAT = 53.670429
MY_EMAIL = 'dansoltan05@gmail.com'
PASSWORD = 'jwka uwus daeb licl'
RECEIVER = 'mysecondaryaccpl123xyz@gmail.com'

responce = requests.get('http://api.open-notify.org/iss-now.json').json()
iss_pos = (lambda x: list(map(float,(x['longitude'], x['latitude']))))(responce['iss_position'])
print(iss_pos)

def iss_is_close():
    distances = [abs(a-b) for (a,b) in zip((MY_LONG, MY_LAT), iss_pos)]
    for distance in distances:
        if distance>5:
            return False
    return True

if iss_is_close():
    print('Iss is close')

params = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

responce = requests.get('https://api.sunrise-sunset.org/json', params=params)
data = responce.json()
sunrise = data['results']['sunrise']
sunrise = re.sub(r'T[^:]*:', f'T{(lambda: (int(re.findall(r'T[^:]*:', sunrise)[0][1:-1])+3))()}:', sunrise).split(':')[0].split('T')[-1]
sunset = data['results']['sunset']
sunset = re.sub(r'T[^:]*:', f'T{(lambda: (int(re.findall(r'T[^:]*:', sunset)[0][1:-1])+3))()}:', sunset).split(':')[0].split('T')[-1]
sunset,sunrise = map(lambda x: int(x), [sunset,sunrise])
print(sunrise, sunset, dt.datetime.now().hour)

def is_dark_outside(sunrise, sunset):
    if dt.datetime.now().hour > sunset or dt.datetime.now().hour < sunrise:
        return True
    else:
        return False
    
while __name__ == '__main__':
    if iss_is_close() and is_dark_outside(sunrise, sunset):
        email_sender.email_sender.send_gmail(MY_EMAIL,PASSWORD,RECEIVER,'ISS', 'Iss is close! Check it out!:)', 'me')
        print('Sent')
    else:
        print('Conditions not met')
    time.sleep(60)