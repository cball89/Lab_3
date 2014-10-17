#Caroline Ball
#Oct. 16th 2014
#GIS 501
#Lab 3

#Step 4- Drawing Turtles

from turtle import *

print("Hello!")

print("Welcome to the Turtle Game!!!")

num_str = input("Choose a number and press Enter")

turtle = Pen()
turtle.shape("turtle")
turtle.speed("slow")
turtle.screen.bgcolor("yellow")
turtle.color("green")

for i in range(num_str):
    turtle.forward(25)
    turtle.right(360/num_str)

    

