# Game building excersize for Programming Hero course
import os
import pygame
try:
    import android
except ImportError:
    android = None

# initial screen and background variables:
screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load('background.png')

# initial planet variables:
planet_x = 140
planet = pygame.image.load('p_one.png')
move_direction = 'right'

# initial spaceship variables:
spaceship = pygame.image.load('spaceship.png')

# initial bullet variables:
bullet = pygame.image.load('bullet.png')
fired = False
bullet_y = 500

# create clock variable for use in fps control:
clock = pygame.time.Clock()

keep_alive = True
# game loop:
while keep_alive:
    
    # key press handler, fire the bullet:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] == True:
        fired = True
    if fired is True:
        bullet_y = bullet_y - 5
        # reset bullet position after firing:
        if  bullet_y == 50:
            fired = False
            bullet_y = 500
            
    screen.blit(background, [0, 0])
    screen.blit(bullet, [180, bullet_y])
    screen.blit(spaceship, [160, 500])
        
    # planet left and right movement:
    if move_direction == 'right':
        planet_x = planet_x + 5
        if planet_x == 300:
            move_direction = 'left'
    else:
        planet_x = planet_x - 5
        if planet_x == 0:
            move_direction = 'right'
            
    screen.blit(planet, [planet_x, 50])
    
    # refresh display at max 60 fps:
    pygame.display.update()
    clock.tick(60)
            
    
    
    
            
    
    
    
    
    
