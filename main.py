import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = {asteroids, updatable, drawable}
    AsteroidField.containers = {updatable}

    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return

        for sprite in updatable:
            sprite.update(dt)

        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # limit to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()