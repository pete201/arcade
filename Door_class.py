from Floor_class import Floor


class Door(Floor):
    '''Door is in fixed position and updates player doorOpen attribute'''

    # Door class uses a different collision method, so override here
    def Collision(self, player):
        #print('Door.Collision: t,b,l,r = ',self.top, self.bottom, self.left, self.right)
        #print('Door.Collision: player at:',player.top, player.bottom, player.left, player.right)
        if player.top <= self.bottom and  player.bottom >= self.bottom and player.left <= self.right and player.right >= self.left:
            # we have a collision!
            if player.hasKey:  # doorOpen is TRUE if player.hasKey
                player.openDoor()
        if player.bottom >= self.top and player.top <= self.top and  player.left <= self.right and player.right >= self.left:
            # we have a collision!
            if player.hasKey:  # doorOpen is TRUE if player.hasKey
                player.openDoor()

        return