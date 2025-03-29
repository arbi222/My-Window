from turtle import *
import turtle
from random import randrange
from freegames import square , vector
from tkinter import *

def run_game():

	setup(420 , 420 , 370 , 200)
	title('Snake')
	root = Screen()._root
	root.iconbitmap("snake.ico")
	root.resizable(False, False)
	hideturtle()
	tracer(False)
	listen()

	points = turtle.Turtle()
	points.color('black')
	points.penup()
	points.left(180)
	points.forward(200)
	points.right(90)
	points.forward(182)
	points.pendown()
	points.hideturtle()

	points.write("Score: 0" , font=("Arial", 15, "normal"))
	
	def close():
		bye()	
   
	root.protocol("WM_DELETE_WINDOW", close)
    	
    	 

	food = vector(0,0)
	snake = [vector(10,0)]
	aim = vector(0, -10)
	def change(x,y):
		# "change snake direction"
		aim.x = x
		aim.y = y
	
	def inside(head):
		# return true if head is inside boundaries
		return -200 < head.x < 190 and -200 < head.y < 190
	
	def move():
		head = snake[-1].copy()
		head.move(aim)
	
		if not inside(head) or head in snake:
			square(head.x , head.y , 9 , 'green')
			update()
			return
	
		snake.append(head)
		
		if head == food:
			score_points = len(snake) - 1
			points.clear()
			points.write("Score: " + str(score_points) , font=("Arial", 15, "normal"))
			#print('Score: ', len(snake))
			food.x = randrange(-15 , 15) * 10
			food.y = randrange(-15 , 15) * 10
		else:
			snake.pop(0)
			clear()
	
		for body in snake:
			square(body.x, body.y , 9 , 'black')
	
		square(food.x , food.y , 9 , 'red')
		update()
		ontimer(move , 90)
	
	
	
	
	onkey(lambda:change(10,0), 'Right')
	onkey(lambda:change(-10,0), 'Left')
	onkey(lambda:change(0,10), 'Up')	
	onkey(lambda:change(0,-10), 'Down')
		
	move()
	done()				
