import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

group_updatable = pygame.sprite.Group()
group_drawable = pygame.sprite.Group()
group_asteroids = pygame.sprite.Group()
group_shots = pygame.sprite.Group()

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    #asteroid = Asteroid()
    
    Player.containers = (group_updatable, group_drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (group_drawable, group_updatable, group_asteroids)

    AsteroidField.containers = (group_updatable)
    asteroidField = AsteroidField()
    
    Shot.containers = (group_shots)


    gameRunning = True
    while gameRunning:
        ### events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatable in group_updatable:
            updatable.update(dt)

        for asteroid in group_asteroids:
            if asteroid.isColliding(player):
                print("Game over!")
                sys.exit()
            for shot in group_shots:
                if asteroid.isColliding(shot):
                    asteroid.split()
                    shot.kill()

        ### rendering
        screen.fill(color = (0,0,0))
        for drawable in group_drawable:
            drawable.draw(screen)
        for shot in group_shots:
            shot.draw(screen)
            shot.update(dt)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

