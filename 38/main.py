import requests as r, pandas as pd, datetime as dt, os

# NUTRITIONIX_APP_ID = os.environ['NUTRITIONIX_APP_ID'] 
# NUTRITIONIX_API_KEY = os.environ['NUTRITIONIX_API_KEY']

NUTRITIONIX_APP_ID = '504cbc27'
NUTRITIONIX_API_KEY = '691fdb70b0662916a1f604e2a60263b4'

# os.environ['NUTRITIONIX_APP_ID'] = NUTRITIONIX_APP_ID
# os.environ['NUTRITIONIX_API_KEY'] = NUTRITIONIX_API_KEY

NUTRITIONIX_API_HOST = 'https://trackapi.nutritionix.com'
EXCERCISE_ENDPOINT = NUTRITIONIX_API_HOST + '/' + 'v2/natural/exercise'

headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY
}

payload = {
    'query': input()
}

responce = r.post(EXCERCISE_ENDPOINT, headers=headers, json=payload)
exercises = responce.json()['exercises']
new_data = {
'Date': [],
'Time': [],
'Exercise': [],
'Duration': [],
'Calories': []
}
for exercise in exercises:  
    new_row = {
    'Date': dt.datetime.now().strftime('%d/%m/%Y'),
    'Time': dt.datetime.now().time().isoformat('seconds'),
    'Exercise': exercise['name'].title(),
    'Duration': exercise['duration_min'],
    'Calories': exercise['nf_calories']
    }
    new_data = {k:v+[new_row[k]] for (k,v) in new_data.items()}
    # print(new_data)
    # print()

df = pd.DataFrame(new_data)

try:
    pd.read_csv('38/data.csv')
except FileNotFoundError:
    df.to_csv('38/data.csv', index=False)
else:
    df.to_csv('38/data.csv', mode='a', index=False, header=False)