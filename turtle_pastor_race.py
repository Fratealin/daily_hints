#! /usr/local/bin/python3

import turtle, operator
from turtle import Turtle
from random import randint, choice



# https://www.youtube.com/watch?v=qOsbvj87Uos&t=7s
# made a subclass and used it to give a name and a score
# used operator and sorted in order to sort class according to attribute


import logging
logging.basicConfig(level=logging.DEBUG)

#Put this line where you want to see if there's an error
logging.debug('The Log message.')
# eg., logging.debug(type(first))

# put this line in to disable logging messages
logging.disable(logging.CRITICAL)






def random_color():
    colors = "red blue purple gray brown navy orange"
    colorList = colors.split()
    return choice(colorList)



def is_winner(kame, direction):
    if direction == "right":
        finish_line = 350
        if kame.pos()[0] >= finish_line:
            return True
    else:
        finish_line = -350
        if kame.pos()[0] <= finish_line:
            return True
    return False


def make_window():
    #WINDOW SETUP
    text = "turtle pastors go to the races"
    window = turtle.Screen()

    window.title(f"!!!  {text}  !!!")
    turtle.bgcolor("forestgreen")
    turtle.color("white")
    turtle.speed(0)
    #lift pen to move turtle
    turtle.penup()
    #set x, y coords
    turtle.setpos(-140, 180)
    turtle.write(text, font = ("Arial", 30, "bold"))
    turtle.penup()

    # DIRT Decoration
    turtle.setpos(-400, -180)
    turtle.color("chocolate")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(300)
    turtle.end_fill()




    # FINISH LINE - TRICKY - DOESN'T MAKE SENSE
    stamp_size = 20
    square_size = 15
    finish_line = 350
    turtle.color("black")
    turtle.shape("square")
    turtle.shapesize(square_size/stamp_size)
    turtle.penup()

    for i in range(10):
        turtle.setpos(finish_line, (150 - (i * square_size * 2)))
        turtle.stamp()

    for j in range(10):
        turtle.setpos(finish_line + square_size, ((150 - square_size) - (j*square_size*2)))
        turtle.stamp()

    turtle.hideturtle()







make_window()


#make turtle subclass, kame, to include name
class Kame(Turtle):
    name = ""
    score = 0


def make_turtle(y, name):
    #check they are all different colors
    while True:
        color = random_color()
        if color not in colors:
            colors.append(color)
            break
    turtle = Kame()
    turtle.speed(0)
    turtle.color(color)
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(-350, y)
    turtle.pendown()
    turtle.name = name
    return turtle


colors = []
turtles = [make_turtle(100, "Alwyn"), make_turtle(50, "Mark Rainbow"), make_turtle(0, "Tico Rice"),
           make_turtle(-50, "Tim")]


"""
turtles.append(make_turtle(100, "Alwyn"))
turtles.append(make_turtle(50, "Mark Rainbow"))
turtles.append(make_turtle(0, "Tico Rice"))
turtles.append(make_turtle(-50, "Tim"))
"""


for turtl in turtles:
    turtl.shape("turtle")
    for turn in range(9):
        turtl.right(10)
    for turn in range(18):
        turtl.left(10)
    for turn in range(9):
        turtl.right(10)



direction = "right"

try:


    #makes the kames go back and forth infinitely
    #Move turtles forward 350
    while True:
        for kame in turtles:
            #todo make it 5 again
            kame.forward(randint(0, randint(10, 30)))



            if is_winner(kame, direction):
                kame.score += 1
                print("%s is the winner" % kame.name)


                print(f"{turtles[0].name} {turtles[0].score}\t{turtles[1].name} {turtles[1].score}\t{turtles[2].name} {turtles[2].score}\t{turtles[3].name} {turtles[3].score}")
                if direction == "right":
                    direction = "left"
                    xcoord = 350
                else:
                    direction = "right"
                    xcoord = -350
                turtles[0].goto(xcoord, 100)
                turtles[1].goto(xcoord, 50)
                turtles[2].goto(xcoord, 0)
                turtles[3].goto(xcoord, -50)
                # spin for return race
                for kame in turtles:
                    for turn in range(18):
                        kame.right(10)
                    kame.penup()
                break

except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.

    # put turtles in order
    turtles = sorted(turtles, key=operator.attrgetter('score'), reverse=True)
    turtles = sorted(turtles, key=lambda x: x.score, reverse=True)
    turtles.sort(key=lambda x: x.score, reverse=True)
    print(f"{turtles[0].name} {turtles[0].score}\t{turtles[1].name} {turtles[1].score}\t{turtles[2].name} {turtles[2].score}\t{turtles[3].name} {turtles[3].score}")


    exit()







