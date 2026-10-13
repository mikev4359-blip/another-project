import pygame
pygame.mixer.quit()
pygame.mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
pygame.mixer.init()
pygame.init()
actual_freq, actual_size, actual_chan = pygame.mixer.get_init()
print(f"--- SYSTEM AUDIO OPENED AT: {actual_freq} Hz ---")
import random
from constants import SCREEN_HEIGHT, BUFF_BREAK_SPAWN_COUNT_MIN, BUFF_BREAK_SPAWN_COUNT_MAX
from constants import BUFF_SPAWN_TIMER_MIN, SCREEN_WIDTH, BASE_SCORE_ADD, PLAYER_COLLIDE_FUDGE_FACTOR
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from buffs import Buff, listed_buffs
from logger import log_event
from shot import Shot
from shockwave import ShockCircle
from gameover import game_over_screen, game_over_text, game_over_text_rect


def main():
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    font = pygame.font.Font(None,36)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    buffs = pygame.sprite.Group()
    shockcircles = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    Buff.containers = (buffs, drawable, updatable)
    ShockCircle.containers = (shockcircles, drawable, updatable)
    asteroidfield1 = AsteroidField()
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    game_over = False
    score = 0
    breaks = 0
    buff_spawn_timer = 0
    break_limit = random.uniform(BUFF_BREAK_SPAWN_COUNT_MIN,BUFF_BREAK_SPAWN_COUNT_MAX)
    death_explosion = pygame.mixer.Sound("sounds/boom.wav")
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER) and game_over == True:
                    #Empty Drawable Parameters -----------
                    drawable.empty()
                    asteroids.empty()
                    shots.empty()
                    updatable.empty()
                    buffs.empty()
                    shockcircles.empty()
                    #Empty Score Parameters --------------
                    score = 0
                    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                    #Reset Asteroid Field
                    asteroidfield1 = AsteroidField()
                    #Empty Buff Parameters ---------------
                    breaks = 0
                    break_limit = random.uniform(BUFF_BREAK_SPAWN_COUNT_MIN, BUFF_BREAK_SPAWN_COUNT_MAX)
                    buff_spawn_timer = 0
                    game_over = False
        screen.fill("black")
        buff_spawn_timer += dt
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.hit()
                    score += BASE_SCORE_ADD
                    breaks += 1
                    if breaks >= break_limit and buff_spawn_timer > BUFF_SPAWN_TIMER_MIN:
                        random_buff = random.choice(listed_buffs)
                        spawn_buff1 = random_buff(asteroid.position.x, asteroid.position.y)
                        breaks = 0
                        break_limit = random.uniform(BUFF_BREAK_SPAWN_COUNT_MIN,BUFF_BREAK_SPAWN_COUNT_MAX)
                        buff_spawn_timer = 0
        for buff in buffs:
            if player1.collides_with(buff):
                buff.apply(player1)
        for asteroid in asteroids:
            for shock in shockcircles:
                if shock.collides_with(asteroid):
                    asteroid.split()
                    score += BASE_SCORE_ADD
        for asteroid in asteroids:
            if not game_over and player1.collides_with(asteroid,PLAYER_COLLIDE_FUDGE_FACTOR):
                game_over = True
                death_explosion.play()
                log_event("player_hit")
                break
        if game_over == True:
            screen.blit(game_over_screen, (0,0))
            screen.blit(game_over_text,game_over_text_rect)
        if game_over == False:
            updatable.update(dt)
        score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surface, (10,10))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
        
    