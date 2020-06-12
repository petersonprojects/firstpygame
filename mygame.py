import pygame
import random
speed = 3

# class Character():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    


class Monster():
    def __init__(self,startx,starty):
        self.x = startx
        self.y = starty
        self.name = 'monster'
    
    def moveRight(self):
        self.x += speed
    
    def moveLeft(self):
        self.x -= speed
    
    def moveUp(self):
        self.y -= speed
        
    def moveDown(self):
        self.y += speed

    def getWrap(self):
        if(self.x > 512):
            self.x = 0

        if(self.x < -30):
            self.x = 512

        if(self.y > 480):
            self.y = 0

        if(self.y < -32):
            self.y = 480

def main():
    # Game initialization
    
    width = 512
    height = 480
    blue_color = (97, 159, 182)
    change_dir = 120

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    
    #image loading
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha() #30x32
    
    clock = pygame.time.Clock()
    #initialize monster
    monster = Monster(60, 400)
    direction = 0

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        # direction changing logic

        change_dir -= 1
        if(change_dir <= 0):
            change_dir = 120
            direction = random.randint(1,4)
        
        if(direction == 1):
            monster.moveRight()
        elif(direction == 2):
            monster.moveLeft()
        elif(direction == 3):
            monster.moveUp()
        elif(direction == 4):
            monster.moveDown()
        # screen wrapping logic
        monster.getWrap()
        
        
        # Draw background
        screen.blit(background_image,(0,0))
        # Game display

        screen.blit(hero_image, (200,200))
        screen.blit(monster_image, (monster.x,monster.y))
        pygame.display.update()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
