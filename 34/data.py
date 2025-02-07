import requests
question_data = [data for data in requests.get('https://opentdb.com/api.php?amount=10&type=boolean').json()['results']]
# for data in question_data:
#     print(data, end=f'{'\n'*5}')
