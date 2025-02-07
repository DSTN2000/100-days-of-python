menu = {
    'espresso': {
        'water': 50,
        'coffee': 18,
        'milk': 0,
        'money': 1.50
    },

    'latte': {
        'water': 200,
        'coffee': 24,
        'milk': 150,
        'money': 2.50
    },

    'cappuccino': {
        'water': 250,
        'coffee': 24,
        'milk': 100,
        'money': 3.00
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

coins = {
    'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01
}

def report():
    '''Print the report of remaining resources'''
    print(*[f'{key.capitalize()}: '\
                                f'{'$' if key == 'money' else ''}{value}'\
                                f'{'g' if key == 'coffee' else 'ml' if key != 'money' else ''}' 
                                for (key, value) in resources.items()], sep ='\n')

def verify_resources_sufficiency(type):
    '''Checks if there are enough resources for the specified type of coffee'''
    for k,v in list(resources.items())[:-1]:
        if resources[k] < menu[type][k]:
            print(f'Insufficient {k}')
            return
    return True

def subtract_resources(type):
    '''Subtracts the resources required to serve the specified type of coffee'''
    for k,v in list(resources.items())[:-1]:
        resources[k] -= menu[type][k]

def prompt_coins():
    '''Prompt the user to insert coins and return the total amount entered'''
    total = 0
    for k,v in coins.items():
        while __name__=='__main__':
            try:
                total += int(input(f'How many {k}? '))*v
                break
            except:
                print('Invalid amount')
                continue
    return round(total,2)

def process_coins(total, type):
    '''Process the total amount of money inserted to buy the specified type of coffee'''
    if total >= menu[type]['money']:
        resources['money'] += menu[type]['money']
        change = round(total - menu[type]['money'],2)
        if change:
            print(f'Here is ${change} in change')
    else:
        print('Insufficient money! Money refunded')
        return
    return True

def serve(type):
    '''Try to serve the specified type of coffee'''
    if verify_resources_sufficiency(type):
        total = prompt_coins()
        if process_coins(total, type):
            subtract_resources(type)
            report()
            print(f'Here is your {type}!\n')

actions = {
    'serve': serve,
    'report': report,
    'off': lambda: exit()
}

def process_input():
    '''Processes input'''
    input_ = input('What would you like? (espresso/latte/cappuccino): ')
    if input_ in menu:
        actions['serve'](input_)
    else:
        try:
            actions[input_]()
        except Exception:
            print('Invalid input!')
            process_input()  

while __name__=='__main__':
    process_input()