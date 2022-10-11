'''
Anderson Iskowitz
Unit 3 Project
8 October 2022
This document draws a flower out depending on the user's input
'''

# defining shapes
def drawHexagon(color):
    t.fillcolor(color)
    '''
    t.pencolor(color) makes the pen outline the same as the fill color
    '''
    t.begin_fill()
    for x in range(6):
        t.fd(length)
        t.right(60)
    t.end_fill()

def drawCenter():
    t.rt(60)
    t.fd(length)
    t.left(60)
    drawHexagon(colorCenter)

def drawFlower():
    for x in range(6):
        t.penup()
        t.fd(lengthMovement)
        t.pendown()
        drawHexagon(colorPetal)
        t.rt(60)
# defining main function
def main():
    drawFlower()
    drawCenter()

# getting input for the color and size of the flower
length = int(input("What is the length of the side?:"))
colorCenter = input("What is the color of the center hexagon?:")
colorPetal = input("What is the color of the petals?:")
lengthMovement = length * 2

# importing turtle
import turtle
# defining t to turtle so it is easier to type
t = turtle.Turtle()

# calling main function
main()

turtle.exitonclick()