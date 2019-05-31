from graphics import *
from random import *
from time import sleep
import math
import sys

node_count=0

def generate_circle_coord(center,radius,node_count,node_number):
	''' Generate node coordinates to fit on the same circle
	adding equal fractions from 0 '''
	t=(2*math.pi/node_count)*float(node_number)
	''' Parameter circle equation ''' 
	x=center+radius*math.sin(t)
	y=center+radius*math.cos(t)
	return (x,y)

def main():

	''' Define the graphical window height and weight.
	All other parameters are relative to these. '''
	width=400
	height=400
	# Initiliaze the graph and graphical window
	graph={}
	graph_win=GraphWin("Graph",width,height)
	graph_win.setBackground("white")

	input_file=open("input.txt","r");

	# Input the graph from a text file
	for line in input_file.readlines():
		line=line.rstrip('\n')
		graph[line.split(' ')[0]]=line.split(' ')[1::]
		global node_count
		node_count+=1

	# Radius in which all nodes will be in (in px)
	circle_radius=width*0.75/2

	# The shift of node label from node center
	label_shift=7

	# Draw all nodes inputted
	node_points={}
	for vertex in graph.keys():
		# Skip vertices already drawn
		if vertex not in node_points.keys():
			coords=generate_circle_coord(width/2,circle_radius,node_count,vertex)
			pt=Point(coords[0],coords[1])

			''' Shift the node labels 1,2,3...n to the side for 
			aesthetics, depending on the halve it's on'''
			if coords[0] < width/2:
				lpt=Point(coords[0]-label_shift,coords[1])
			else:
				lpt=Point(coords[0]+label_shift,coords[1])

			label=Text(lpt,str(vertex))
			label.draw(graph_win)

			node_points[vertex]=pt
		else:
			continue
		
		for neighbour in graph[vertex]:
			# Skip neighbouring vertices already drawn
			if neighbour not in node_points.keys():
				coords=generate_circle_coord(width/2,circle_radius,node_count,neighbour)
				pt=Point(coords[0],coords[1])

				if coords[0] < width/2:
					lpt=Point(coords[0]-label_shift,coords[1])
				else:
					lpt=Point(coords[0]+label_shift,coords[1])
					
				label=Text(lpt,str(neighbour))
				label.draw(graph_win)

				node_points[neighbour]=pt
	
	# Draw the edges, skip edges already drawn
	edges=[]
	visited=[]
	for vertex in graph.keys():
		
		if vertex not in visited:
			visited.append(vertex)
		
		for neighbour in graph[vertex]:
			if neighbour not in visited:
				edge=Line(node_points[vertex],node_points[neighbour])
				''' This is an optional argument, to draw edges in real time
				one by one, use only for entertainment ;D '''
				len(sys.argv) != 1 and sleep(int(sys.argv[1]))
				edge.draw(graph_win)
	
	# Pause the graphical window, awaiting mouse input

	graph_win.getMouse()
	input_file.close()

main()
