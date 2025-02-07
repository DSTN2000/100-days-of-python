import pandas as pd

file_path = '26/nato_phonetic_alphabet.csv'
df = pd.read_csv(file_path)

correspondence = {row.letter:row.code for (id, row) in df.iterrows()}
[(lambda letter: print(correspondence[letter],end=' '))(letter.upper()) for letter in input() if letter.upper() in correspondence]


