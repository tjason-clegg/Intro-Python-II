# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.list = []

    def __str__(self):
        return f"Player: '{self.name}' '{self.current_room}'"

    def add_item(self, item):
        self.list.append(item)
        return f"You picked up {item}! It has been added to your inventory."

    def movement(self, direction):
        val = getattr(self.current_room, direction)
        if val != None:
            self.current_room = getattr(self.current_room, direction)

    def drop_item(self, item):
        self.list.remove(item)
        return f"You dropped {item}! It has been removed from your inventory."

    def print_items(self):
        if len(self.list) == 0:
            print("No item in the room")
        else:
            for item in self.list:
                print(item, "Is in your inventory")
