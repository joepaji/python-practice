#!/usr/bin/env python3
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Guessing Game")
image = 'blank_states_img.gif'
screen.setup(725,491)
turtle.addshape(image)
turtle.shape(image)
data = pandas.read_csv('50_states.csv')
states = data.state.to_list()

while len(states) > 0:
    answer = screen.textinput(title=f"{50-len(states)}/50 States correct", \
        prompt="What's the next state?".title())
    answer = answer.title()
    if answer == 'Exit':
        break
    if answer in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = data[data.state == answer]
        t.goto(int(state_info.x), int(state_info.y))
        t.write(state_info.state.item())
        states.remove(answer)

df = pandas.DataFrame(states, columns=["States"])
df.to_csv('states_to_learn.csv', index=False)