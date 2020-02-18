#Casandra Villagran
#2/13/2020

#Asking the user user for the number of sides, the length of the side, the color of the line, and the fill color of a regular polygon.


numsides= int(input ("How many sides are in the polygon? "))

lensides= int(input ("what are the lengths of the sides? "))

linecolor= input ("What is the color of the line? ")

fillcolor= input ("What is the fill color of the regular polygon? ")


Angle= (360/ numsides)

import turtle

t= turtle.Turtle()
t.begin_fill()

t.fillcolor(fillcolor)

t.color(linecolor)


for f in range (numsides):
    t.forward(lensides)
    t.right(Angle)


    
t.end_fill()


  
