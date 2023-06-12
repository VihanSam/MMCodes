#cookie clicker
import turtle

wn = turtle.Screen()
wn.title("Cookie Clicker by Vihan")
wn.bgcolor("black")

wn.register_shape("cookie.png")

cookie = turtle.Turtle()
cookie.shape("cookie.png")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 400)
pen.write(f"Clicks : {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked():
    global clicks
    click+=1
    pen.clear()
    pen.writepen.write(f"Clicks : {clicks}", align="center", font=("Courier New", 32, "normal"))

cookie.oneclick(clicked)



wn.mainloop()