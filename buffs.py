from circleshape import CircleShape
import pygame
import random
from constants import PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, LINE_WIDTH, BUFF_RADIUS

class Buff(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    # draw the buff
    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius,LINE_WIDTH)
    def update(self, dt):
        self.radius = BUFF_RADIUS * random.uniform(.9, 1.1)