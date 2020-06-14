import pygame
import random
import math

# work on getting audio to work again and drawin xp bar

mSpeed = 2
gSpeed = 4
hSpeed = 4
diagSpeed = 0
class Character():
    def __init__(self, startx, starty, speed):
        self.x = startx
        self.y = starty
        self.type = 'character'
        self.diagSpeed = hSpeed/2
        self.speed = speed
    def moveRight(self):
        self.x += hSpeed
    def moveLeft(self):
        self.x -= hSpeed
    def moveUp(self):
        self.y -= hSpeed
    def moveDown(self):
        self.y += hSpeed
    def moveNW(self):
        self.x -= self.diagSpeed
        self.y -= self.diagSpeed
    def moveNE(self):
        self.x += self.diagSpeed
        self.y -= self.diagSpeed
    def moveSW(self):
        self.x -= self.diagSpeed
        self.y += self.diagSpeed
    def moveSE(self):
        self.x += self.diagSpeed
        self.y += self.diagSpeed
    
    def getWrap(self):
        
        if(self.x > 512):
            self.x = 0
        if(self.x < -30):
            self.x = 512
        if(self.y > 480):
            self.y = 0
        if(self.y < -32):
            self.y = 480
        
class Hero(Character):
    def __init__(self, startx, starty, speed):
        self.x = startx
        self.y = starty
        self.name = 'hero'
        self.speed = speed
        self.points = 0
    
    def addPoint(self, getPoint):
        self.points += 1

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
class Monster(Character):
    def __init__(self, startx, starty, speed):
        self.x = startx
        self.y = starty
        self.name = 'monster'
        self.speed = speed
        self.diagSpeed = mSpeed/2
        
    def getWrap(self):
        if(self.x > 512):
            self.x = 0
        if(self.x < -30):
            self.x = 512
        if(self.y > 480):
            self.y = 0
        if(self.y < -32):
            self.y = 480
class Goblin(Character):
    def __init__(self, startx, starty, speed):
        self.x = startx
        self.y = starty
        self.name = 'goblin'
        self.speed = speed
        self.diagSpeed = gSpeed/2
        
def main():
    # Game initialization
    width = 512
    height = 480
    change_dir = 0
    change_gobdir = 0

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My PyGame')
    
    #image loading
    background_image = pygame.image.load('images/background.png').convert_alpha() #512x480
    hero_image = pygame.image.load('images/hero.png').convert_alpha() #32x32
    monster_image = pygame.image.load('images/monster.png').convert_alpha() #30x32
    goblin_image = pygame.image.load('images/goblin.png').convert_alpha() #32x32
    winSound = pygame.mixer.Sound('sounds/win.wav')
    loseSound = pygame.mixer.Sound('sounds/lose.wav')
    clock = pygame.time.Clock()
    #initialize monster, hero and goblins

    direction = 0
    gobdirection = 0
    points = 0
    getPoint = False
    pressed_left = False
    pressed_right = False
    pressed_up = False
    pressed_down = False
    stop_game = False
    monsterdead = False
    winSoundPlayed = False
    loseSoundPlayed = False
    heroDead = False
    restart = False
    spawned = False
    monster = Monster(60, 400, mSpeed)
    hero = Hero(200,200, hSpeed)
    randomgobx = random.randint(0,512)
    randomgoby = random.randint(0,480)
    goblin = Goblin(randomgobx,randomgoby, gSpeed)
    
    
    while not stop_game:
        
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
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    restart = True
                    monsterdead = False
                    heroDead = False
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
        change_gobdir -= 1
        if(change_dir <= 0):
            change_dir = 120
            direction = random.randint(1,8)
        if(change_gobdir <= 60):
            change_gobdir = 120
            gobdirection = random.randint(1,8)
            
        if(direction == 1):
            monster.moveRight()
        elif(direction == 2):
            monster.moveLeft()
        elif(direction == 3):
            monster.moveUp()
        elif(direction == 4):
            monster.moveDown()
        elif(direction == 5):
            monster.moveNE()
        elif(direction == 6):
            monster.moveNW()
        elif(direction == 7):
            monster.moveSE()
        elif(direction == 8):
            monster.moveSW()
        
        if(gobdirection == 1):
            goblin.moveRight()
        elif(gobdirection == 2):
            goblin.moveLeft()
        elif(gobdirection == 3):
            goblin.moveUp()
        elif(gobdirection == 4):
            goblin.moveDown()
        elif(gobdirection == 5):
            goblin.moveNE()
        elif(gobdirection == 6):
            goblin.moveNW()
        elif(gobdirection == 7):
            goblin.moveSE()
        elif(gobdirection == 8):
            goblin.moveSW()
            
        
        #collision testing
        mondistance = math.sqrt(((hero.x-monster.x)**2) + ((hero.y-monster.y)**2))
        gobdistance = math.sqrt(((hero.x-goblin.x)**2)+ ((hero.y-goblin.y)**2))
        if(mondistance < 32):
            getPoint = True
            monsterdead = True
            restart = False
        
        if(getPoint == True):
            hero.addPoint(getPoint)
            getPoint = False
            print(f"Points: {hero.points}")
            XPBarSize = hero.points
            
        if gobdistance < 32:
            restart = False
            loseSoundPlayed = True
            heroDead = True
            points = 0

        # screen wrapping logic
        monster.getWrap()
        goblin.getWrap()
        hero.getBorderCollision()
        
        # Draw background
        screen.blit(background_image,(0,0))
        
        if(heroDead == False):
            screen.blit(hero_image, (hero.x,hero.y))
            
        screen.blit(goblin_image, (goblin.x,goblin.y))
        
        if(monsterdead == False):
            screen.blit(monster_image, (monster.x,monster.y))
        
        ## put xp bar drawing here.
        #screen.blit( (30,430)
        
        if(monsterdead == True):
            winSound.set_volume(0.1)
            if(winSoundPlayed == False):
                winSound.play(loops=0)
                winSoundPlayed = True
            
        if loseSoundPlayed == True:
            loseSound.set_volume(0.1)
            if loseSoundPlayed == False:
                loseSound.play(loops=0)
                loseSoundPlayed = True

            if restart == False:
                font = pygame.font.Font('freesansbold.ttf',32)
                white = (255,255,255)
                blue = (0,0,128)
                text = font.render('Hit Enter to Play Again', True, blue, white)
                screen.blit(text,(80,220))
        
        if(restart == True):
            while spawned == False:
                randommonx = random.randint(0,512)
                randommony = random.randint(0,480)
                randomherx = random.randint(30,480)
                randomhery = random.randint(25,448)
                randomgobx = random.randint(0,512)
                randomgoby = random.randint(0,480)
                
                if(randommonx != randomherx and randommony != randomherx):
                    monster = Monster(randommonx,randommony, mSpeed)
                    hero = Hero(randomherx, randomhery, hSpeed)
                    goblin = Goblin(randomgobx, randomgoby, gSpeed)
                    spawned = True
                    restart = False
        #this essentially resfreshes the screen
        pygame.display.update()

        clock.tick(60) #controls framerate


        

    if(stop_game == True):
        pygame.quit()

if __name__ == '__main__':
    main()
