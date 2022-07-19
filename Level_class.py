class Level(object):
    '''Level is a holder for screen objects'''
    def __init__(self, name) -> None:
        self.name = name
        self.itemList = []       # an initially empty list that contains all the items on the screen

    def addItem(self, item):
        self.itemList.append(item)

    def removeItem(self, item):
        self.itemList.remove(item)

    def reset(self):
        self.itemList = []

    def __str__(self) -> str:
        '''print(levelObject) prints list of objects in this level'''

        if self.itemList:       # if itemList is not empty
            rep = ''
            for item in self.itemList:
                rep += str(item) + ' '
        else:
            rep = '<empty>'
        return rep

    #def detectCollision(self, playerTop, playerBottom, playerLeft, playerRight):
    def detectCollision(self, player):
        # look for collisions between player and all other objects on screen
        #first reset all movement directions, then restrictions are additive
        player.resetMovementBlocks()
        # result is that allow movemenet attributes are set and reset
        for item in self.itemList:
            item.Collision(player)

            