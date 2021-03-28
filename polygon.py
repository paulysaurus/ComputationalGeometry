# draw any polygon in turtle
import turtle
 
t = turtle.Turtle()  

l = int(80)
# taking input for the no of the sides of the polygon
n = int(input("Enter the no of the sides of the polygon : "))

if n > 2:
    for _ in range(n):
        turtle.forward(l)
        turtle.right(360 / n)
else: 
    print("Introduce 3 sides or more ")
    
turtle.exitonclick()
