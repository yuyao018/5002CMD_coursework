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

    def get_name(self):
        # return the person's name
        return self.name