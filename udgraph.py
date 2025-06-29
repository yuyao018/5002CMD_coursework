from typing import TypeVar, Generic, Dict, Set #creation of generic types

# define a generic type variable T for vertex data type
T = TypeVar('T')

"""
THIS IS THE SAMPLE IMPLEMENTATION OF GENERTIC
def echo(value: T) -> T: # pattern of accepting a generic parameter
    return value

print(echo(42))
print(echo("Hello"))
"""

# define generic class for the unweighted directed graph
class UDgraph(Generic[T]):
    def __init__(self):
        self.graph: Dict[T, Set[T]] = {}

    def add_vertex(self, vertex: T) -> None:
        # function to add a vertex to the graph

        # check if the vertex is present in the graph or not. If no, add vertex to graph.
        if vertex not in self.graph:
            self.graph[vertex] = set()

    def add_edge(self, start: T, end: T) -> None:
        # function to add a directed edge from 'start' vertex to 'end' vertex

        # check if both vertices exist in the graph before adding the edge
        if start in self.graph and end in self.graph:
            self.graph[start].add(end) # add the edge from start to end
        else:
            print("One or both vertices not found.") # display error message if either one vertex doesn't exists

    def remove_edge(self, start: T, end: T) -> None:
        # function to remove a directed edge from 'start' vertex to 'end' vertex

        # check if both vertices exist in the graph before removing the edge
        if start in self.graph and end in self.graph:
            self.graph[start].remove(end) # remove the edge from start to end
        else:
            print("One or both vertices not found.") # display error message if either one vertex doesn't exists

    def list_out_going_adjacent_vertex(self, vertex: T) -> list[T]:
        # Function to list all outgoing adjacent vertices for a given vertex
        return list(self.graph.get(vertex, []))
