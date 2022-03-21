# Game building excersize for Programming Hero course

import pygame

# initial screen and background variables:
screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load('background.png')

# initial planet variables:
planets = ['p_one.png', 'p_two.png', 'p_three.png']
p_index = 0
planet_x = 140
planet = pygame.image.load(planets[p_index])
move_direction = 'right'

# initial spaceship variable:
spaceship = pygame.image.load('spaceship.png')

# initial bullet variables:
bullet = pygame.image.load('bullet.png')
fired = False
bullet_y = 500

# create clock variable for use in fps control:
clock = pygame.time.Clock()

# game loop:
keep_alive = True
while keep_alive:
    
    # key press handler:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_alive = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            keep_alive = False
        elif event.type == pygame.K_SPACE or event.type == pygame.FINGERUP: # something here isn't working correctly
            fired = True
        else:
            print(event.type)
    
    # fire the bullet:        
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
    
    # bullet and planet collision:
    if bullet_y < 80 and 120 < planet_x < 180:
        p_index += 1
        # iterate through planets list:
        if p_index < len(planets):
            planet = pygame.image.load(planets[p_index])
            planet_x = 10
        # if no more planets in list, win condition is met:
        else:
            print('Congratulations!/nYou Win!')
            keep_alive = False
    
    # refresh display at max 60 fps:
    pygame.display.update()
    clock.tick(60)
            
    
    
    
            
    
    
    
    
    
