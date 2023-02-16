import turtle
import pandas

screen = turtle.Screen()
image = "UsStatesGame/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.ht()
writer.penup()
data = pandas.read_csv("UsStatesGame/50_states.csv")
data = data.astype({'x':'int'})
data = data.astype({'y':'int'})
states_list = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?" ).title()
    if answer_state == "Exit":
        break
    for state in states_list:
        if state == answer_state:
            guessed_states.append(state)
            current_state = data[data.state == state]
            state_x = int(current_state.x)
            state_y = int(current_state.y)
            print(state_x)
            
            writer.goto(state_x, state_y)
            writer.write(state)

list_to_learn = []
for state in states_list:
    if state not in guessed_states:
        list_to_learn.append(state)

to_learn = pandas.DataFrame(list_to_learn)
to_learn.to_csv("UsStatesGame/states_to_learn.csv")


