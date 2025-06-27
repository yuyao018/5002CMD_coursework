from udgraph import UDgraph

# define a class to represent a person in the social graph
class Person:
    def __init__(self, name, gender, biography, privacy):
        # initialize the person's attributes
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy # private or public

    def __repr__(self):
        # return a readable string of the person's information
        return f"{self.name} ({self.gender}, {self.biography}, {self.privacy})"

if __name__ == "__main__":
    # create instances of Person
    sarah = Person("Sarah", "female", "Loves music", "private")
    wendy = Person("wendy", "female", "Loves fashion", "public")
    jaden = Person("Jaden", "male", "All Time Gamer", "public")

    # create a unweighted directed social graph with Person as the vertex type
    social_graph = UDgraph[Person]()

    # add people to the graph as vertices
    social_graph.add_vertex(sarah)
    social_graph.add_vertex(wendy)
    social_graph.add_vertex(jaden)

    # add directed edges to the graph to represent who follows who
    social_graph.add_edge(sarah, wendy)
    social_graph.add_edge(wendy, sarah)
    social_graph.add_edge(jaden, sarah)
    social_graph.add_edge(jaden, wendy)

    # print out each person's followings
    print("=========================Social Connection=========================")
    print("Sarah follows: ", social_graph.list_out_going_adjacent_vertex(sarah))
    print("Wendy follows: ", social_graph.list_out_going_adjacent_vertex(wendy))
    print("Jaden follows: ", social_graph.list_out_going_adjacent_vertex(jaden))