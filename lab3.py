import turtle
'''
turtle.forward(100)
turtle.right(145)
turtle.forward(100)
turtle.right(145)
turtle.forward(100)
turtle.right(145)
turtle.forward(100)
turtle.right(145)
turtle.forward(100)
'''
'''
turtle.begin_fill()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(50)
turtle.forward(50)
turtle.right(90)
turtle.forward(45)
turtle.right(50)
turtle.forward(45)
turtle.home()
turtle.end_fill()
turtle.mainloop()
'''
turtle.register_shape("asd.gif")
turtle.shape("asd.gif")
dsa = 1
turtle.speed(100000000000)
for i in range(720):
	dsa = dsa + 1
	turtle.pendown()
	turtle.right(dsa)
	turtle.forward(200)
	
	turtle.right(55)

	turtle.forward(100)
	turtle.right(90)
	turtle.forward(90)
	turtle.penup()
	turtle.home()
turtle.mainloop()