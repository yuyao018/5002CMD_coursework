from typing import TypeVar, Generic, Dict, Set #creation of generic types

# define a generic type variable T for vertex data type
T = TypeVar('T')

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


    def list_out_going_adjacent_vertex(self, vertex: T) -> list[T]:
        return list(self.graph.get(vertex, []))

if __name__ == "__main__":
    g = UDgraph[T]() # create a graph variable 'g' with generic data type

    # add vertices to the graph
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")

    # add directed edges between vertices
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")
    g.add_edge("C", "B")

    # print the adjacent list for each vertex
    print("A ->", g.list_out_going_adjacent_vertex("A"))
    print("B ->", g.list_out_going_adjacent_vertex("B"))
    print("C ->", g.list_out_going_adjacent_vertex("C"))