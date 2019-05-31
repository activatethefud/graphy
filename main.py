from graphics import *
from random import *

def main():

	graph={}
	graph_win=GraphWin("Graph",200,200)
	graph_win.setBackground("white")

	input_file=open("input.txt","r");

	for line in input_file.readlines():
		line=line.rstrip('\n')
		graph[line.split(' ')[0]]=line.split(' ')[1::]

	node_points={}
	for vertex in graph.keys():
		pt=Point(randint(0,200),randint(0,200))

		label=Text(pt,str(vertex))
		label.draw(graph_win)

		node_points[vertex]=pt
	
	for vertex in graph.keys():
		
		for neighbour in graph[vertex]:
			edge=Line(node_points[vertex],node_points[neighbour])
			edge.draw(graph_win)
	
	graph_win.getMouse()
	print(graph)

	input_file.close()

main()
