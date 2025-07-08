import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def is_colliding(self, another):
        distance = self.position.distance_to(another.position)
        return distance <= self.radius + another.radius
    
    def is_off_screen(self):
        return (self.position.x + self.radius + SCREEN_KILL_TOLERANCE < 0 or
                self.position.x - self.radius - SCREEN_KILL_TOLERANCE > SCREEN_WIDTH or
                self.position.y + self.radius + SCREEN_KILL_TOLERANCE < 0 or
                self.position.y - self.radius - SCREEN_KILL_TOLERANCE > SCREEN_HEIGHT)


    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass