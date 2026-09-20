import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        num_points = 24
        self.offsets = []
        for i in range(num_points):
            angle = (360 / num_points) * i
            distance_multiplier = random.uniform(0.8, 1.2)
            offset = pygame.Vector2(0, self.radius*distance_multiplier).rotate(angle)
            self.offsets.append(offset)
    def draw(self, screen):
        points = []
        for offset in self.offsets:
            points.append(self.position + offset)
        pygame.draw.polygon(screen, "white", points, 2)
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



        