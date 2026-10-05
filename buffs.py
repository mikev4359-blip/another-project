from circleshape import CircleShape
import pygame
import random
from constants import PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, LINE_WIDTH, BUFF_RADIUS

class Buff(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, BUFF_RADIUS)
    # to be overridden by subclass buffs
    def apply(self,player):
         pass

class RapidFire(Buff):
    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius,LINE_WIDTH)
    def update(self, dt):
        self.radius = BUFF_RADIUS * random.uniform(.9, 1.1)
    def apply(self, player):
        self.kill()
        player.shot_cooldown = 0.1
        player.rf_buff_cooldown = 7

class MegaShot(Buff):
    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius,LINE_WIDTH)
    def update(self, dt):
        self.radius = BUFF_RADIUS * random.uniform(.9, 1.1)
    def apply(self, player):
        self.kill()
        player.ms_buff_cooldown = 7

listed_buffs = [RapidFire, MegaShot]

