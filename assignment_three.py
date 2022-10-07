# Anderson Iskowitz
# Unit 3 Project
#how to make the length return as a float
#asking for inputs about the length and color of the plus signs

length = int(input("What is the length of the side?:"))
colorCenter = input("What is the color of the center hexagon?:")
colorPetal = input("What is the color of the petals?:")


def drawHexagon():
    t.fillcolor(colorPetal)
    for x in range(6):
        t.fd(length)
        t.rt(60)





#importing turtle to draw the plus signs
import turtle
t = turtle.Turtle()
t.color(colorCenter)
drawHexagon()


turtle.exitonclick()