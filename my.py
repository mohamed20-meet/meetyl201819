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
	def move(self,screen_width,screen_height):
		current_x=self.x
		new_x=self.dx+current_x
		current_y=self.y
		new_y=self.dy+current_y
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		up_side_ball=new_y+self.r
		down_side_ball=new_y-self.r
		self.goto(new_x,new_y)
		if right_side_ball>screen_width:
			self.dx=-self.dx
		if left_side_ball>screen_width:
			self.dx=-self.dx
		if up_side_ball>screen_height:
			self.dy=-self.dy
		if down_side_ball>screen_height:
			self.dy=-self.dy


    


	
		

myball=Ball(100,200,50,50,50,"blue")
myball.move(100,100)
turtle.mainloop()
	