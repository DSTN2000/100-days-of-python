from flask import *
import random

application = Flask(__name__)

INDEX_GIF = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'
LOWER_GIF = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
CORRECT_GIF = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'
HIGHER_GIF = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'

@application.route('/')
def show_index_page():
    return f'<img src={INDEX_GIF} >'

@application.route('/<int:number>')
def show_feedback(number):
    if number == correct_number:
        return f'<h1 style=\'color: gold\'>Gongrats, you found me!</h1><img src={CORRECT_GIF} >'
    elif number < correct_number:
        return f'<h1 style=\'color: red\'>Too low, try again!</h1><img src={LOWER_GIF} >'
    else:
        return f'<h1 style=\'color: purple\'>Too high, try again!</h1><img src={HIGHER_GIF} >'

if __name__ == '__main__':
    correct_number = random.randint(1,10)
    application.run(debug=True)