#from arcade.class_player import Player



class Floor(object):
    '''create a floor and supply its x and y coordinates'''
    def __init__(self, xPosn, yPosn, width=50, height=50) -> None:
        # default variables
        self.height = height
        self.width  = width
        #input variables
        self.xPosn = xPosn
        self.yPosn = yPosn
        self.top = self.yPosn
        self.bottom = self.yPosn + self.height
        self.left = self.xPosn
        self.right = self.xPosn + self.width

    def Collision(self, player):
        '''compares player positin with self position and set/reset collision status'''
        # set movemnet True or False to each of the collision possibilities: TRUE = movement is allowed, FALSE = movement blocked by collision
        # these are TRUE upon collision
        #print('Floor.Collision: t,b,l,r = ',self.top, self.bottom, self.left, self.right)
        #print('Floor.Collision: player at:',player.top, player.bottom, player.left, player.right)
        blockUP = player.top <= self.bottom and  player.bottom >= self.bottom and player.left < self.right and player.right > self.left
        blockDOWN = player.bottom >= self.top and player.top <= self.top and player.left < self.right and player.right > self.left
        blockLEFT = player.left <= self.right and player.right >= self.right and player.top < self.bottom and player.bottom > self.top
        blockRIGHT = player.right >= self.left and player.left <= self.left and player.top < self.bottom and player.bottom > self.top
        player.allowMove(blockUP, blockDOWN, blockLEFT, blockRIGHT) # this is instance of player, not the class
