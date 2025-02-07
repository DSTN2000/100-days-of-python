from flask import *
import datetime as dt
import requests, pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('test.html', author='me', year=dt.datetime.now().year)


@app.route('/guess/<name>')
def get_name_data(name):
    name = name.capitalize()
    responces = [requests.get(f'{x}', params={'name': name}).json() for x in [
        'https://api.genderize.io', 'https://api.agify.io']]
    # print([responce.json() for responce in responces])
    data = {'gender': responces[0]['gender'], 'age': responces[1]['age']}
    return render_template('guess.html', author='me', year=dt.datetime.now().year, name=name, **data)

@app.route('/blogs')
def blogs_home():
    data = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    data = data.json()
    print(data)
    return render_template('index.html', data=data)

@app.route('/post/<id>')
def get_post(id):
    data = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    data = pd.DataFrame(data.json())
    data = data[data['id']==int(id)]
    data = data.to_dict(orient='records')[0]
    print(data)
    return render_template('post.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
