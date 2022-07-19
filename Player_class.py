class Player(object):
    '''creates player with associated move keys and x,y, positions'''
    # class variables go here

    def __init__(self, UPkey, DOWNkey, LEFTkey, RIGHTkey, xPosn=0, yPosn=0) -> None:
        # default variables
        self.height = 50
        self.width  = 50
        self.hasKey = False
        self.doorOpen = False
        #input variables
        self.UPkey    = UPkey
        self.DOWNkey  = DOWNkey
        self.LEFTkey  = LEFTkey
        self.RIGHTkey = RIGHTkey
        self.resetMovementBlocks()
        self.setPosition(xPosn, yPosn)      # this sets top, bottom, left and right as well as x,y

        print('a player has been created :)')
        

    # def getPosition(self):
    #     #print('Player position is:',self.xPosn, self.yPosn)
    #     return self.top, self.bottom, self.left, self.right


    def setPosition(self, x, y):
        self.xPosn = x
        self.yPosn = y
        # top, bottom, left and right are needed for collision detection
        self.top = self.yPosn
        self.bottom = self.yPosn + self.height
        self.left = self.xPosn
        self.right = self.xPosn + self.width

    def resetMovementBlocks(self):
        '''removes any inhibits on player motion'''
        self.allowUP    = True
        self.allowDOWN  = True
        self.allowLEFT  = True
        self.allowRIGHT = True

    def allowMove(self, blockUP, blockDOWN, blockLEFT, blockRIGHT):
        '''movement direction is blocked by colliding object'''
        # a block = TRUE is NANDed with status so blocks add up
        self.allowUP    = self.allowUP and (not blockUP)
        self.allowDOWN  = self.allowDOWN and (not blockDOWN)
        self.allowLEFT  = self.allowLEFT and (not blockLEFT)
        self.allowRIGHT = self.allowRIGHT and (not blockRIGHT)

    def getKey(self):
        self.hasKey = True

    def dropKey(self):
        self.hasKey = False

    def openDoor(self):
        self.doorOpen = True

    def newDoor(self):
        self.doorOpen = False


    def update(self, up=0, down=0, left=0, right=0):
        '''override default values to make player move'''
        newX = self.xPosn
        newY = self.yPosn

        if self.allowUP:
            newY = self.yPosn - up
        if self.allowDOWN:
            newY = self.yPosn + down
        if self.allowLEFT:
            newX = self.xPosn - left
        if self.allowRIGHT:
            newX = self.xPosn + right
        
        self.setPosition(newX, newY)



