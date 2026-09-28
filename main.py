import pygame
import sys
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from circleshape import CircleShape
from shot import Shot
from gameover import game_over_screen, game_over_text


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    font = pygame.font.Font(None,36)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    asteroidfield1 = AsteroidField()
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    game_over = False
    score = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for players in drawable:
            players.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score += 100
        for asteroid in asteroids:
            if player1.collides_with(asteroid):
                game_over = True
                log_event("player_hit")
        if game_over == True:
            screen.blit(game_over_screen, (0,0))
            screen.blit(game_over_text,(520,SCREEN_HEIGHT/2))
        if game_over == False:
            updatable.update(dt)
            print(shots)
        score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surface, (10,10))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
        
    