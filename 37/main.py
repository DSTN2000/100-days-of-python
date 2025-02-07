import requests as req, datetime as dt

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'

AUTH_TOKEN = 'W<d6uD[/U+=E]rw9VS"*e^y!}47tp,?q'
USERNAME = 'myusername123'

GRAPH_ENDPOINT = PIXELA_ENDPOINT+'/'+USERNAME+'/graphs'
GRAPH_ID = 'graph1'

headers = {
    'X-USER-TOKEN': AUTH_TOKEN
}

today = dt.datetime.now()
today_date = today.strftime('%Y%m%d')
print(today_date)

data = {
    'date': input(),
    'quantity': input()
}

responce = req.delete(GRAPH_ENDPOINT+'/'+GRAPH_ID+'/'+data['date'], headers=headers)      #deletes a pixel using DELETE
print(responce.text)

# responce = req.put(GRAPH_ENDPOINT+'/'+GRAPH_ID+'/'+data['date'], json={'quantity': data['quantity']}, headers=headers)      #updates a pixel using PUT
# print(responce.text)

# responce = req.post(GRAPH_ENDPOINT+'/'+GRAPH_ID, json=data, headers=headers)      #creates a new pixel using POST
# print(responce.text)


# graph_config = {               #this was needed in order to create a new graph
#     'id': 'graph1',
#     'name': 'Screen Time',
#     'unit': 'Minutes',
#     'type': 'float',
#     'color': 'shibafu'
# }

# responce = req.post(GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(responce.text)



# payload = {                               #this was needed in order to create an account @ pixela
#     'token': AUTH_TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes'
# }

# responce = req.post(PIXELA_ENDPOINT, json=payload)
# print(responce.json())
