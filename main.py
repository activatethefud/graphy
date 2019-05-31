from graphics import *
from random import *
import sys

def main():

	# Initiliaze the grap and graphical window
	graph={}
	graph_win=GraphWin("Graph",200,200)
	graph_win.setBackground("white")

	input_file=open("input.txt","r");

	# Input the graph from a text file
	for line in input_file.readlines():
		line=line.rstrip('\n')
		graph[line.split(' ')[0]]=line.split(' ')[1::]

	# Draw all nodes inputted (TODO)
	node_points={}
	for vertex in graph.keys():
		if vertex not in node_points.keys():
			pt=Point(randint(0,200),randint(0,200))
			label=Text(pt,str(vertex))
			label.draw(graph_win)
			node_points[vertex]=pt
		
		for neighbour in graph[vertex]:
			if neighbour not in node_points.keys():
				pt=Point(randint(0,200),randint(0,200))
				label=Text(pt,str(neighbour))
				label.draw(graph_win)
				node_points[neighbour]=pt
	
	# Draw the edges
	for vertex in graph.keys():
		
		for neighbour in graph[vertex]:
			edge=Line(node_points[vertex],node_points[neighbour])
			edge.draw(graph_win)
	
	# Pause the graphical window, awaiting mouse input
	graph_win.getMouse()
	print(graph)

	input_file.close()

main()
