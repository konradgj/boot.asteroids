import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, pygame.Color(255, 0, 0), self.position, self.radius, 2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        print(self.position)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(angle)
        vec2 = self.velocity.rotate(-angle)

        newRadius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position[0], self.position[1], newRadius)
        a2 = Asteroid(self.position[0], self.position[1], newRadius)
        a1.velocity = vec1 * 1.2
        a2.velocity = vec2 * 1.2
