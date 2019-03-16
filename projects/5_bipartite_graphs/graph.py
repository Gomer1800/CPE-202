from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key           # string of key, like v1, v2
        self.adjacent_to = []   # list of edges from self
        self.color = 0

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''
        reads in the specification of a graph and creates a graph using an adjacency list representation.    
        You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
        represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
        in the input file should appear on the adjacency list of each vertex of the two vertices associated 
        with the edge.
        '''
        self.vertex_list = dict()
        self.num_vertices = 0

        try:
            key_val_pairs = []
            # Open file and read lines
            with open(filename, 'r') as file_object:
                line_list = file_object.readlines()
                # populate vertex list
                for line in line_list:
                    key_val = line.split()
                    key_val_pairs.append(key_val)
                    #print(key_val)
                    self.add_vertex(key_val[0])     # add vertex if able
                    self.add_vertex(key_val[1])     # add vertex if able

                #print(self.vertex_list.keys())
                for pairs in key_val_pairs:         # add edge if able
                    self.add_edge(pairs[0], pairs[1])

        except FileNotFoundError:
            raise FileNotFoundError("Graph()")

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        try:
            new_vertex = Vertex(key)

            if key not in self.vertex_list: # Valid Case, unique key
                self.vertex_list[key] = new_vertex
                self.num_vertices += 1
        except ValueError:
            raise ValueError("add_vertex(): ", key)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None''' 
        if key in self.vertex_list:         # Check is key is in vertex list
            return self.vertex_list[key]
        else:
            return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph
        '''
        try:
            v1_adj_verts = self.vertex_list[v1].adjacent_to
            v2_adj_verts = self.vertex_list[v2].adjacent_to
            if v2 not in v1_adj_verts:
                v1_adj_verts.append(v2)
                #print(v1,": ",v1_adj_verts)
            if v1 not in v2_adj_verts:
                v2_adj_verts.append(v1)
                #print(v2,": ",v2_adj_verts)
                
        except ValueError:
            raise ValueError("add_edge(): ", v1, v2)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        try:
            keys = sorted(self.vertex_list.keys())
            #print("keys :", keys)
            return keys
        except Exception:
            raise Exception("get_vertices()\ncurrent list: ",self.vertex_list,"\nnum items: ",self.num_items)

    def conn_components(self): 
        '''
        Returns a list of lists.  For example, if there are three connected components 
        then you will return a list of three lists.  Each sub list will contain the 
        vertices (in ascending order) in the connected component represented by that list.
        The overall list will also be in ascending order based on the first item of each sublist.
        This method MUST use Depth First Search logic
        '''
        unvisited = self.get_vertices()             # unvisited vertices
        #print("unvisited vertices: ", unvisited)
        visited = []                                # visited vertices
        my_stack = Stack(len(unvisited))
        i = 0                                       # sub graph counter

        # while there are unvisited vertices
        while len(unvisited) != 0:
            # intitialize source key
            current_key = unvisited.pop(0)
            # append source key to visited list i
            visited.append([current_key])
            # push source key to stack
            my_stack.push(current_key)

            # stack may contain same vertex twice
            # check if vertex has been visited
            while my_stack.is_empty() is False:
                current_key = my_stack.pop()                            # pop stack

                if current_key not in visited[i]:                       # check if visited
                    visited[i].append(current_key)
                    #print(current_key," added to visited: ", visited)

                # Get all adjacent vertices of the poppped vertex
                # if adjacent vertex is unvisited, push to stack
                adj_to = self.vertex_list[current_key].adjacent_to
                #print(current_key," adjacent to: ", adj_to)
                for adj in adj_to[::-1]:                                # iterate in reverse
                    if adj in unvisited:
                        unvisited.remove(adj)
                        my_stack.push(adj)
                        #print(adj," removed from unvisited: " ,unvisited)

            visited[i] = sorted(visited[i])                             # sorted list
            i += 1  # add new sub graph

        #print(i," sub graphs: ", visited)
        return visited

    def is_bipartite(self):
        '''
        Returns True if the graph is bicolorable and False otherwise.
        This method MUST use Breadth First Search logic!
        '''
        unvisited = self.get_vertices()
        visited = []
        my_q = Queue(len(unvisited))
        i = 0                                  # sub graph counter

        while len(unvisited) != 0:
            # initialize source vertex and color
            current_key = unvisited.pop(0)
            self.vertex_list[current_key].color = 1
            visited.append( [current_key] )
            my_q.enqueue(current_key)
            
            # stack may contain same vertex twice
            # check if vertex has been visited
            while my_q.is_empty() is False:
                #print("Queue :", my_q.get_items())
                current_key = my_q.dequeue()
                current_vertex = self.vertex_list[current_key]

                if current_key not in visited[i]:                       # check if visited
                    visited[i].append(current_key)
                    #print(current_key," added to visited: ", visited)
                
                # Get all adjacent vertices of the poppped vertex
                # if adjacent vertex is unvisited, enqueue
                adj_to = self.vertex_list[current_key].adjacent_to
                #print(current_key," adjacent to: ", adj_to)
                for adj in adj_to:
                    adj_vertex = self.vertex_list[adj]

                    #print(current_key," color: ", current_vertex.color, adj," color: ,",adj_vertex.color)
                    if adj_vertex.color == 0:
                        adj_vertex.color = -current_vertex.color
                    if adj_vertex.color == current_vertex.color:
                        return False
                    #print(current_key," color: ", current_vertex.color, adj,"  color: ,",adj_vertex.color)
                    
                    if adj in unvisited:
                        unvisited.remove(adj)
                        #print(adj," removed from unvisited: ", unvisited)
                        # check color of adj vertex, assign if default
                        my_q.enqueue(adj)

            visited[i] = sorted(visited[i])                             # sorted list
            i += 1  # add new sub graph

        #print(i," sub graphs: ", visited)
        return True

