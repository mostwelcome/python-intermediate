from os import stat
import turtle
import pandas
from pandas.core.indexes.api import all_indexes_same
screen = turtle.Screen()
screen.title('U.S states game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv('50_states.csv')

all_states = data['state'].to_list()

gussed_list = []
while len(gussed_list) <50:
    state = screen.textinput(title=f'{len(gussed_list)}',prompt="what's another state name?").strip().title()
    print(type(state))

    if state == 'Exit':
        break
    if state in all_states:
        state_data = data[data['state'] == state]
        print(state_data)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())
        gussed_list.append(state)


#when exiting the game in this csv will include all the state names which u were not able to guess
remaining_states = set(all_states) ^ set(gussed_list)

remaining_state_df = pandas.DataFrame(remaining_states)

print(remaining_state_df)
remaining_state_df.to_csv('other_states.csv')