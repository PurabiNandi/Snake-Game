# importing the required modules
import turtle # for handling graphics
import time
import random

# we will pass this delay variable in the time libraries sleep function, which will act as a gap
delay = 0.1

# initializing the values of score and highest_score as 0
score = 0
high_score = 0

bodies = []  # creating a empty list for snake's body

# NOTE: For every component we are making a separate turtle

# Getting a screen | Canvas for displaying the game
s = turtle.Screen()  # creating a screen using turtle.screen()
s.title("Snake Game")  # setting the title of the screen
s.bgcolor('yellow')  # setting the background-color of screen
s.setup(width=600, height=600)  # setting the screen dimension
s.tracer(0)  # to turn the turtle animation off

# creating snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()  # used so that if turtle moves then nothing is drawn
head.goto(0,0)  # initially the snake's head is at (0,0)
head.direction = "stop"  # initially the snake is at rest

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)  # initially the food appears in (0,100)

# scoreboard
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)  # position of the score-board
sc.write("Score: 0 | Highest Score: 0", align = "center", font=("ds-digital", 24, "normal"))

# Functions to move the snake in all directions by changing the value of head's direction variable
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()  # getting the present y-coordinate value
        head.sety(y+20)  # adding 20 to y-coordinate to make it move up
    if head.direction == "down":
        y = head.ycor()  # getting the present y-coordinate value
        head.sety(y-20)  # subtracting 20 from y-coordinate to make it move down
    if head.direction == "left":
        x = head.xcor()  # getting the present x-coordinate value
        head.setx(x-20)  # subtracting 20 from x-coordinate to make it move left
    if head.direction == "right":
        x = head.xcor()  # getting the present x-coordinate value
        head.setx(x+20)  # adding 20 to x-coordinate to make it move right

# Event Handling - Keyboard Bindings i.e if the user is performing some actions through the keyboard,
# then how will our code respond to it, for this we have the onkeypress() function
s.listen()
s.onkeypress(go_up, "Up")
s.onkeypress(go_down, "Down")
s.onkeypress(go_left, "Left")
s.onkeypress(go_right, "Right")

# Main Loop
while True:
    s.update()  # this is to update the screen

    # checking collision with border area
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # hide the segments of body
        for segment in bodies:
            segment.goto(1000,1000)  # out of range
        # clear the segments
        bodies.clear()

        # reset score
        score = 0

        # reset delay
        delay = 0.1

        sc.clear()
        sc.write("Score: {} | Highest Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

    # To check collision with food
    # if the gap from food is less than 20 that means collision occurred
    if head.distance(food) <20:
        # move the food to new random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # add a new segment to the head to increase the length of the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        bodies.append(new_segment)  # append new segment to our list bodies

        # shorten the delay, decreasing delay value increases the speed
        delay -= 0.001
        # increase the score
        score += 10

        # Update the highest score
        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("Score: {} | Highest Score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))

    # move the segments in reverse order to move the snake's body
    for index in range(len(bodies)-1,0,-1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x,y)

    # move bodies[0] to head
    if len(bodies)>0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x,y)

    move()

    # To check collision with snake's body itself
    for segment in bodies:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"  # as the player loses we need to stop

            # hide bodies
            for segment in bodies:
                segment.goto(1000,1000)
            bodies.clear()
            # reset score and delay
            score = 0
            delay = 0.1

            # update the scoreboard
            sc.clear()
            sc.write("Score: {} | Highest Score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))
    time.sleep(delay)
