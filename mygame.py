import pygame
import random

class Character():
    speed = 3
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def moveRight(self):
        self.x += speed
    
    def moveLeft(self):
        self.x -= speed
    
    def moveUp(self):
        self.y -= speed
        
    def moveDown(self):
        self.y += speed

class Monster(Character):
    speed = 3
    def __init__(self):
        self.x = 60
        self.y = 400
        self.name = 'monster'
        

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
    monster = Monster()

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
        
        if(direction == 1): #go right
            monster.moveRight()
        elif(direction == 2): #go left
            monster.moveLeft()
        elif(direction == 3): #go up
            monster.moveUp()
        elif(direction == 4): #go down
            monsterY.moveDown()
            
        # screen wrapping logic
        if(monsterX > 512):
            monsterX = 0
        elif monsterX < -30:
            monsterX = 512
        if(monsterY > 480):
            monsterY = 0
        elif(monsterY < -32):
            monsterY = 480
        
        
        # Draw background
        screen.fill(blue_color)
        # Game display
        screen.blit(background_image,(0,0))
        screen.blit(hero_image, (200,200))
        screen.blit(monster_image, (monsterX,monsterY))
        pygame.display.update()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
