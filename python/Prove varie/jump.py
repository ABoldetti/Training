import pygame
groundy=0


class Player:
    def __init__ (self, hp, weight, power, flyingspeed, x,y,  isjumping=True, isfalling=False):
        self.hp=hp
        self.x=x
        self.y=y
        self.weight=weight
        self.power=power
        self.flyingspeed=flyingspeed

    
    def inertia(self):
        self.x+=self.flyingspeed
    
    def jump(self):
        
        self.y+=self.power
        self.power-=self.weight
        Player.inertia()
        if( self.y ==groundy): 
            self.weight=0
            self.power=0



if( event.key == pygame.K_SPACE): Player.jump()