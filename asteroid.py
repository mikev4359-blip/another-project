import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle1 = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle1)
        vector2 = self.velocity.rotate(-angle1)
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        small_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        small_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        small_asteroid1.velocity = vector1 * 1.2
        small_asteroid2.velocity = vector2 * 1.2



        