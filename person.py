class Person:
    def __init__(self, name, gender, biography, privacy):
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy # private or public

    def __repr__(self):
        return f"{self.name} ({self.gender}, {self.biography}, {self.privacy})"

    def get_name(self):
        return self.name