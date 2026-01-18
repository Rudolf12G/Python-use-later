import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("I LOVE YOU Rudolf ❤️")
turtle.tracer(0, 0)

screen_width = screen.window_width() // 2
screen_height = screen.window_height() // 2

texts = []
directions = {}

def create_text():
    if len(texts) >= 7:
        return
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color(random.choice(["red", "hot pink", "deep pink", "light coral"]))
    t.goto(random.randint(-screen_width + 50, screen_width - 50),
           random.randint(-screen_height + 50, screen_height - 50))
    texts.append(t)
    directions[t] = (random.choice([-3, 3]), random.choice([-3, 3]))

create_text()
last_spawn = time.time()

while True:
    for t in texts:
        x, y = t.position()
        dx, dy = directions[t]
        if x + dx > screen_width or x + dx < -screen_width:
            dx *= -1
        if y + dy > screen_height or y + dy < -screen_height:
            dy *= -1
        directions[t] = (dx, dy)
        t.goto(x + dx, y + dy)

    if time.time() - last_spawn > 1:
        create_text()
        last_spawn = time.time()

    for t in texts:
        t.clear()
        t.write("I LOVE YOU ❤️", align="center", font=("Arial", 24, "bold"))

    turtle.update()
    time.sleep(0.03)