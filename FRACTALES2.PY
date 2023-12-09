import turtle
import time
import math
import random
import colorsys

class colorCounter:
	def __init__(self):
		self.r = 0
		self.g = 0
		self.b = 0
		self.stage = 'r'
		self.hue = 0
	def next_color(self,percent):
		self.hue += 1*percent
		self.hue % 1
		print(self.hue)
		return colorsys.hls_to_rgb(self.hue,0.5,0.5)
def fractal(depth, length,turt):
	if depth <= 0:
		turt.forward(length)
	else:
		fractal(depth-1,length/3,turt)
		turt.left(60)

		fractal(depth-1,length/3,turt)
		turt.right(120)

		fractal(depth-1,length/3,turt)
		turt.left(60)

		fractal(depth-1,length/3,turt)

def draw_fractal(steps,length, turt):
	for i in range(steps):
		my_win.clear()
		turt.speed(i*5)
		turt.up()
		turt.goto(-length/2)
		turt.down()
		fractal(i,length,turt)
		time.sleep(0.5)

def circle(turt, step,radius,centerx,centery, color_start, color_end, colorCount, percent):
	#print(hex(int(color_start)), " : " ,hex(int(color_end)))
	turt.speed(200)
	turt.resizemode('user')
	turt.shapesize(0.2,0.2,0.2)
	degree = 0
	turt.shape('circle')
	#color = colorCount.next_color(percent)
	#color = color_start
	#color_step = (color_end-color_start)/(360/step)
	while degree < 360:

		rad = math.radians(degree)
		x = (math.cos(rad) * radius) + centerx
		y = (math.sin(rad) * radius) + centery
		turt.up()
		turt.goto(x,y)
		turt.down()
		if radius < 15:
			color = colorCount.next_color(percent)
			#color = color_start
			color_step = (color_end-color_start)/(360/step)
			#turt.color('#' + hex(int(color) % 16777215)[2:].rjust(6,'0'))
			tempcol = (int(color[0] * 255), int(color[1] * 255), int(color[2]* 255))
			#print(tempcol)
			turt.color(tempcol)
			turt.stamp()

		else:
			#circle(turt,step, radius // 5, x,y,color, color + color_step, colorCount)
			circle(turt,step,radius//5,x,y,1,1,colorCount, percent * (step/360))
		degree += step
		#color += color_step


my_win = turtle.Screen()
my_win.colormode(255)
turt = turtle.Turtle()
turt.speed(20)
colorCount = colorCounter()
circle(turt,45,300,0,0,0,16777215, colorCount, 1 * (45/360)) 
my_win.mainloop()