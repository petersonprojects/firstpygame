import pygame
import random
import math

# work on getting audio to work again and drawin xp bar

mSpeed = 2
gSpeed = 2
hSpeed = 3
points = 0

class Character():
    def __init__(self, startx, starty, speed):
        self.x = startx
        self.y = starty
        self.type = 'character'
        self.speed = speed
        
    def moveRight(self):
        self.x += self.speed
    def moveLeft(self):
        self.x -= self.speed
    def moveUp(self):
        self.y -= self.speed
    def moveDown(self):
        self.y += self.speed
    def moveNW(self):
        self.x -= 1
        self.y -= 1
    def moveNE(self):
        self.x += 1
        self.y -= 1
    def moveSW(self):
        self.x -= 1
        self.y += 1
    def moveSE(self):
        self.x += 1
        self.y += 1
    
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
        self.diagSpeed = hSpeed/2

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
        self.gobDirection = 0
        
    def getGobDir(self):
        return self.gobDirection
    
    def setGobDir(self, randInt):
        self.gobDirection = randInt
    
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
    # winSound = pygame.mixer.Sound('sounds/win.wav')
    # loseSound = pygame.mixer.Sound('sounds/lose.wav')
    clock = pygame.time.Clock()
    #initialize monster, hero and goblins

    direction = 0
    gobdirection = 0
    points = 0
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
    levelUp = False
    
    randommonx = random.randint(0,512)
    randommony = random.randint(0,480)
    randomgobx = random.randint(0,512)
    randomgoby = random.randint(0,480)
    randomgobx2 = random.randint(0,512)
    randomgoby2 = random.randint(0,480)
    
    hero = Hero(175,175, hSpeed)
    monster = Monster(randommonx, randommony, mSpeed)
    goblins = [Goblin(randomgobx,randomgoby, gSpeed),Goblin(randomgobx2,randomgoby2, gSpeed)]
    
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
        change_gobdir -= 2
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
            monster.moveNE()
        elif(direction == 6):
            monster.moveNW()
        elif(direction == 7):
            monster.moveSE()
        elif(direction == 8):
            monster.moveSW()
        
        mondistance = math.sqrt(((hero.x-monster.x)**2) + ((hero.y-monster.y)**2))
        monster.getWrap()
                        
        if(mondistance < 32):
            monsterdead = True
            
        for x in range(len(goblins)):
            
            if(change_gobdir <= 0):
                change_gobdir = 120          
                gobdirection = random.randint(1,8)
                goblins[x].setGobDir(gobdirection)
                
            if(goblins[x].getGobDir() == 1):
                goblins[x].moveRight()
            elif(goblins[x].getGobDir() == 2):
                goblins[x].moveLeft()
            elif(goblins[x].getGobDir() == 3):
                goblins[x].moveUp()
            elif(goblins[x].getGobDir() == 4):
                goblins[x].moveDown()
            elif(goblins[x].getGobDir() == 5):
                goblins[x].moveNE()
            elif(goblins[x].getGobDir() == 6):
                goblins[x].moveNW()
            elif(goblins[x].getGobDir() == 7):
                goblins[x].moveSE()
            elif(goblins[x].getGobDir() == 8):
                goblins[x].moveSW()
                #collision testing
    
            gobdistance = math.sqrt(((hero.x-goblins[x].x)**2)+ ((hero.y-goblins[x].y)**2))
                    
            if gobdistance < 32:
                restart = False
                heroDead = True
                points = 0
                goblins.clear()
                goblins = [Goblin(randomgobx,randomgoby, gSpeed),Goblin(randomgobx2,randomgoby2, gSpeed)]
                
            goblins[x].getWrap()
            
        hero.getBorderCollision()
        
        # Draw background
        screen.blit(background_image,(0,0))    
            
        if loseSoundPlayed == True:
            loseSound.set_volume(0.1)
            loseSound.play(loops=0)
            loseSoundPlayed = False

        if restart == False and heroDead == True:
            font = pygame.font.Font('freesansbold.ttf',32)
            white = (255,255,255)
            blue = (0,0,128)
            text = font.render('Hit Enter to Play Again', True, blue, white)
            screen.blit(text,(80,220))
        
        if(monsterdead == True):
            while monsterdead == True:
                randommonx = random.randint(0,512)
                randommony = random.randint(0,480)
                randomherx = random.randint(30,480)
                randomhery = random.randint(25,448)
                randomgobx = random.randint(0,512)
                randomgoby = random.randint(0,480)
                
                if(randommonx != randomherx and randommony != randomhery):
                    points = points + 1
                    monster = Monster(randommonx,randommony, mSpeed)
                    restart = False
                    monsterdead = False
                    heroDead = False
        
        if levelUp == True:
            goblins.append(Goblin(randomgobx,randomgoby,gSpeed))
            levelUp = False
        
        if(heroDead == False):
            screen.blit(hero_image, (hero.x,hero.y))
        
        if(monsterdead == False):
            screen.blit(monster_image, (monster.x,monster.y))
                                    
        for goblin in goblins:
            screen.blit(goblin_image, (goblin.x,goblin.y))
                    
        
        #drawXP
        maxXP = 100
        if points > 0:
            xpbarX = points*10
        elif points == 0:
            xpbarX = 0
            
        yellow = (250, 218, 94)
        white = (255,255,255)
        black = (0,0,0)
        
        pygame.draw.rect(screen, white, (25,445, maxXP,20))
        pygame.draw.rect(screen, black, (30,450,maxXP-10,10))
        
        if points <= 10:
            pygame.draw.rect(screen, yellow, (30,450,xpbarX,10))
        
        if points == 10:
            levelUp = True
            points = 0
        
        #this essentially resfreshes the screen
        pygame.display.update()

        clock.tick(60) #controls framerate


    if(stop_game == True):
        pygame.quit()

if __name__ == '__main__':
    main()
