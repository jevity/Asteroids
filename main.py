import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
   
    # create asteroid field
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()

    # spawn a player object
    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                return
            for bullet in shots:
                if bullet.is_colliding(asteroid):
                    asteroid.split()
                    bullet.kill()


        screen.fill("black")

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # limit to 60 FPS
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
