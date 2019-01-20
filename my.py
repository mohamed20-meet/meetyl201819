from turtle import *
import random
import turtle
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.r=(r/10)
		self.color(color)
		self.shape('circle')
		self.penup()
		self.goto(x,y)
	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		new_x=self.dx+current_x
		current_y=self.ycor()
		new_y=self.dy+current_y
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		up_side_ball=new_y+self.r
		down_side_ball=new_y-self.r
		self.goto(new_x,new_y)
		if right_side_ball>screen_width:
			self.dx=-self.dx
		if left_side_ball< -screen_width:
			self.dx=-self.dx
		if up_side_ball>screen_height:
			self.dy=-self.dy
		if down_side_ball< -screen_height:
			self.dy=-self.dy
	BALLS = ()
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADUIS=10
MAXIMUM_BALL_RADUIS= 100
MINIMUM_BALL_DX= -5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY= 5
for i in range (NUMBER_OF_BALLS):
	
	x = random.randint(-screen_width +MAXIMUM_BALL_RADUIS)
	x = random.randint(screen_width - MAXIMUM_BALL_RADUIS)
	y = random.randint(-screen_height + MAXIMUM_BALL_RADUIS)
	y = random.randint(screen_height - MAXIMUM_BALL_RADUIS)
	dx = random.randint(MINIMUM_BALL_DX)
	dx = random.randint(MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY)
	dy = random.randint(MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADUIS)
	radius = random.randint(MAXIMUM_BALL_RADUIS)
	color = (random.random(), random.random(), random.random())




    


my_tuple = (3, 5, 4)

random_color = (random.random(), random.random(), random.random())
screen_width = turtle.getcanvas() .winfo_width()/2
screen_height = turtle.getcanvas() .winfo_height()/2
myball=Ball(100,200,50,50,50,random_color)
myball.move(100,100)
myball2=Ball(100,200,50,50,50,random_color)
myball2.move(100,100)


while True:
	myball.move(screen_width,screen_height)
