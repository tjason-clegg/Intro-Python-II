from room import Room
from item import Item
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Castle Entrance:",
                     "North of you, the castle beckons. You see a cross sitting on the marble staircase"),

    'foyer':    Room("Foyer:", """Dim light filters in from outside towards the south. On each side of this massive foyer lie old but nicley maintained doors. Opening them, you see that they lead to dusty
passages running north and east. While looking around, you see and smell a succulent looking turkey, sitting on the table, as if to welcome you."""),

    'overlook': Room("Grand Overlook:", """You decide to head north. As you reach the end of the hallway, you find that it leads to an overlook. You look down and see a steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. You barley manage to catch a glimpse some lightly permeable fabric whipping in the intense wind"""),

    'narrow':   Room("Narrow Passage:", """You decide to head East. As you approach this passage you notice that its more narrow then you aticipated. As you traverse this narrow passage, you come to a split, it bends here from west
to north. The smell of death and decay permeates the air. You see some new leather that you may be able to fix your whip with."""),

    'torture':   Room("Torture Chamber:", """You decide to go north. Coming to the end of this passage, it opens up into a dim, small room. One of the first you realise is the lack of decor compared to the foyer you entered the passage through, its obvious whoever this place belonged to wasn't excpecting their guests to come down here. All there is in this room is an old man, helplessly chained to the wall. The only exit is to the south. A crown is sitting on the ground, glinting what little light is filtering in the room from barred windows."""),
}

# List of Items
items = {
    'cross': Item("Cross", "Clears room of all enemies."),
    'turkey': Item("Turkey", "Replenishes a good amount of HP."),
    'invisibility': Item("Invisibility", "Makes you immune to attacks for 30 seconds."),
    'power_up_whip': Item("Power Up Whip", "Powers the whip up by one level."),
    'crown': Item("Crown", "A sparkling crown of kings long gone."),

}

# List items to rooms

room['outside'].add_items(items['cross'])
room['foyer'].add_items(items['turkey'])
room['overlook'].add_items(items['invisibility'])
room['narrow'].add_items(items['power_up_whip'])
room['torture'].add_items(items['crown'])

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['torture']
room['torture'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

new_player = Player("Trevor Belmont", room["outside"])

# Write a loop that:

welcome_message = f'What would you like to do? \n \nPress m to move \n \nPress i for inventory \n \nPress q to quit'

command = input(welcome_message)


move_message = f'Choose a direction \n \nPress n for North \n \nPress e for East \n \nPress s for South \n \nPress w for West \n \nPress m for Main Menu \n \nPress q to Quit'

while command != 'q':

    while command == 'm':

        move2 = input(move_message)
        move_choice = f"{move2.lower()}_to"
        print(new_player)

        if move2 == "q":
            exit()
        elif move2 == "i":
            command = "i"
        else:
            new_player.movement(move_choice)

    while command == 'i':

        inventory_message = f'Choose what to do with your items\nType "take" to take an item\nType "drop" to drop an item\nPress q to leave this screen'

        new_player.current_room.print_items()
        new_player.print_items()
        i_command = input(inventory_message)

        action = i_command.split()[0].lower()
        item = i_command.split()[1].lower()

        if action == "q" and item == "m":
            command = input(welcome_message)

        if action == 'take':
            for i in new_player.current_room.list:
                if i.name.lower() == item:
                    new_player.add_item(i)
                    new_player.current_room.drop_item(i)

        if action == 'drop':
            for i in new_player.current_room.list:
                if i.name.lower() == item:
                    new_player.current_room.take_items(i)
                    new_player.drop_item(i)
        # * Prints the current room name
        # * Prints the current description (the textwrap module might be useful here).
        # * Waits for user input and decides what to do.
        #
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        #
        # If the user enters "q", quit the game.
