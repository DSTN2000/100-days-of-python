import turtle
import pandas as pd


FONT = ('Arial', 8, 'normal')

screen = turtle.Screen()
screen.title('States')
map_image = '25/states/blank_states_img.gif'
screen.addshape(map_image)
map = turtle.Turtle(map_image)
writer = turtle.Turtle(visible=False)

df = pd.read_csv('25/states/50_states.csv')
states = [state.lower() for state in df['state'].to_list()]
not_guessed_states = [state.title() for state in states]
# print(states)
correct_guesses = 0
while correct_guesses < 50:
    answer = screen.textinput(f'Guessed {correct_guesses}/50', 'Enter the name of a state').lower()
    if answer in states:
        answer = ' '.join([word.capitalize() for word in answer.split()])
        position = df[df['state'] == answer]
        position = (int(str(position.x.to_list()).strip('[]')), int(str(position.y.to_list()).strip('[]')))
        print(position)
        writer.teleport(*position)
        writer.write(answer,font=FONT)
        correct_guesses+=1
        try:
            not_guessed_states.remove(answer.title())
        except:
            pass
    elif answer.title() == 'Exit' :
        break

not_guessed_states = pd.Series(not_guessed_states)
not_guessed_states.to_csv('25/states/not_guesses_states.csv', index = False, header=False)


screen.mainloop()

