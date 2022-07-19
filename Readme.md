The 'level' class is a container that keeps track of all the objects on the screen for a given level

The 'Floor' class includes any obstacle on the screen, including floors
this class has a collision method that prevents movement of the player

the 'key' class is derived from 'floor' and has a collision method that adds a key to the player

the 'door' class is derived from 'floor' and has a collision method that completes the current level if the player has the key