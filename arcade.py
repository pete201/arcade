
from Door_class import Door
from Level_class import Level
from Floor_class import Floor
from Key_class import Key
from Player_class import Player


def main():
    # create a player object
    player1 = Player('s','x','z','c',100)   # (upKey, downKey, leftKey, rightKey, xPosn, yPosn)
    player1.setPosition(100,10)
    #player1.getPosition()

# update is simulating key presses since i'm not detecting them here
    player1.update(0,1,0,0)                 # (up, down, left right) move amount
    
    #lets create a level with some objects in it
    level0 = Level('intro')

    ### DONT ADD PLAYER AS IT WILL COLLIDE WITH ITSELF ###
    level0.addItem(Floor(100,100))      # notice that these objects have no name here - they are tracked via addItem() to array in level class
    level0.addItem(Floor(300,300))
    level0.addItem(Key(500,500,50,50))
    level0.addItem(Door(300,250,50,50))
    print(level0)


    print (f'UP = {player1.allowUP}, DOWN = {player1.allowDOWN}, LEFT = {player1.allowLEFT}, RIGHT = {player1.allowRIGHT}')


    level0.detectCollision(player1)

    print (f'UP = {player1.allowUP}, DOWN = {player1.allowDOWN}, LEFT = {player1.allowLEFT}, RIGHT = {player1.allowRIGHT}')  

    print('update player position to collide with floor')
    player1.setPosition(100,50)
    level0.detectCollision(player1)
    print (f'UP = {player1.allowUP}, DOWN = {player1.allowDOWN}, LEFT = {player1.allowLEFT}, RIGHT = {player1.allowRIGHT}')

    print ('player1.hasKey =',      player1.hasKey)
    print ('player1.doorOpen =',    player1.doorOpen)

    print('update player position to collide with door')
    player1.setPosition(300,250)
    level0.detectCollision(player1)
    print (f'UP = {player1.allowUP}, DOWN = {player1.allowDOWN}, LEFT = {player1.allowLEFT}, RIGHT = {player1.allowRIGHT}')
    print ('player1.hasKey =',      player1.hasKey)
    print ('player1.doorOpen =',    player1.doorOpen)

    print('update player position to collide with key')
    player1.setPosition(500,500)
    level0.detectCollision(player1)
    print (f'UP = {player1.allowUP}, DOWN = {player1.allowDOWN}, LEFT = {player1.allowLEFT}, RIGHT = {player1.allowRIGHT}')
    print ('player1.hasKey =',      player1.hasKey)
    print ('player1.doorOpen =',    player1.doorOpen)

    print('update player position to collide with door')
    player1.setPosition(300,250)
    level0.detectCollision(player1)
    print (f'UP = {player1.allowUP}, DOWN = {player1.allowDOWN}, LEFT = {player1.allowLEFT}, RIGHT = {player1.allowRIGHT}')
    print ('player1.hasKey =',      player1.hasKey)
    print ('player1.doorOpen =',    player1.doorOpen)

    


    print('done')












if __name__ == '__main__':
    main()