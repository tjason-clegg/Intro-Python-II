# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.list = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        return f"Room: {self.name} {self.description}"

    def add_items(self, item):
        self.list.append(item)

    def drop_item(self, item):
        self.list.remove(item)
        return f"You dropped {item}! It has been removed from your inventory."

    # def getItems(self):
    #     return f"Name: {self.name}, Description: {self.description}, Items: {self.list}"

    def print_items(self):
        if len(self.list) == 0:
            print("No item in the room")
        else:
            for item in self.list:
                print(item, "Is in your inventory")
