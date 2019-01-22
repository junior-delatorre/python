# plot-dictionary.py
import tkinter as tk 
import turtle 

def main():
	#table is a dictionary 
	table = {-112:3,-92:5,-85:21,-79:12,-6:56,-50:62,
				-40:5,-30:69,-20:23,-10:10,0:0,
					10:2,20:67,30:32,40:20,50:60,
					60:9,70:89,80:65,90:50,100:90
			}
	print(" KEYS ")
	print(table.keys())
	print(" VALUES ")
	print(table.values())
	#turtle graphics
	twin = turtle.Screen()
	twin.clear()
	t = turtle.Turtle()
	#tWin = turtle.Screen()
	for h,k in table.items():  #get the items in the dictionary 
		print(h, k) # trace code 
		#x,y = table[n]
		t.penup()
		t.goto(h,k)
		t.pendown()
		t.circles(5)
		t.speed()
	twin.extionclick()

main()


