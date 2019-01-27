from game import Ball
import time
import turtle
from turtle import *
import random
turtle.tracer(0)
import math
import sys


turtle.bgpic("bg.gif")

score = 0

RUNNING = True
sleep = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT =turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(0,1,10,30,40,"blue")

NUMBER_OF_BALLS = 8
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range (NUMBER_OF_BALLS):
	x = random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT) + int(MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	while dx == 0:
		dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	while dy == 0:
		dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	ball1 = Ball(x, y, dx, dy, radius, color)

	BALLS.append (ball1)


def move_all_balls():
	for D in BALLS:
		D.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball_1, ball_2):
	if ball_1 == ball_2 :
		return False
		
	distance_between_centers = ((ball_1.xcor()-ball_2.xcor())**2 + (ball_1.ycor()-ball_2.ycor())**2)**0.5

	if distance_between_centers+10 <= ball_1.radius + ball_2.radius:
		return True
	else:
		return False
		sys.exit("GAME OVER")
		print("THE END")

def check_all_balls_collision():
	for ball_1 in BALLS:
		for ball_2 in BALLS:
			if collide(ball_1,ball_2) == True:
				radius_a = ball_1.radius
				radius_b = ball_2.radius
				X_coordinate = random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
				Y_coordinate = random.randint(int(-SCREEN_HEIGHT) + int(MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAXIMUM_BALL_RADIUS))
				X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while X_axis_speed == 0:
					 X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				Y_axis_speed  = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while Y_axis_speed  == 0:
					Y_axis_speed  = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				a = random.randint(0,255)
				b = random.randint(0,255)
				c = random.randint(0,255)
				color = (a,b,c)

				if ball_1 < ball_2:
					ball_1.goto(X_coordinate, Y_coordinate) 
					ball_1.dx = X_axis_speed 
					ball_1.dy = Y_axis_speed
					ball_1.color(color)
					ball_1.radius = radius
					ball_2.radius += 5
					ball_1.shapesize(ball_1.radius/10)
					ball_2.shapesize(ball_2.radius/10)

				

				else:
					ball_2.goto(X_coordinate, Y_coordinate)
					ball_2.dx = X_axis_speed 
					ball_2.dy = Y_axis_speed
					ball_2.radius = radius
					ball_2.color(color)
					ball_1.radius += 5
					ball_1.shapesize(ball_1.radius/10)
					ball_2.shapesize(ball_2.radius/10)



				
def check_myball_collision():
	global score
	for i in BALLS:
		if collide(i,MY_BALL) == True:
			print(i.radius, MY_BALL.radius)
			radius_i = i.radius
			radius_MY_BALL= MY_BALL.radius

			if MY_BALL.radius < i.radius:
				RUNNING = False
				turtle.goto(-200,0)
				turtle.color("red")
				turtle.write("Loser", move=False, font=("Arial", 50, "bold"))
				time.sleep(3)
				sys.exit("Error message")


			else:
				score += 1
				X_coordinate = random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
				Y_coordinate = random.randint(int(-SCREEN_HEIGHT) + int(MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAXIMUM_BALL_RADIUS))
				X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while X_axis_speed == 0:
					X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				Y_axis_speed  = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while Y_axis_speed  == 0:
					Y_axis_speed  = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)
				color = (r,g,b)

			
				i.goto(X_coordinate, Y_coordinate)
				i.dx = X_axis_speed 
				i.dy = Y_axis_speed
				i.radius = radius
				i.shapesize(radius/10)
				i.color(color)
				MY_BALL.radius = MY_BALL.radius+5
				MY_BALL.shapesize(MY_BALL.radius/10)


	return True

def movearound(event):
	NEW_X_coordinate = event.x - SCREEN_WIDTH
	NEW_Y_coordinate = -(event.y - SCREEN_HEIGHT)
	MY_BALL.goto(NEW_X_coordinate, NEW_Y_coordinate)


def countdown():
	for i in range(3, 0, -1):
		turtle.penup()
		turtle.color("red")
		turtle.goto(0, 200)
		turtle.clear()
		turtle.write(str(i), font=("ariel",20,"normal"))
		turtle.update()
		time.sleep(1)


countdown()

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while RUNNING == True:
	
	SCREEN_WIDTH=turtle.getcanvas().winfo_width()//2 
	SCREEN_HEIGHT=turtle.getcanvas().winfo_height()//2



	move_all_balls()
	check_myball_collision()
	turtle.penup()
	turtle.color("white")
	turtle.goto(-800,200)
	turtle.clear()
	turtle.write("score: " +str(score), font=("ariel",20,"normal"))

	getscreen().update()
	time.sleep(sleep)
	

mainloop()