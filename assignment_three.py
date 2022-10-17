#Anderson Iskowitz Unit 3 Project
#Last edited: 14 October 2022
#This document draws a flower out depending on the user's input of size and color
'''
getting input for the length'''

length = int(input("What is the length of the side?:"))

'''getting the color of the center hexagon'''
colorCenter = input("What is the color of the center hexagon?:")

'''getting the color of the outer hexagons'''
colorPetal = input("What is the color of the petals?:")

'''making movement of the length twice'''
lengthMovement = length * 2

# defining shapes
'''Defining hexagon shape and setting the color'''
def drawHexagon(color):
    t.fillcolor(color)
    t.begin_fill()
    for x in range(6):
        t.fd(length)
        t.right(60)
    t.end_fill()
'''defining the centeral hexagon and defining the color'''
def drawCenter():
    t.rt(60)
    t.fd(length)
    t.left(60)
    drawHexagon(colorCenter)
'''defining the total flower shape using the draw hexagon function'''
def drawFlower():
    for x in range(6):
        t.penup()
        t.fd(lengthMovement)
        t.pendown()
        drawHexagon(colorPetal)
        t.rt(60)

'''defining main function'''
def main():
    drawFlower()
    drawCenter()

'''importing turtle'''
import turtle
'''defining t to turtle so it is easier to type'''
t = turtle.Turtle()
# calling main function
main()

import unittest

class TestStringMethods(unittest.TestCase):
    def upperTest(self):
        self.assertEqual('boo'.upper(), 'BOO')

    def testIsUpper(self):
        self.assertTrue('BOO'.isupper())
        self.assertFalse('Boo'.isupper())

if __name__ == '__main__':
    unittest.main()

turtle.exitonclick()