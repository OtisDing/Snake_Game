import turtle
from turtle import Turtle, Screen
import random

isRaceOn = False
screen = Screen()
screen.setup(width=500, height=400)
userBet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
yPositions = [-70, -40, -10, 20, 50, 80]
allTurtle = []

for turtleIndex in range(0, 6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(colours[turtleIndex])
    newTurtle.penup()
    newTurtle.goto(x=-230, y=yPositions[turtleIndex])
    allTurtle.append(newTurtle)

if userBet:
    isRaceOn = True

while isRaceOn:

    for turtle in allTurtle:
        if turtle.xcor() > 230:
            isRaceOn = False
            winningColour = turtle.pencolor()
            if winningColour == userBet:
                print(f"You've won! The {winningColour} turtle is the winner!")
            else:
                print(f"You've lost! The {winningColour} turtle is the winner!")
        randDistance = random.randint(0, 10)
        turtle.forward(randDistance)


screen.exitonclick()
