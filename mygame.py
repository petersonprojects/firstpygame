import pygame
import random
mSpeed = 2
gSpeed = 1
hSpeed = 3
# class Character():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
class Hero():
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
        self.name = 'hero'

    def moveRight(self):
        self.x += hSpeed
    
    def moveLeft(self):
        self.x -= hSpeed
    
    def moveUp(self):
        self.y -= hSpeed
        
    def moveDown(self):
        self.y += hSpeed

class Monster():
    def __init__(self,startx,starty):
        self.x = startx
        self.y = starty
        self.name = 'monster'
    
    def moveRight(self):
        self.x += mSpeed
    
    def moveLeft(self):
        self.x -= mSpeed
    
    def moveUp(self):
        self.y -= mSpeed
        
    def moveDown(self):
        self.y += mSpeed

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
    background_image = pygame.image.load('images/background.png').convert_alpha() #512x480
    hero_image = pygame.image.load('images/hero.png').convert_alpha() #32x32
    monster_image = pygame.image.load('images/monster.png').convert_alpha() #30x32
    
    clock = pygame.time.Clock()
    #initialize monster, hero and goblins
    monster = Monster(60, 400)
    hero = Hero(200,200)
    direction = 0
    pressed_left = False
    pressed_right = False
    pressed_up = False
    pressed_down = False
    stop_game = False
    
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP  or event.key == pygame.K_w:
                    pressed_up = True

                if event.key == pygame.K_DOWN  or event.key == pygame.K_s:
                    pressed_down = True

                if event.key == pygame.K_LEFT  or event.key == pygame.K_a:
                    pressed_left = True

                if event.key == pygame.K_RIGHT  or event.key == pygame.K_d:
                    pressed_right = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP  or event.key == pygame.K_w:
                    pressed_up = False

                if event.key == pygame.K_DOWN  or event.key == pygame.K_s:
                    pressed_down = False

                if event.key == pygame.K_LEFT  or event.key == pygame.K_a:
                    pressed_left = False

                if event.key == pygame.K_RIGHT  or event.key == pygame.K_d:
                    pressed_right = False
                
        # Game logic
        # direction changing logic
        
        if pressed_left:
            hero.moveLeft()
        if pressed_right:
            hero.moveRight()
        if pressed_up:
            hero.moveUp()
        if pressed_down:
            hero.moveDown()

        change_dir -= 1
        if(change_dir <= 0):
            change_dir = 120
            direction = random.randint(1,8)
        
        if(direction == 1):
            monster.moveRight()
        elif(direction == 2):
            monster.moveLeft()
        elif(direction == 3):
            monster.moveUp()
        elif(direction == 4):
            monster.moveDown()
        elif(direction == 5): #northeast
            monster.moveUp()
            monster.moveRight()
        elif(direction == 6): #northwest
            monster.moveUp()
            monster.moveLeft()
        elif(direction == 7): #southeast
            monster.moveDown()
            monster.moveRight()
        elif(direction == 8): #southwest
            monster.moveDown()
            monster.moveLeft()
            
        # screen wrapping logic
        monster.getWrap()
        bush = 30
        heroWidth = 32 #same as height
        max_x = (width - bush - heroWidth)
        min_x = bush
        max_y = (height - bush - heroWidth - 2)
        min_y = bush
        
        #adding hero constraints note that bushes are 30 pixels wide
        
        if(hero.x > max_x): #far right constraint
            hero.x = max_x
        if(hero.x < min_x): #far left constraint
            hero.x = min_x
        if(hero.y < min_y): #top constraint
            hero.y = min_y
        if(hero.y > max_y): #bottom constraint
            hero.y = max_y
        # Draw background
        screen.blit(background_image,(0,0))
        # Game display

        screen.blit(hero_image, (hero.x,hero.y))
        screen.blit(monster_image, (monster.x,monster.y))
        pygame.display.update()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
