import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, BUFF_RADIUS, SHOCKWAVE_GROWTH_FACTOR, SHOCKWAVE_TIMER_LIMIT

class ShockCircle(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, BUFF_RADIUS)
        self.radius = BUFF_RADIUS
        self.shockwave_timer = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.radius += dt*SHOCKWAVE_GROWTH_FACTOR
        self.shockwave_timer += dt
        if self.shockwave_timer >= SHOCKWAVE_TIMER_LIMIT:
            self.kill()