import turtle
from random import randint

window=turtle.Screen()
window.bgcolor('white')
turtles=[]
k = 0

colors=['red', 'green', 'blue', 'violet', 'purple', 'orange', 'darkblue', 'black']
for i in range(6):
    lines=turtle.Turtle()
    lines.hideturtle()
    lines.penup()
    lines.goto(k,-150)
    lines.pendown()
    lines.goto(k,300)
    lines.write(str(i*10)+'\n')
    k += 50


k =- 100
for i in range(8):
    t = turtle.Turtle('turtle')
    turtles.append(t)
    t.penup()
    t.hideturtle()
    t.speed(0)
    t.goto(-300,0)
    t.showturtle()
    t.speed('slow')
    t.shapesize(1.5)
    t.color('black',colors[i])
    t.left(180)
    t.goto(0,k)
    t.right(-180)
    k += 50



cond=False
while not cond:
    for t in turtles:
        speed=randint(1,20) if not cond else 0
        t.forward(speed/5)
        if t.xcor()>250:
            t.shapesize(2)
            t.write('\t\tWINNER')
            cond = True
            break

turtle.mainloop()

