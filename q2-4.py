from udgraph import UDgraph
from person import Person

if __name__ == "__main__":
    # create several user profiles
    sarah = Person("Sarah", "female", "Loves music", "private")
    wendy = Person("wendy", "female", "Loves fashion", "public")
    jaden = Person("Jaden", "male", "All Time Gamer", "public")
    alice = Person("Alice", "female", "Photographer and traveler", "public")
    bob = Person("Bob", "male", "Coffee lover and tech enthusiast", "private")
    clara = Person("Clara", "female", "Bookworm and writer", "public")
    david = Person("David", "male", "Fitness coach and nutritionist", "public")
    eva = Person("Eva", "female", "Music teacher and pianist", "private")

    # create a unweighted directed social graph with Person as the vertex type
    social_graph = UDgraph[Person]()

    # add the user profiles as vertices in the graph
    social_graph.add_vertex(sarah)
    social_graph.add_vertex(wendy)
    social_graph.add_vertex(jaden)
    social_graph.add_vertex(alice)
    social_graph.add_vertex(bob)
    social_graph.add_vertex(clara)
    social_graph.add_vertex(david)
    social_graph.add_vertex(eva)

    # add directed edges to represent users following relationships
    social_graph.add_edge(sarah, wendy)
    social_graph.add_edge(wendy, sarah)
    social_graph.add_edge(jaden, sarah)
    social_graph.add_edge(david, wendy)
    social_graph.add_edge(sarah, alice)
    social_graph.add_edge(wendy, david)
    social_graph.add_edge(jaden, david)
    social_graph.add_edge(eva, wendy)
    social_graph.add_edge(clara, alice)
    social_graph.add_edge(bob, david)
    social_graph.add_edge(alice, david)
    social_graph.add_edge(eva, wendy)

    # store all user profiles in a list
    user_profiles = [sarah, wendy, jaden, alice, bob, clara, david, eva]

    # display who is following who
    print("=========================Instagram Following=========================")
    for user in user_profiles:
        following = social_graph.list_out_going_adjacent_vertex(user)
        print(f"{user.name} follows: {[f.name for f in following]}")