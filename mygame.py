import pygame
import random
import math

mSpeed = 2
gSpeed = 3
hSpeed = 3

class Character():
    def __init__(self):
        pass
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
    def getBorderCollision(self):
        width = 512
        height = 480
        bush = 30
        heroWidth = 32 #same as height
        max_x = (width - bush - heroWidth)
        min_x = bush
        max_y = (height - bush - heroWidth - 2)
        min_y = bush

        if(self.x > max_x): #far right constraint
            self.x = max_x
        if(self.x < min_x): #far left constraint
            self.x = min_x
        if(self.y < min_y): #top constraint
            self.y = min_y
        if(self.y > max_y): #bottom constraint
            self.y = max_y
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
    change_dir = 120

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My PyGame')
    
    #image loading
    background_image = pygame.image.load('images/background.png').convert_alpha() #512x480
    hero_image = pygame.image.load('images/hero.png').convert_alpha() #32x32
    monster_image = pygame.image.load('images/monster.png').convert_alpha() #30x32
    winSound = pygame.mixer.Sound('sounds/win.wav')
    
    clock = pygame.time.Clock()
    #initialize monster, hero and goblins

    direction = 30
    pressed_left = False
    pressed_right = False
    pressed_up = False
    pressed_down = False
    stop_game = False
    monsterdead = False
    winSoundPlayed = False
    restart = False
    spawned = False
    monster = Monster(60, 400)
    hero = Hero(200,200)
    
    
    while restart == False or not stop_game:
        
        for event in pygame.event.get():
            
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
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    pressed_up = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    pressed_down = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    pressed_left = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    pressed_right = False
            
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    restart = True
                    monsterDead = False
                    print("Return key pressed.")
        #for event loop end
        
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
        elif(direction == 5):
            monster.moveUp()
            monster.moveRight()
        elif(direction == 6):
            monster.moveUp()
            monster.moveLeft()
        elif(direction == 7):
            monster.moveDown()
            monster.moveRight()
        elif(direction == 8):
            monster.moveDown()
            monster.moveLeft()
            
        
        #collision testing
        distance = math.sqrt(((hero.x-monster.x)**2) + ((hero.y-monster.y)**2))

        if(distance < 32):
            monsterdead = True

        # screen wrapping logic
        monster.getWrap()
        hero.getBorderCollision()
        
        # Draw background
        screen.blit(background_image,(0,0))
        screen.blit(hero_image, (hero.x,hero.y))
        
        if(monsterdead == False):
            screen.blit(monster_image, (monster.x,monster.y))
        
        if(monsterdead == True):
            winSound.set_volume(0.1)
            if(winSoundPlayed == False):
                winSound.play(loops=0)
                winSoundPlayed = True
            
            if restart == False:
                font = pygame.font.Font('freesansbold.ttf',32)
                white = (255,255,255)
                green = (0,255,0)
                blue = (0,0,128)
                text = font.render('Hit Enter to Play Again', True, blue, white)
                screen.blit(text,(80,220))
        
        if(restart == True):
            while spawned == False:
                randommonx = random.randint(0,512)
                randommony = random.randint(0,480)
                randomherx = random.randint(30,480)
                randomhery = random.randint(25,448)
                
                if(randommonx != randomherx and randommony != randomherx):
                    monster = Monster(randommonx,randommony)
                    hero = Hero(randomherx, randomhery)
                    spawned = True
        #this essentially resfreshes the screen
        pygame.display.update()

        clock.tick(60) #controls framerate

    if(stop_game == True):
        pygame.quit()

if __name__ == '__main__':
    main()
