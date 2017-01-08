import sys
from Queue import Queue

infinity = 999999 

class Vertex(object):
	def __init__(self,id):
		self.id=id
		self.parent = None
		self.color = "white"
		self.distance = infinity

	def print_object():
		pass
		# to print instance properties

#to add compatability for directed and undirected
class Graph(object):
	def __init__(self):
		self.adj_list=dict(list())
		self.vertices = dict()

	def add_edge(self,v1,v2):
		if self.vertices.has_key(v1)==False:
			self.vertices[v1]=Vertex(v1)
		if self.vertices.has_key(v2)==False:
			self.vertices[v2]=Vertex(v2)
		
		if self.adj_list.has_key(v1):
			self.adj_list[v1].append(v2)
		else:
			self.adj_list[v1]=[v2]
		if self.adj_list.has_key(v2):								#for undirected graph
			self.adj_list[v2].append(v1)
		else:
			self.adj_list[v2]=[v1]

	def print_graph(self):  
		'''
		for vertex,list in self.adj_list.iteritems():
				print str(vertex)+":",
				for ele in list:
					print str(ele.id)+",",
				print "\n"
		'''

	def BFS(self,source_id):
		source = self.vertices[source_id]
		source.color = "grey"
		source.distance = 0

		q = Queue()
		q.put(source)
		while not q.empty():
			v = q.get()
			for vertex in self.adj_list[v.id]:
				u = self.vertices[vertex]   #added
				if u.color == "white":
					u.color = "grey"
					u.distance = v.distance+1
					u.parent = v.id
					q.put(u)
			v.color = "black"
			
			

	def print_result(self):
		for vertice in self.vertices:
			print "id: ",self.vertices[vertice].id ,
			print " color:", self.vertices[vertice].color ,
			print " distance:",self.vertices[vertice].distance ,
			print " parent: ",self.vertices[vertice].parent 






graph = Graph()

graph.add_edge(1,2)
graph.add_edge(1,5)
graph.add_edge(2,6)
graph.add_edge(3,4)
graph.add_edge(3,7)
graph.add_edge(3,6)
graph.add_edge(4,8)
graph.add_edge(6,7)
graph.add_edge(7,8)

graph.print_graph()

graph.BFS(2)

graph.print_result()



