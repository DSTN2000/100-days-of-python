import random
import string

def generate_password():
  letters = string.ascii_letters
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = [char for char in [random.choice(letters) for _ in range(nr_letters)]+\
                  [random.choice(symbols) for _ in range(nr_symbols)]+\
                  [random.choice(numbers) for _ in range(nr_numbers)]]

  random.shuffle(password_list)

  return ''.join(char for char in password_list)