import pygame
import random
from objects.circleshape import CircleShape
from objects.particle import Particle
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            # explode asteroid
            for i in range(0, PARTICLE_NUMBER):
                angle = 360 / PARTICLE_NUMBER * i
                particle_velocity = pygame.Vector2(0, 1).rotate(angle) * PARTICLE_SPEED
                particle = Particle(self.position.x, self.position.y)
                particle.velocity = particle_velocity
            return
        new_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(new_angle)
        vector2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vector1 * 1.2
        asteroid2.velocity = vector2 * 1.2


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.is_off_screen():
            self.kill()