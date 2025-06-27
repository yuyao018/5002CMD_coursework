from typing import TypeVar, Generic, Dict, Set #creation of generic types

T = TypeVar('T')
"""
THIS IS THE SAMPLE IMPLEMENTATION OF GENERTIC
def echo(value: T) -> T: # pattern of accepting a generic parameter
    return value

print(echo(42))
print(echo("Hello"))
"""
class UDgraph(Generic[T]):
    def __init__(self):
        self.graph: Dict[T, Set[T]] = {}

    def add_vertex(self, vertex: T) -> None:
        if vertex not in self.graph:
            self.graph[vertex] = set()

    def add_edge(self, start: T, end: T) -> None:
        if start in self.graph and end in self.graph:
            self.graph[start].add(end)
        else:
            print("One or both vertices not found.")

    def remove_edge(self, start: T, end: T) -> None:
        if start in self.graph and end in self.graph:
            self.graph[start].remove(end)
        else:
            print("One or both vertices not found.")

    def list_out_going_adjacent_vertex(self, vertex: T) -> list[T]:
        return list(self.graph.get(vertex, []))

if __name__ == "__main__":
    g = UDgraph[str]()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")
    g.add_edge("C", "B")

    print("A ->", g.list_out_going_adjacent_vertex("A"))
    print("B ->", g.list_out_going_adjacent_vertex("B"))
    print("C ->", g.list_out_going_adjacent_vertex("C"))