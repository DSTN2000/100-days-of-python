from flask import *

application = Flask(__name__)

def add_tags(*tags):
    def wrapper_wrapper(fun):
        def wrapper():
            contents = fun()
            try:
                return f'{''.join(['<'+tag+'>' for tag in tags])}{contents}{''.join(['</'+tag+'>' for tag in tags])}'
            except:
                print('Invalid tag')
            #return fun()
        return wrapper 
    return wrapper_wrapper

@application.route('/')
@add_tags('strong')
def show_index_page():
    return 'Hello, World!'

if __name__ == '__main__':
    application.run(debug=True)