from Floor_class import Floor


class Key(Floor):
    '''Key is in fixed position and updates player has_key attribute'''

    # Key class uses a different collision method, so override here
    def Collision(self, player):
        #print('Key.Collision: t,b,l,r = ',self.top, self.bottom, self.left, self.right)
        #print('Key.Collision: player at:',player.top, player.bottom, player.left, player.right)
        if player.top <= self.bottom and  player.bottom >= self.bottom and player.left <= self.right and player.right >= self.left:
            # we have a collision!
            player.getKey()
        if player.bottom >= self.top and player.top <= self.top and player.left <= self.right and player.right >= self.left:
            # we have a collision!
            player.getKey()
        return