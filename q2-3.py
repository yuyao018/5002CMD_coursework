# from udgraph import UDgraph

# define a Person class to represent a user in the social network
class Person:
    def __init__(self, name, gender, biography, privacy):
        # initialize the attributes of a person
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy # private or public

    def __repr__(self):
        return f"{self.name} ({self.gender}, {self.biography}, {self.privacy})"

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

    # store the user profiles in a list
    user_profiles = [sarah, wendy, jaden, alice, bob, clara, david, eva]

    # display all user profiles
    print("=========================User Profiles=========================")
    for user in user_profiles:
        print(user)