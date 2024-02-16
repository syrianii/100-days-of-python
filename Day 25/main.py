import turtle
import pandas as pd

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")

turtle.addshape(IMAGE)
turtle.shape(IMAGE)

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:

  answer_state = screen.textinput(
      title=f"{len(guessed_states)}/50 Guess the State",
      prompt="What's another state's name?").title()

  if answer_state == "Exit":
    missing_states = []
    missing_states = [state for state in states if state not in guessed_states]
    new_data = pd.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    break

  if answer_state in states:

    state = turtle.Turtle(visible=False)
    state.penup()
    state_data = data[data["state"] == answer_state]
    guessed_states.append(answer_state)
    state.goto(int(state_data.x), int(state_data.y))
    state.write(answer_state)
