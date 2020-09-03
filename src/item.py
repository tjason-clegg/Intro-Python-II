class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.list = []

    def __str__(self):
        return f"{self.name}: {self.description}"
