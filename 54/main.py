from flask import *

test = Flask(__name__)

@test.route('/')
def hello_world():
    return 'Hello, World!'

test.run(debug=True)

