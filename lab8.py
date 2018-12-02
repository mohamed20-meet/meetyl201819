from turtle import *
import random
import turtle
import math
class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape('circle')
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

ball1 = Ball(30,'red', 10)
ball2 = Ball(20, 'blue',10)
balls=[]
balls.append(ball1)
balls.append(ball2) 
'''ball1.goto(100,0)
'''
def check_collision(ball1,ball2):
	x2=ball1.xcor()
	y2=ball1.ycor()
	x1=ball2.xcor()
	y1=ball2.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D > balls[1].radius +balls[0].radius :
		print('the balls did not collid')
	if D <= balls[1].radius +balls[0].radius :	
		print('the balls collided')
check_collision(ball1,ball2)
def teleport ():
	oldx2=ball1.xcor()
	oldy2=ball1.ycor()
	oldx1=ball2.xcor()
	oldy1=ball2.ycor()
	D = math.sqrt(math.pow((oldx2-oldx1),2) + math.pow((oldy2-oldy1),2))
	if D <= balls[1].radius +balls[0].radius:
		ball1.goto(random.randint(1,100),random.randint(1,100))
teleport()
turtle.mainloop()
